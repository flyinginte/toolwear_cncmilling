"""Through this file it is intended to analyse CNC milling experiment data, in order to come up with potential
breakthroughs in terms of process optimization. Here, a relation between the measured variables and tool wear
is sought. For that end, the following steps are undertaken:

1) DATA VISUALIZATION;
2) """

#### Data Visualization ####
import glob
import argparse
from imutils import paths

# construct argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "path to input dataset")
ap.add_argument("-e", "--extension", required = True, help = "extension of the file")
args = vars(ap.parse_args())

# grab paths of the experiments .csv files
print("[INFO] loading files...")
experimentsPaths = glob.glob(args["dataset"] + args["extension"])






