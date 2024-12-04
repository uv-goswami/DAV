import pandas as pd

# Create the DataFrame
data = {
    'FamilyName': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'MonthlyIncome': [44000.00, 65000.00, 43150.00, 66500.00, 255000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]
}

df = pd.DataFrame(data)

# a. Calculate and display familywise gross monthly income
familywise_income = df.groupby('FamilyName')['MonthlyIncome'].sum()
print("Familywise Gross Monthly Income:")
print(familywise_income)

# b. Display the highest and lowest monthly income for each family name
highest_lowest_income = df.groupby('FamilyName')['MonthlyIncome'].agg(['max', 'min'])
print("\nHighest and Lowest Monthly Income for Each Family Name:")
print(highest_lowest_income)

# c. Calculate and display monthly income of all members earning income less than Rs. 80000.00
income_below_80000 = df[df['MonthlyIncome'] < 80000]
print("\nMonthly Income of Members Earning Less Than Rs. 80000.00:")
print(income_below_80000)

# d. Display total number of females along with their average monthly income
female_count = df[df['Gender'] == 'Female'].shape[0]
average_female_income = df[df['Gender'] == 'Female']['MonthlyIncome'].mean()
print(f"\nTotal Number of Females: {female_count}, Average Monthly Income: {average_female_income:.2f}")

# e. Delete rows with Monthly income less than the average income of all members
average_income = df['MonthlyIncome'].mean()
df_filtered = df[df['MonthlyIncome'] >= average_income]

print("\nDataFrame after deleting rows with Monthly Income less than the average income:")
print(df_filtered)
