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











