import pandas as pd

# Data Collection
df1 = pd.read_csv('Datasets/Datasets_1/movies.csv')
df2 = pd.read_csv('Datasets/Datasets_2/tv-series.csv')

print("Printing Dataset 1")
print()
print(df1.head())
print()

print("Printing Dataset 2")
print()
print(df1.head())
print()

# Data Integration
merged_df = pd.merge(df1, df2, on=['id', 'title', 'vote_average', 'status', 'vote_count', 'homepage', 'spoken_languages', 'original_language', 'tagline', 'production_companies', 'production_countries', 'adult', 'backdrop_path', 'genres', 'popularity', 'poster_path', 'overview'], how='outer')

# Data Storage and Maintenance
# Assuming you want to store the merged data as a new CSV file
merged_df.to_csv('Merged_Dataset.csv', index=False)

print("Printing Merged Dataset:")
print()
print(merged_df.head())
print()

# Combine all columns with '_x' and '_y' suffixes into a single column
for column in merged_df.columns:
    if column.endswith('_x'):
        base_column = column[:-2]
        merged_df[base_column] = merged_df[column].combine_first(merged_df[f'{base_column}_2'])

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

# Display the cleaned and integrated data
print("Printing Dataset after performing Data Quality checks and Data Cleaning")
print()
print(merged_df.head())

# Save the combined dataset to a new CSV file
merged_df.to_csv('Datasets/Combined_Dataset/tmdb_dataset.csv', index=False)
