import pandas as pd

# Data for the two Excel files
data1 = {
    "Name": ["Alice", "Bob", "Alice", "Charlie", "Eve"],
    "Date": ["2024-12-01", "2024-12-01", "2024-12-02", "2024-12-01", "2024-12-01"],
    "Duration": [30, 40, 50, 30, 40],
}

data2 = {
    "Name": ["Alice", "David", "Charlie", "Eve", "Bob"],
    "Date": ["2024-12-01", "2024-12-01", "2024-12-02", "2024-12-02", "2024-12-02"],
    "Duration": [40, 30, 50, 40, 30],
}

# Creating DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Save to Excel files
file1_path = "Workshop_Attendance1.xlsx"
file2_path = "Workshop_Attendance2.xlsx"

# Writing to Excel
df1.to_excel(file1_path, index=False, sheet_name="Workshop1")
df2.to_excel(file2_path, index=False, sheet_name="Workshop2")

print(f"Excel files saved as {file1_path} and {file2_path}")
