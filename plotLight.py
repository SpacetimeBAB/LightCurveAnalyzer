from matplotlib import pyplot as plt
from readInFile import readInFile as starInfo
import numpy as np


def plotLight(star):

    # Call readInFile for lightInfo results for star
    info = starInfo(star)

    # Used to check array type
    # print(type(info.time))

    # Receive column data into separate variables and make sure it's just the data and not the unit
    time = info.time.value
    flux = info.flux.value

    # Uses matplot to plot variables from NASA
    plt.plot(time, flux)
    plt.title(f"{star.title()} Light Curve")
    plt.xlabel("Time in days")
    plt.ylabel("Flux in electrons / s")

    return plt.show()

