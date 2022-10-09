import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    # todo: load the "results.csv" file from the mia-results directory
    # todo: read the data into a list
    # todo: plot the Dice coefficients per label (i.e. white matter, gray matter, hippocampus, amygdala, thalamus)
    #  in a boxplot
    fig, ax = plt.subplots(1, 1, figsize=[5.5,6], dpi=300)
    db=pd.read_csv("mia-result/2022-10-08-21-24-34/results.csv", sep=";")
    db.boxplot(column='DICE', by="LABEL",ax=ax, ylabel="Dice Score", xlabel=" ", rot=45)
    #plt.show()
    fig.savefig('BoxGraphDice.jpg', dpi=300)

    # alternative: instead of manually loading/reading the csv file you could also use the pandas package
    # but you will need to install it first ('pip install pandas') and import it to this file ('import pandas as pd')

if __name__ == '__main__':
    main()
