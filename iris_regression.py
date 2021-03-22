#! /usr/bin/env python3

#Scripting for Biologists Exercise: Tabular Data

"A script which performs and plots linear regressions of petal length vs. sepal length for the three types of irises in iris.csv."

import panda as pd
import matplotlib.pyplot as plt
from scipy import stats

def regress_and_plot(species):
    """
    Gets the lines of data out of iris.csv based on the species entered.
    
    Parameters
    ----------
    species: str
            The name of the species for which you want data.
    Returns
    -------
    regression slope, intercept, and .png of the plot or None
            A linear regression of sepal length vs petal length data from the rows of 
            data in iris.csv which pertain to the species entered or None if the species 
            entered is not in iris.csv.
    """
    dataframe = read.csv("iris.csv")
    dataframespecies = dataframe[dataframe.species == species]
    x = dataframespecies.petal_length_cm
    y = dataframespecies.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress.png")
    #if dataframespecies isn't empty
    #return slope, intercept, plot



