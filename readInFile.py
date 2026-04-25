import lightkurve as lk


def readInFile(star):
    # Initialize search_result list
    search_result = []

    # Gather data from NASA databeses from required star
    search_result = lk.search_lightcurve(star, author='Kepler', cadence="long")
    lightInfo = search_result[4].download()

    # Used to check all the columns of data imported I didn't need
    # print(lightInfo.columns)

    # Remove unneeded columns
    lightInfo.remove_columns(
        ["sap_flux_err", "quality", "timecorr", "centroid_col", "centroid_row", "cadenceno", "sap_flux", "sap_bkg",
         "sap_bkg_err", "pdcsap_flux",
         "pdcsap_flux_err", "sap_quality", "psf_centr1", "psf_centr1_err", "psf_centr2", "psf_centr2_err", "mom_centr1",
         "mom_centr1_err", "mom_centr2"
            , "mom_centr2_err", "pos_corr1", "pos_corr2"])

    return lightInfo
