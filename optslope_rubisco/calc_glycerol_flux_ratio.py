#!/usr/local/bin/python3

import optslope_rubisco
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from copy import deepcopy
from cobra.io import read_sbml_model
from importlib_resources import read_text
from matplotlib import cm
from optlang.interface import OPTIMAL
from optslope.util import EPSILON
from tqdm import tqdm


def make_ko_model(wt_model, knockouts):
    ko_model = deepcopy(wt_model)
    for ko in knockouts:
        for k in ko.split('|'):
            ko_model.reactions.get_by_id(k).knock_out()
    return ko_model


def main():
    """Calculate a DataFrame with slopes of all KOs on all CSs."""

    wt_model = read_sbml_model(read_text(optslope_rubisco, optslope_rubisco.WILDTYPE_MODEL))
    knockouts = ('RPI', 'EDD|EDA')

    
    for carbon_sources in tqdm(optslope_rubisco.CARBON_SOURCES_LIST,
                               total=len(optslope_rubisco.CARBON_SOURCES_LIST),
                               desc="Carbon Sources"):

        print(carbon_sources)
        ko_model = make_ko_model(wt_model, knockouts)

        exchange_ids = ["EX_" + cs + "_e" for cs in carbon_sources]
        for ex_id in exchange_ids:
            ko_model.reactions.get_by_id(ex_id).lower_bound = -1000

        rxn_target = ko_model.reactions.get_by_id(optslope_rubisco.TARGET_REACTION)

        # First, try to see if growth depends on the target at all. If there is
        # growth without it, the slope is 0
        rxn_target.bounds = (0, 0)
        solution = ko_model.optimize()
        if solution.status == OPTIMAL and solution.objective_value > EPSILON:
            print('0 slope for', carbon_sources)

        rxn_target.bounds = (1.0 - EPSILON, 1.0 + EPSILON)
        solution = ko_model.optimize()

        # If even with the target reaction on, we still can't find solutions
        # then the slope is undefined
        if solution.status != OPTIMAL or solution.objective_value < EPSILON:
            print('undefined slope for', carbon_sources)

        slope = 1.0 / solution.objective_value
        print(slope)
        print(ko_model.metabolites.dhap_c.summary())
        print(ko_model.metabolites.get_by_id('3pg_c').summary())



if __name__ == '__main__':
    main()