import pandas as pd

data_set1 = pd.read_csv('dataset1.csv')
data_set2 = pd.read_csv('dataset.csv')

# this is to merge the dataset
result = pd.merge(data_set1, data_set2,on='Email', how='inner')
print(result)
