# Financial Data Analysis Pipeline using Decision tree Algorithm with Noise-Elimination 

This repository contains scripts for preprocessing financial data and building an XGBoost classification model to predict price movement. The following sections detail the structure of the repository and guide you through using these scripts effectively.

## Table of Contents

- [Introduction](#introduction)
- [Preprocessing Script: preprocess.py](#preprocessing-script-preprocesspy)
- [Modeling Script: main.py](#modeling-script-mainpy)
- [Usage](#usage)
- [License](#license)

## Introduction

In the world of financial analysis, preparing data and constructing accurate models are crucial steps. This repository offers two key scripts: `preprocess.py` for data preprocessing and `main.py` for creating an XGBoost model.

## Preprocessing Script: preprocess.py
The preprocess.py script performs the following steps:

- Imports necessary libraries: numpy, pandas.
- Defines the kendall_correlation function to calculate Kendall Correlation coefficients.
- Reads historical price data from a CSV file (BTC-USD.csv).
- Extracts the Close Price data and calculates Kendall Correlation coefficients using the kendall_correlation function.
- Adds the calculated correlation values as a new column 'NET' to the price data.
- Calculates target labels for price movement (0 for price decrease, 1 for price increase) and adds them as a new column 'Sign'.
- Saves the preprocessed data to a new CSV file (filtered_prices_2021.csv).
## Modeling Script: main.py
The main.py script demonstrates the following workflow:

- Imports necessary libraries: sklearn.metrics, pandas, xgboost, numpy, train_test_split.
- Reads target labels (Shifted_price_data.csv) and preprocessed historical data (filtered_prices.csv).
- Scales and normalizes the target labels and price data.
- Reshapes the price data for compatibility with XGBoost.
- Splits the data into training and testing sets using the train_test_split function.
- Initializes an XGBoost classifier and trains it on the training data.
- Evaluates the model's performance on the testing data using accuracy, precision, recall, F1 score, and ROC AUC score.
## Usage
To utilize this repository, follow these steps:

- Clone the repository: git clone https://github.com/yourusername/financial-analysis.git.
- Place your historical price data CSV file as BTC-USD.csv in the repository folder.
- Run preprocess.py to preprocess the data: python preprocess.py.
- Run main.py to build and evaluate the XGBoost model: python main.py.
