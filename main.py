import plotLight as pl


def main():
    # Initialize variables for data wanted
    starInput = ""

    # Ask urser for star to look up
    starInput = input("Star for Light Curve: ")

    # Receives light curve from plotLight and displays it
    graph = pl.plotLight(starInput)

main()
