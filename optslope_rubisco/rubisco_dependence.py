#!/usr/local/bin/python3

import optslope_rubisco
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from cobra.io import read_sbml_model
from importlib_resources import read_text
from matplotlib import cm
from matplotlib.colors import ListedColormap
from optslope import calculate_slope_multi
from tqdm import tqdm


def main(num_processes: int = 1) -> None:
    """Calculate a DataFrame with slopes of all KOs on all CSs."""

    FULL_RESULT_PATH = f"optslope_rubisco/results.csv"
    FIGURE_PATH = f"optslope_rubisco/heatmap.pdf"

    wt_model = read_sbml_model(read_text(optslope_rubisco, optslope_rubisco.WILDTYPE_MODEL))

    dfs = []
    print(f"Calculating slopes for up to 2 knockouts, and "
          f"for {len(optslope_rubisco.CARBON_SOURCES_LIST)} carbon source combinations")

    for carbon_sources in tqdm(optslope_rubisco.CARBON_SOURCES_LIST,
                               total=len(optslope_rubisco.CARBON_SOURCES_LIST),
                               desc="Carbon Sources"):
        df = calculate_slope_multi(
            wt_model=wt_model,
            carbon_sources=carbon_sources,
            single_knockouts=optslope_rubisco.SINGLE_KOS,
            target_reaction=optslope_rubisco.TARGET_REACTION,
            max_knockouts=2,
            num_processes=num_processes,
            chunksize=100)

        dfs.append(df)

    result_df = pd.concat(dfs)
    result_df = result_df.round(3)

    # write all the slopes to a CSV file
    with open(FULL_RESULT_PATH, 'w') as fp:
        result_df.to_csv(fp)

    # the knockouts are given as 2-tuples, we first need to convert them to 2
    # columns of string values
    N = len(optslope_rubisco.SINGLE_KOS)
    data_mat = np.zeros((3*N, 3*N)) * np.nan
    for row in result_df.itertuples():
        if len(row.knockouts) == 0 or len(row.carbon_sources) == 0:
            continue

        i0 = optslope_rubisco.SINGLE_KOS.index(row.knockouts[0])
        if len(row.knockouts) == 1:
            i1 = i0
        else:
            i1 = optslope_rubisco.SINGLE_KOS.index(row.knockouts[1])

        i2 = optslope_rubisco.CARBON_SOURCES_LIST.index(row.carbon_sources)

        x = 3 * i0 + i2 // 3
        y = 3 * i1 + i2 % 3
        data_mat[x, y] = row.slope

    fig, ax = plt.subplots(1, 1, figsize=(12, 10))

    # make a colormap which assigns a red color to values around 0,
    # and uses Viridis for all positive values
    cmap = ListedColormap([[150 / 256, 10 / 256, 50 / 256, 1]] +
                          cm.get_cmap('viridis', 50).colors.tolist())

    g = sns.heatmap(data_mat.T, vmin=-0.5, vmax=35, cmap=cmap,
                    cbar_kws={'label': 'slope'}, ax=ax)
    g.set_facecolor('darkgrey')
    ax.set_xticks(np.arange(1.5, 3*N, 3))
    ax.set_yticks(np.arange(1.5, 3*N, 3))
    ax.set_xticklabels(optslope_rubisco.SINGLE_KOS, rotation=90, ha='center', fontsize=12)
    ax.set_yticklabels(optslope_rubisco.SINGLE_KOS, rotation=0, va='center', fontsize=12)

    ax.text(data_mat.shape[0] * 0.6 + 8, data_mat.shape[0] * 0.02,
            "Carbon Sources", fontsize=12, va='center', ha='center')
    for i, cs in enumerate(optslope_rubisco.CARBON_SOURCES_LIST):
        y = i // 3
        x = 2 - (i % 3)
        ax.text(data_mat.shape[0] * 0.6 + 8 * x,
                data_mat.shape[0] * 0.1 + 8 * y,
                cs[0], fontsize=12, va='center', ha='center')

    fig.tight_layout()
    sys.stderr.write(f"Writing heatmap figure to {FIGURE_PATH}\n")
    fig.savefig(FIGURE_PATH)


if __name__ == '__main__':
    main(4)