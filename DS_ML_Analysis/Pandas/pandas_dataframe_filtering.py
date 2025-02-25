# pandas_dataframe_filtering.py
# This script creates a Pandas DataFrame with actors and their work statistics.
# It then filters the DataFrame to display rows where the number of movies is greater than 460.

import numpy as np
import pandas as pd

# Defining NaN for missing values
NaN = np.nan

# Creating a DataFrame with actor names, movie counts, serials, and ad appearances
df = pd.DataFrame({
    'Name': ['Amitabh', 'Rekha', 'SHARUKH', 'SALMAN', 'PRIYANKA', 'HEMA'],
    'MOVIES': [500, 470, 450, 467, NaN, 340],
    'SERIAL': [45, 3, NaN, 2, 1, 1],
    'ADDS': [13, 10, 15, NaN, NaN, 13]
})

print("Original DataFrame:")
print(df)
print("\n")

# Filtering and displaying rows where 'MOVIES' is greater than 460
print("Movies greater than 460:")
print("\n")
print(df[df['MOVIES'] > 460])