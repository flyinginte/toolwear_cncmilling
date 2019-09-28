import pandas as pd

class DataLoader:
    def __init__(self, experimentsPaths):
        pass

    def load(self, experimentsPaths, verbose = 1):
        # initialize the list of experiments
        experiments = []

        # loop over the .csv files
        for (experimentPath) in enumerate(experimentsPaths):
            # read the file from the address given
            file_exp = pd.read_csv(experimentPath)
            experiments.append(file_exp)

        return experiments




