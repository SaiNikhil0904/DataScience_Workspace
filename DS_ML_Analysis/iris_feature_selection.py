"""
Feature Selection Analysis on Iris Dataset using Pearson Correlation

This script loads the Iris dataset and performs feature selection using Pearson correlation.
A heatmap is generated to visualize feature correlations, and highly correlated features
with the output variable are identified.

Libraries Used:
- pandas
- numpy
- seaborn
- matplotlib
- sklearn (datasets, feature selection)
"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

# Load the Iris dataset
dataset = datasets.load_iris()
X = dataset.data  
y = dataset.target 

# Creating a DataFrame
df = pd.DataFrame(X, columns=['sepal length', 'sepal width', 'petal length', 'petal width'])
df["Output"] = y 

# Display first few rows of the dataset
print(df.head())

# Pearson Correlation Heatmap
plt.figure(figsize=(12, 10))
correlation_matrix = df.corr() 
sns.heatmap(correlation_matrix, annot=True, cmap=plt.cm.Reds)
plt.title("Feature Correlation Heatmap")
plt.show()

# Correlation with the output variable
cor_target = abs(correlation_matrix["Output"]) 
relevant_features = cor_target[cor_target > 0.5] 

# Display relevant features
print("Highly correlated features with the target variable:")
print(relevant_features)

# Pairwise correlation between selected feature pairs
print("\nCorrelation between 'sepal length' and 'sepal width':")
print(df[["sepal length", "sepal width"]].corr())

print("\nCorrelation between 'petal length' and 'petal width':")
print(df[["petal length", "petal width"]].corr())