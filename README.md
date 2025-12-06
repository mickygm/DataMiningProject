# Deepfake Audio Detection
# By McKinley Morris, Zach Cobb, Sai Keerthan Proddato

## Project Objective
The proposed research aims to build an automated system that can detect deepfake audio signals based on the techniques of data mining and machine learning. A dataset of real audio signals and artificially generated deepfake audio signals was built. After carrying out the necessary preprocessing steps on the dataset, the following spectral features have been taken into consideration:
- MFCC
- Spectral Centroid
- Spectral Bandwidth
- Spectral Rolloff
- Spectral Flatness
- Zero Crossing Rate
- RMS
- Spectral Flux

A number of modeling techniques have been assessed, including:
- Vanilla KNN
- KNN + PCA
- KNN + OPTICS
- KNN + ISOLATION FOREST

## Required Packages
- numpy
- pandas
- librosa
- soundfile
- scikit-learn

## How to Run the Code
- You can run the project interactively using a Jupyter Notebook. 
- An HTML copy of the notebook is also included in the repository for easy viewing without execution.
