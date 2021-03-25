#! /usr/bin/env python3

#Scripting for Biologists Exercise: Tabular Data

"A script which performs and plots linear regressions of petal length vs. sepal length for the three types of irises in iris.csv."

import os
import sys
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def gen_filename(speciesname):
    """
    Generates a file name for the plot based on species name.
    
    Parameters
    ----------
    speciesname : str
        The name of the species you will be plotting in whatever format you want it to appear in the file name.

    Returns
    -------
    str
        The file name.
    """
    if speciesname:
        plot_path = "{0}-petal-v-sepal-length-regression.png".format(speciesname)
    return plot_path


def regress_and_plot(species, plot_path = None):
    """
    Gets the lines of data out of iris.csv based on the species entered.
    
    Parameters
    ----------
    species: str
            The name of the species for which you want data separated by underscores and surrounded by quotation marks (""). 
            Example: "Iris_virginica"
    Returns
    -------
    The plot is saved and nothing is returned.
    """
    #if plot_path is not provided, use the gen_filename path to generate it
    if not plot_path:
        plot_path = gen_filename(species)

    #read in iris.csv and select desired species
    dataframe = pd.read_csv("iris.csv")
    dataframespecies = dataframe[dataframe.species == species]
    #check that the species is in iris.csv
    if len(dataframespecies.columns) == 0:
        print('Species not in iris.csv.')
    else:
        #select variables petal length and sepal length
        x = dataframespecies.petal_length_cm
        y = dataframespecies.sepal_length_cm
        #perform linear regression
        regression = stats.linregress(x, y)
        slope = regression.slope
        intercept = regression.intercept
        #plot the points and the regressed line, save plot as .png
        plt.scatter(x, y, label = 'Data')
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.legend()
        plt.savefig(plot_path)
        quit()

if __name__ == '__main__':

    regress_and_plot("Iris_virginica")

    regress_and_plot("Iris_versicolor")

    regress_and_plot("Iris_setosa")





