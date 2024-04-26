## Jobs in Data Salary Estimator: Project Overview

- Aim to Create a tool that estimates salaries from different data fields to help people negotiate their income when they get a job.
- Engineered features from the dataset to identify which companies tend to pay which job role more.
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
- Built a client facing API using flask

## Resources and code used
The data set is scrapped from Ambition box website which contains information about different jobs and companies,their experiences and salaries

https://www.kaggle.com/datasets/madhurpant/data-science-jobs-in-india

https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

Python Version: 3.7

Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle

## Data Cleaning

I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

- Parsed numeric data out of salary
- Checked for any duplicates in the dataset

## EDA

I looked at the distributions of the data and the value counts for the various categorical variables also found out outliers

<img width="368" alt="Screenshot 2024-04-27 at 12 11 57 AM" src="https://github.com/SanjilMahajani/Salary_predictor/assets/43502576/228d61c3-6d3c-4556-8de5-3bcf5727acba">

<img width="316" alt="Screenshot 2024-04-27 at 12 12 32 AM" src="https://github.com/SanjilMahajani/Salary_predictor/assets/43502576/07bde4fb-9d4d-42ec-a848-5e3d5f3168f2">

<img width="389" alt="Screenshot 2024-04-27 at 12 13 10 AM" src="https://github.com/SanjilMahajani/Salary_predictor/assets/43502576/0c1a6fcf-100b-481d-b064-00700430ec95">

## Model Building

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried four different models:

- Multiple Linear Regression – Baseline for the model
- Lasso and Ridge Regression – Because of the sparse data from the many categorical variables.
- Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

## Model performance

The Random Forest model far outperformed the other approaches with a R2 score of 0.999.

## Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. This is how the page looks











