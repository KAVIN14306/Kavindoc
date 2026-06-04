#import required libraries
import pandas as pd
import numpy as np

#create sample data
data = {
    'Name': ['Kavin', 'Arun', 'Priya', 'Kavin', None],
    'Age': [21, 22, np.nan, 21, 20],
    'City': ['Chennai', 'Madurai', 'Coimbatore', 'Chennai', 'Salem'],
    'Salary': [25000, 30000, 28000, 25000, np.nan]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

#check missing values
print("\nMissing Values:")
print(df.isnull().sum())

#fill missing values automatically
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print(df)

#fill missing text values
df['Name'].fillna('Unknown', inplace=True)

#remove duplicate records
df.drop_duplicates(inplace=True)

print("\nAfter Removing Duplicates:")
print(df)

#standardize text forrmat
df['Name'] = df['Name'].str.upper()
df['City'] = df['City'].str.upper()

print(df)

#detect outliers
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df['Salary'] >= lower) &
        (df['Salary'] <= upper)]

#automate the entire process
def clean_data(df):

    # Fill missing numerical values
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Salary'].fillna(df['Salary'].mean(), inplace=True)

    # Fill missing text values
    df['Name'].fillna('Unknown', inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Standardize text
    df['Name'] = df['Name'].str.upper()
    df['City'] = df['City'].str.upper()

    return df

#run the automation
cleaned_df = clean_data(df)

print("\nCleaned Dataset:")
print(cleaned_df)