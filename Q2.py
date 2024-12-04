import pandas as pd

# Task a
# Create a series with 5 elements
series_a = pd.Series([10, 5, 20, 15, 1], index=['a', 'b', 'c', 'd', 'e'])

# Display the series sorted by index
sorted_by_index = series_a.sort_index()

# Display the series sorted by values
sorted_by_values = series_a.sort_values()

# Task b
# Create a series with N elements and duplicate values
series_b = pd.Series([50, 10, 20, 50, 10, 30, 50])

# Rank the values using 'first' method
ranks_first = series_b.rank(method='first')

# Rank the values using 'max' method
ranks_max = series_b.rank(method='max')

# Minimum and maximum ranks
min_rank_first = ranks_first.min()
max_rank_first = ranks_first.max()

# Task c
# Index of the minimum and maximum elements of a Series
min_index = series_a.idxmin()
max_index = series_a.idxmax()

# Display results
print("Task a:")
print("Original Series:")
print(series_a)
print("\nSorted by Index:")
print(sorted_by_index)
print("\nSorted by Values:")
print(sorted_by_values)

print("\nTask b:")
print("Original Series:")
print(series_b)
print("\nRanks using 'first' method:")
print(ranks_first)
print("\nRanks using 'max' method:")
print(ranks_max)
print(f"\nMinimum Rank (first method): {min_rank_first}")
print(f"Maximum Rank (first method): {max_rank_first}")

print("\nTask c:")
print(f"Index of Minimum Value: {min_index}")
print(f"Index of Maximum Value: {max_index}")
