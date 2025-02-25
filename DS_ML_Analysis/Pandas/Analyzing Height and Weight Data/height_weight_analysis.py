# height_weight_analysis.py
# This script reads an Excel file containing height and weight data.
# It filters data based on gender and country, computes average values, 
# and extracts min/max weight statistics.

import pandas as pd

# Load the dataset
file_path = "Height-and-Weight.xlsx"
df = pd.read_excel(file_path)

print("Original DataFrame:")
print(df.head())

# -------------- A: Select only women --------------
print("\nA - Filtering only women:")
df_women = df[df['Gender'] == 'W']
print(df_women)

# -------------- B: Compute average height and weight of women --------------
print("\nB - Average height and weight of women:")
average_height = df_women['Height(cm)'].mean()
average_weight = df_women['Weight(kg)'].mean()
print(f"Average Height (cm) of Women: {average_height:.2f}")
print(f"Average Weight (kg) of Women: {average_weight:.2f}")

# -------------- C: Find min and max weight among women --------------
print("\nC - Min and Max Weight of Women:")
max_weight = df_women['Weight(kg)'].max()
min_weight = df_women['Weight(kg)'].min()
print(f"Max Weight (kg) of Women: {max_weight}")
print(f"Min Weight (kg) of Women: {min_weight}")

# -------------- D: Filter women from Algeria and compute mean height --------------
print("\nD - Women from Algeria and their mean height:")
df_women_algeria = df_women[df_women['Country/Team'] == 'Algeria']
print(df_women_algeria)
mean_height_algeria = df_women_algeria['Height(cm)'].mean()
print(f"Mean Height (cm) of Women from Algeria: {mean_height_algeria:.2f}")