import pandas as pd
import numpy as np

df1 = pd.read_excel("Workshop_Attendance1.xlsx")
df2 = pd.read_excel("Workshop_Attendance2.xlsx")



# Task a: Merge the two data frames to find names of students who attended both workshops
common_attendees = pd.merge(df1, df2, on="Name", how="inner")["Name"].unique()

# Task b: Find names of all students who attended a single workshop only
all_names = set(df1["Name"]).union(df2["Name"])
single_workshop_names = all_names - set(common_attendees)

# Task c: Merge two data frames row-wise and find the total number of records
merged_rowwise = pd.concat([df1, df2], axis=0, ignore_index=True)
total_records = len(merged_rowwise)

# Task d: Merge two data frames row-wise and use 'Name' and 'Date' as multi-row indexes
hierarchical_df = merged_rowwise.set_index(["Name", "Date"])
descriptive_stats = hierarchical_df.describe()

# Display results
results = {
    "Task a": {
        "Common Attendees": list(common_attendees),
    },
    "Task b": {
        "Single Workshop Attendees": list(single_workshop_names),
    },
    "Task c": {
        "Total Records in Merged DataFrame": total_records,
    },
    "Task d": {
        "Hierarchical DataFrame Descriptive Statistics": descriptive_stats,
    },
}

for task, output in results.items():
    print(f"{task}:\n{output}\n")
