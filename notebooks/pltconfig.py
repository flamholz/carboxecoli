import seaborn as sns
from matplotlib import pyplot as plt

greys = sns.color_palette('Greys', n_colors=8)
greens = sns.color_palette('Greens', n_colors=8)
blue_greens = sns.color_palette("GnBu_d", n_colors=12)
blues = sns.color_palette('Blues', n_colors=8)
oranges = sns.color_palette('Oranges', desat=0.8)
purples = sns.color_palette('Purples', n_colors=8)
reddish_purple = sns.set_hls_values(sns.xkcd_rgb['reddish purple'], 0.9, 0.3, 1)
reddish = sns.xkcd_rgb['raspberry']

rcParams = plt.rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Myriad Pro', 'Roboto', 'Tahoma', 'DejaVu Sans',
                               'Lucida Grande', 'Verdana']