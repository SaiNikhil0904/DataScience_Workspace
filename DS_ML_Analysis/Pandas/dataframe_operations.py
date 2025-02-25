# dataframe_operations.py
# This script demonstrates operations on two Pandas DataFrames.

import pandas as pd

df1 = pd.DataFrame({'mark 1': [10, 40, 15, 40], 'mark 2': [15, 45, 30, 70]})
df2 = pd.DataFrame({'mark 1': [30, 20, 20, 50], 'mark 2': [20, 25, 30, 30]})

# -------------- A: Display DataFrames --------------
print("\nA - Original DataFrames:")
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# -------------- B: Add DataFrames --------------
print("\nB - Sum of DataFrames (df1 + df2):")
df_sum = df1 + df2
print(df_sum)

# -------------- C: Subtract df2 from df1 --------------
print("\nC - Difference of DataFrames (df1 - df2):")
df_diff = df1 - df2
print(df_diff)

# -------------- D: Rename column "mark 1" to "marks 1" --------------
print("\nD - Renaming 'mark 1' to 'marks 1' in both DataFrames:")
df1_renamed = df1.rename(columns={"mark 1": "marks 1"})
df2_renamed = df2.rename(columns={"mark 1": "marks 1"})
print("\nUpdated DataFrame 1:")
print(df1_renamed)
print("\nUpdated DataFrame 2:")
print(df2_renamed)

# -------------- E: Rename row indices in df1 --------------
print("\nE - Renaming row indices in df1:")
df1_renamed_index = df1.rename(index={0: 'zero', 1: 'one', 2: 'two', 3: 'three'})
print(df1_renamed_index)

# -------------- F: Modify a Specific Value --------------
print("\nF - Modifying a Specific Value:")
df1.at[2, 'mark 1'] = 99  # Changing the value at row index 2, column 'mark 1'
print(df1)

# -------------- G: Compute and Display Mean of Selected Columns --------------
print("\nG - Computing Mean of Selected Columns:")
mean_mark1 = df1['mark 1'].mean()
mean_mark2 = df1['mark 2'].mean()
print(f"Mean of 'mark 1': {mean_mark1:.2f}")
print(f"Mean of 'mark 2': {mean_mark2:.2f}")