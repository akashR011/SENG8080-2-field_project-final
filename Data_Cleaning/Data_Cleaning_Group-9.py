import pandas as pd

# Data Collection
df = pd.read_csv('Combined Dataset/tmdb_dataset.csv')

# Data Quality Checks and Data Cleaning
# Assuming you want to drop duplicates
merged_df = merged_df.drop_duplicates()

# Handling Missing Values
# Example: Impute missing values for numeric columns with mean, for categorical columns with mode
numeric_columns = merged_df.select_dtypes(include='number').columns
categorical_columns = merged_df.select_dtypes(exclude='number').columns

merged_df[numeric_columns] = merged_df[numeric_columns].fillna(merged_df[numeric_columns].mean())
merged_df[categorical_columns] = merged_df[categorical_columns].fillna(merged_df[categorical_columns].mode().iloc[0])

# Drop the original release_date column
columns_to_drop = ['number_of_seasons', 'release_date', 'number_of_episodes', 'original_title', 'budget', 'revenue', 'runtime', 'first_air_date', 'last_air_date', 'in_production', 'original_name', 'type', 'created_by', 'languages', 'networks', 'origin_country', 'episode_run_time', 'imdb_id']
merged_df = merged_df.drop(columns=columns_to_drop, axis=1)

# Find and print columns with missing values
columns_with_missing_values = merged_df.columns[merged_df.isnull().any()]

# Checking for columns with missing values
for column in columns_with_missing_values:
    print(f"{column}: {merged_df[column].isnull().sum()} missing values")

