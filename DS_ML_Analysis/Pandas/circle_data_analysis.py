# circle_data_analysis.py
# This script creates a DataFrame for circle data, calculates statistics,
# and performs operations like deleting rows and columns.

import pandas as pd

# Creating the DataFrame
circle_data = {
    'radius (in cm)': [1.0, 1.5, 2.5, 4.0, 6.0],
    'color': ['red', 'blue', 'orange', 'green', 'red']
}
df = pd.DataFrame(circle_data, index=['Circle 1', 'Circle 2', 'Circle 3', 'Circle 4', 'Circle 5'])

# -------------- A: Display DataFrame --------------
print("\nA - Original Circle DataFrame:")
print(df)

# -------------- B: Calculate average radius --------------
print("\nB - Average radius of circles:")
average_radius = df['radius (in cm)'].mean()
print(f"Average Radius (cm): {average_radius:.2f}")

# -------------- C: Find the most frequently occurring color --------------
print("\nC - Most frequently occurring color:")
most_frequent_color = df['color'].mode()[0]  # Extract the first mode value
print(f"Most Frequent Color: {most_frequent_color}")

# -------------- D: Add 'area (in cm²)' column --------------
df['area (in cm²)'] = df['radius (in cm)']**2 * 3.14
print("\nD - DataFrame after adding 'area (in cm²)':")
print(df)

# -------------- E: Remove 'area (in cm²)' column --------------
df = df.drop(columns=['area (in cm²)'])
print("\nE - DataFrame after removing 'area (in cm²)':")
print(df)

# -------------- F: Delete the row with the largest area --------------
df['area (in cm²)'] = df['radius (in cm)']**2 * 3.14  # Recalculate area
row_with_max_area = df['area (in cm²)'].idxmax()  # Get index of max area row
df = df.drop(index=row_with_max_area)  # Drop the row
print("\nF - DataFrame after removing the circle with the largest area:")
print(df)