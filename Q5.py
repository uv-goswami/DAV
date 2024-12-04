import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
import scipy.stats as stats

# Load the Iris dataset
iris_data = load_iris()
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['species'] = iris_data.target_names[iris_data.target]

# a. Display info on datatypes in the dataset
print("Iris Dataset Info:")
print(df.info())

# b. Find the number of missing values in each column
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# c. Plot bar chart to show the frequency of each class label in the data
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='species', palette='viridis')
plt.title('Frequency of Each Class Label in the Iris Dataset')
plt.xlabel('Species')
plt.ylabel('Frequency')
plt.legend(title='Species')
plt.show()

# d. Draw a scatter plot for Petal Length vs Sepal Length and fit a regression line
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x='sepal length (cm)', y='petal length (cm)', marker='o', color='blue')
plt.title('Petal Length vs Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# e. Plot density distribution for feature Petal width
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='petal width (cm)', hue='species', fill=True, common_norm=False, palette='crest')
plt.title('Density Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Density')
plt.legend(title='Species')
plt.show()

# f. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset
sns.pairplot(df, hue='species', palette='bright')
plt.suptitle('Pairwise Bivariate Distribution in the Iris Dataset', y=1.02)
plt.show()

# g. Draw heatmap for any two numeric attributes
plt.figure(figsize=(8, 5))
sns.heatmap(df[['sepal length (cm)', 'sepal width (cm)']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Sepal Length and Sepal Width Correlation')
plt.show()

# h. Compute mean, mode, median, standard deviation, confidence interval and standard error for each numeric feature
statistics = {}
for column in df.columns[:-1]:  # Exclude species column
    statistics[column] = {
        'Mean': df[column].mean(),
        'Median': df[column].median(),
        'Mode': df[column].mode()[0],
        'Standard Deviation': df[column].std(),
        'Standard Error': stats.sem(df[column]),
        'Confidence Interval (95%)': stats.t.interval(0.95, len(df[column])-1, loc=df[column].mean(), scale=stats.sem(df[column]))
    }

statistics_df = pd.DataFrame(statistics).T
print("\nStatistics for Numeric Features:")
print(statistics_df)

# i. Compute correlation coefficients between each pair of features and plot heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Coefficients Heatmap')
plt.show()
