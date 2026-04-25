import numpy as np
import lightkurve as lk
import matplotlib as inline


def readInFile(star):
    search_result = lk.search_lightcurve('Kepler-8', author='Kepler', cadence = "long")
    klc = search_result[4].download()
    print(klc)
    klc.plot()
readInFile("salah")