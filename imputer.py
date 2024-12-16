from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

# Read the dataset from CSV
data_set = pd.read_csv('dataset1.csv')

# Display original data for reference
# print("Original Dataset:")
# print(data_set)

# Handle missing data in the 'Age' and 'Salary' columns
# Selecting these columns for imputation
columns_to_impute = ['Age', 'Salary']

# Replace 'np.nan' with actual NumPy NaN values in the dataset
data_set.replace('NAN', np.nan, inplace=True)

# Create SimpleImputer object with mean strategy
imputer = SimpleImputer(missing_values=np.nan, strategy='mode')

# Fit the imputer to the selected columns
data_set[columns_to_impute] = imputer.fit_transform(data_set[columns_to_impute])

# Display the imputed data
print("\nDataset after Imputation:")
print(data_set)
