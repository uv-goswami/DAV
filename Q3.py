import pandas as pd
import numpy as np

# Create a DataFrame with 3 columns and 50 rows of random numeric data
np.random.seed(0)  # For reproducibility
data = np.random.rand(50, 3) * 100  # Random values between 0 and 100
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])

# Replace 10% of the values with null values
num_nulls = int(0.1 * df.size)  # 10% of total values
null_indices = np.random.choice(df.size, num_nulls, replace=False)
df.values.ravel()[null_indices] = np.nan

print("DataFrame with NaN values:\n", df)

# Task a: Identify and count missing values in a DataFrame
missing_values_count = df.isnull().sum()
print("\nMissing values in each column:\n", missing_values_count)

# Task b: Drop the column having more than 5 null values
df_dropped_column = df.dropna(axis=1, thresh=len(df) - 5)
print("\nDataFrame after dropping columns with more than 5 null values:\n", df_dropped_column)

# Task c: Identify the row label having the maximum sum of all values in a row and drop that row
row_sums = df_dropped_column.sum(axis=1)
max_row_index = row_sums.idxmax()
df_dropped_row = df_dropped_column.drop(index=max_row_index)
print("\nDataFrame after dropping the row with maximum sum:\n", df_dropped_row)

# Task d: Sort the DataFrame on the basis of the first column
df_sorted = df_dropped_row.sort_values(by='Column1')
print("\nSorted DataFrame based on Column1:\n", df_sorted)

# Task e: Remove all duplicates from the first column
df_no_duplicates = df_sorted.drop_duplicates(subset='Column1')
print("\nDataFrame after removing duplicates from Column1:\n", df_no_duplicates)

# Task f: Find the correlation between the first and second column
correlation = df_no_duplicates['Column1'].corr(df_no_duplicates['Column2'])
print("\nCorrelation between Column1 and Column2:", correlation)

# Find the covariance between the second and third column
covariance = df_no_duplicates['Column2'].cov(df_no_duplicates['Column3'])
print("Covariance between Column2 and Column3:", covariance)

# Task g: Discretize the second column and create 5 bins
df_no_duplicates['Column2_Binned'] = pd.cut(df_no_duplicates['Column2'], bins=5, labels=False)
print("\nDataFrame with discretized Column2 into 5 bins:\n", df_no_duplicates)
