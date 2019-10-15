"""Through this file it is intended to analyse CNC milling experiment data, in order to come up with potential
breakthroughs in terms of process optimization. Here, a relation between the measured variables and tool wear
is sought. For that end, the following steps are undertaken:

1) Importing Files;
2) Exploratory Data Analysis
3) """

#### 1) IMPORTING FILES ####
import glob
import argparse

# construct argument parser and parse arguments (C:/Users/thiag/Desktop/MachineLearning/projects/toolwear_cncmilling/*.csv)
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "path to input dataset")
ap.add_argument("-e", "--extension", required = True, help = "extension of the file")
args = vars(ap.parse_args())

# grab paths of the experiments .csv files
print("[INFO] loading files...")
experimentsPaths = glob.glob(args["dataset"] + args["extension"])

#### 2) EXPLORATORY DATA ANALYSIS ####
from dataloader import DataLoader
import matplotlib.pyplot as plt

# load datasets: experiments contain the measured data; outputs contain the results of the experiment
dl = DataLoader()
experiments, outputs = dl.load(experimentsPaths)

""" Plots of the Data are analyzed in the Jupyter Notebook file """
spindle_inertia = 12.0 # kg.m²
