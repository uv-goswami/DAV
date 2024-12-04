import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# a. Clean the data by dropping the column which has the largest number of missing values
column_with_most_nan = titanic_data.isnull().sum().idxmax()
titanic_data.drop(columns=[column_with_most_nan], inplace=True)
print(f"Dropped column: {column_with_most_nan}")

# b. Find total number of passengers with age more than 30
passengers_over_30 = titanic_data[titanic_data['Age'] > 30].shape[0]
print(f"Total number of passengers with age more than 30: {passengers_over_30}")

# c. Find total fare paid by passengers of second class
total_fare_second_class = titanic_data[titanic_data['Pclass'] == 2]['Fare'].sum()
print(f"Total fare paid by passengers of second class: {total_fare_second_class}")

# d. Compare number of survivors of each passenger class
survivors_per_class = titanic_data.groupby('Pclass')['Survived'].sum()
print("\nNumber of survivors of each passenger class:")
print(survivors_per_class)

# e. Compute descriptive statistics for age attribute gender-wise
age_statistics_gender = titanic_data.groupby('Sex')['Age'].describe()
print("\nDescriptive statistics for age attribute gender-wise:")
print(age_statistics_gender)

# f. Draw a scatter plot for passenger fare paid by Female and Male passengers separately
plt.figure(figsize=(10, 6))
sns.scatterplot(data=titanic_data, x='Fare', y='Age', hue='Sex', alpha=0.6)
plt.title('Passenger Fare vs Age by Gender')
plt.xlabel('Fare')
plt.ylabel('Age')
plt.legend(title='Gender')
plt.show()

# g. Compare density distribution for features age and passenger fare
plt.figure(figsize=(10, 6))
sns.kdeplot(data=titanic_data, x='Age', fill=True, label='Age', color='blue', alpha=0.5)
sns.kdeplot(data=titanic_data, x='Fare', fill=True, label='Fare', color='orange', alpha=0.5)
plt.title('Density Distribution of Age and Fare')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

# h. Draw the pie chart for three groups labelled as class 1, class 2, class 3 respectively
class_counts = titanic_data['Pclass'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(class_counts, labels=['Class 1', 'Class 2', 'Class 3'], autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Passenger Distribution by Class')
plt.show()

# Find % of survived passengers for each class
survival_rate_per_class = titanic_data.groupby('Pclass')['Survived'].mean() * 100
print("\n% of survived passengers for each class:")
print(survival_rate_per_class)

# Answer the question: Did class play a role in survival?
print("\nDid class play a role in survival?")
if survival_rate_per_class.max() > survival_rate_per_class.min():
    print("Yes, class played a role in survival.")
else:
    print("No, class did not play a role in survival.")
