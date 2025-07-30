

03/21/2025 (mdl)

Akime-O_odham-diabetes.data.csv
This file is DIFFERENT from the one in lab. Please use this data file for your data cleaning.

NOTE:  this data file has column headers included!  (leave headers in file, alter code to handle)

This analysis uses the diabetes dataset collected from the
[Akimel O'odham or River People community](https://en.wikipedia.org/wiki/Akimel_O%27odham "River People") in Arizona.  
This .csv file is a canonical data set used in introductory machine learning examples and is  typically named using 
the colonization label "Pima", `pima-peoples-diabetes.data.csv`. We will use Akimel O'odham.

WorkflowDataPrepSpec.pdf
The program specification ("spec").

README.txt

README.txt

Project Title: Diabetes Data Cleaning and Analysis

# Project Overview
This project involves performing data cleaning and analysis on the Akime-O'odham Diabetes Dataset. The dataset contains various medical features related to diabetes diagnosis, collected from the Akimel O'odham (River People) community in Arizona. Data cleaning techniques are applied to ensure data quality, followed by building a logistic regression model to predict diabetes.

# Files Included
- Akime-O_odham-diabetes.data.csv: The original dataset used for this analysis. Note that this file includes column headers.
- LOGfile.csv: A log file documenting the steps performed during data cleaning.
- cleaned_data.cs*: The final cleaned version of the dataset after applying various data preprocessing techniques.
- WorkflowDataPrepSpec.pdf: The program specification detailing data cleaning requirements and objectives.
- WorkFlowDataPrep.ipynb: Jupyter notebook containing code for data cleaning, analysis, and modeling.
- README.txt: This document explaining the project structure and contents.

# Objective
The main objective is to clean and preprocess the data to handle missing values, detect outliers, and ensure data consistency. A logistic regression model is then built to predict whether a patient is likely to have diabetes based on their medical features.

# Data Cleaning Techniques Applied
1. Handling Missing Values: Instead of removing columns with missing values, imputation techniques such as mean, median, and mode were applied based on the data distribution.
2. Outlier Detection and Treatment: Outliers were identified using boxplots and statistical measures. Rather than removing outliers, log transformations and other scaling methods were applied.
3. Feature Engineering: New features were created based on the existing data to enhance model performance. For example, a logarithmic transformation was applied to columns with skewed distributions.
4. Feature Selection: Highly correlated or redundant features were identified using a correlation matrix and removed to prevent multicollinearity.
5. Standardization: Features were scaled using StandardScaler to ensure that all features contributed equally to the logistic regression model.

# Visualizations
- Data Distribution: Histograms and box plots were created to compare data before and after cleaning, showcasing the impact of transformations and outlier management.
- Correlation Matrix: Heatmaps were used to visualize correlations between features, both before and after data cleaning.
- Confusion Matrix: Visual representation of the model's classification results using the confusion matrix.
- ROC Curve: An ROC curve was plotted to evaluate the model's performance and its ability to distinguish between classes.

# Model Evaluation
A logistic regression model was trained on the cleaned data, achieving a balanced accuracy score. The confusion matrix and ROC curve provided insights into the model's performance, indicating effective classification.

# Citation
The code and visualizations for this project were generated with the assistance of ChatGPT by OpenAI. If referencing the code or visual outputs, please use the following citation:
> "Generated using ChatGPT by OpenAI for data cleaning, visualization, and model evaluation in a machine learning project." 

# Additional Notes
- Ensure that cleaned_data.csv is present in the working directory before running the code.
- Python libraries required: pandas, numpy, matplotlib, seaborn, sklearn.
- The results may vary slightly depending on random seed values used during train-test splitting.
