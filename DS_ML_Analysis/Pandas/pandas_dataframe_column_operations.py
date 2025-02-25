# pandas_dataframe_column_operations.py
# This script performs multiple operations on a Pandas DataFrame:
# A. Adds a new column 'Economics' to the DataFrame.
# B. Modifies values in the 'Economics' column.
# C. Adds a new row to the DataFrame.
# D. Converts data types of selected columns.
# E. Drops a specific column and row.

import pandas as pd

# Creating a DataFrame with subject marks
dict_data = {'English': [85, 73, 98], 'Math': [60, 80, 58], 
             'Science': [90, 60, 74], 'French': [95, 87, 92]}
df = pd.DataFrame(dict_data, index=['2018', '2019', '2020'])

# Adding a new column 'Economics'
Economics = [99, 99, 99]
df['Economics'] = Economics
print("A - DataFrame after adding 'Economics' column:")
print(df)
print('\n')

# Modifying values in the 'Economics' column
print('B - Modify a DOUBLE value:')
df.loc['2019', 'Economics'] = 54
df.loc['2020', 'Economics'] = 45
print(df)
print('\n')

# Adding a new row and converting data types
print("C - Adding a new row and converting column types:")
new_row = [89, 21, 87, 59, 43]
df.loc[2022] = new_row

# Converting data types to float
df['English'] = pd.to_numeric(df['English'], downcast='float')
df['Math'] = pd.to_numeric(df['Math'], downcast='float')
df['Science'] = pd.to_numeric(df['Science'], downcast='float')
df['French'] = pd.to_numeric(df['French'], downcast='float')

print(df)
print('\n')

# Dropping the last column and a specific row
print("E - Dropping the 'Economics' column and row '2018':")
df = df.drop(columns=['Economics'])  # Dropping the 'Economics' column
df = df.drop(index='2018')  # Dropping the '2018' row
print(df)