# Content Monetization Modeler

# Introduction:
This project entails youtube ad revenue dataset in the form of csv and Preprocessing the dataset with the use of pandas , numpy for Handling missing values, remove duplicates, feature engineering.
To identify and handle the outliers  by using matplotlib and seaborn and identifying the correlation between the features.
Experimenting with 5 different regression models to predict ad_revenue_usd,  comparing their performance to identify the most effective model and using appropriate regression metrics to evaluate performance of the model.
 Furthermore, an interactive dashboard is developed with Streamlit incorporating the best model  to predict Ad revenue.


# Domain: Social Media Analytics 

# Skills Takeaway
Regression models
Predictive Modeling
Feature Engineering
Data Cleaning
Exploratory Data Analysis (EDA)
Regression Metrics (R², RMSE, MAE)
Data Visualization
Streamlit
Python
Pandas
Scikit-learn
Categorical Encoding
Outlier Detection
Missing Value Handling

# TECHNOLOGY USED
Python 
Streamlit


# Packages and Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import streamlit as st
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

# Understand the Dataset:
 Loading and inspecting the  youtube ad revenue dataset with the use of pandas and identifying missing values and duplicates values

# Preprocessing :
Handling missing values, removing duplicates and feature engineering with the use of pandas and numpy

# Exploratory Data Analysis: 
Identifying the trends, correlations, and outliers with the use of matplotlib , seaborn , poltly. Handling outliers with the use of  Winsorizing \IQR method and endcoding catogerical features using pandas onehot endcoding function ( pd.get_dummies())

# Model Building:
Experimenting with 5 different regression models to predict ad_revenue_usd and comparing their performance to identify the most effective model and pickling the model.

# Develope Streamlit:
Predict the ad_revenue_usd with our Streamlit app by providing the inputs . It's easy to use, with a user-friendly interface that lets you interact effortlessly with dynamic columns. 


# Analysis:
In this Analysis part, it shows seamless performance in Yearly,Quaterly and State wise of the data
