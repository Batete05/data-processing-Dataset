# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# import pandas as pd

# # Read the dataset from CSV
# data_set = pd.read_csv('dataset1.csv')

# # Display original data for reference
# print("Original Dataset:")
# print(data_set)

# # Label encode the 'Purchased' column
# label_encoder = LabelEncoder()
# data_set['Purchased'] = label_encoder.fit_transform(data_set['Purchased'])

# # OneHot encode the 'Country' column
# column_transformer = ColumnTransformer(
#     transformers=[
#         ('onehot', OneHotEncoder(sparse_output=False), ['Country'])  # Encode 'Country'
#     ],
#     remainder='passthrough'  # Keep other columns unchanged
# )

# # Transform the dataset
# x = column_transformer.fit_transform(data_set)

# # Convert the transformed array back to a DataFrame for better readability
# encoded_data = pd.DataFrame(
#     x, 
#     columns=[
#         f"Country_{cat}" for cat in label_encoder.classes_
#     ] + list(data_set.columns[1:])  # Adjust column names as needed
# )

# print("Encoded Dataset:")
# print(encoded_data)
