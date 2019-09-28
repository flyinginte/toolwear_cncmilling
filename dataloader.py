import pandas as pd

class DataLoader:
    def __init__(self):
        pass

    def load(self, path, verbose = 1):
        # initialize the list of experiments
        experiments = []
        outputs = []

        # loop over the .csv files
        for (experimentPath) in enumerate(path):
            # read the file from the address given
            file_exp = pd.read_csv(experimentPath[1]) # [1] = address stored at the tuple
            experiments.append(file_exp)
        outputs = experiments[-1]
        experiments = experiments[:-1]

        return experiments, outputs




