# This script demonstrates various Pandas operations such as:
# 1. Creating DataFrames
# 2. Handling missing values
# 3. Removing duplicates
# 4. Retrieving DataFrame properties

import pandas as pd  
import numpy as np  

# 1: Create a DataFrame and Print It
data = {'FDL Lab(40)': [34, 35, 28, 45], 'FDL theory(60)': [56, 45, 34, 29]}
df = pd.DataFrame(data)
print("1: Displaying the DataFrame\n")
print(df)

# 2: Assign Index Labels to the DataFrame
df = pd.DataFrame(data, index=['Student 1', 'Student 2', 'Student 3', 'Student 4'])
print("\n2: Displaying DataFrame with Index Labels\n")
print(df)

# 3: Find the Number of Rows and Columns
num_rows = len(df)
num_columns = len(df.columns)
print("\n3: DataFrame Properties")
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

# 4: Remove Duplicate Rows
data = {'FDL Lab(40)': [34, 35, 28, 45, 28, 45], 'FDL theory(60)': [56, 45, 34, 29, 34, 29]}
df = pd.DataFrame(data, index=['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 3', 'Student 4'])
print("\n4: DataFrame with Duplicates\n")
print(df)

df_no_duplicates = df.drop_duplicates()
print("\n4: DataFrame After Removing Duplicates\n")
print(df_no_duplicates)

# 5: Handling Missing Values
marks = pd.DataFrame({'FDL(40)': [34, '?', 28, 45], 
                      'FDL(60)': [56, 45, 34, '?']},
                     index=['Student 1', 'Student 2', 'Student 3', 'Student 4'])

print("\n5: DataFrame with Missing Values\n")
print(marks)

marks_cleaned = marks.replace('?', np.NaN)
print("\n5: DataFrame After Handling Missing Values\n")
print(marks_cleaned)