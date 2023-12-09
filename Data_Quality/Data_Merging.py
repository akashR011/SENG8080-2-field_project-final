import pandas as pd

# Data Collection
df1 = pd.read_csv('Datasets/Datasets_1/movies.csv')
df2 = pd.read_csv('Datasets/Datasets_1/tv-series.csv')

# Data Integration
merged_df = pd.merge(df1, df2, on=['id', 'title', 'vote_average', 'status', 'vote_count', 'homepage', 'spoken_languages', 'original_language', 'tagline', 'production_companies', 'production_countries', 'adult', 'backdrop_path', 'genres', 'popularity', 'poster_path', 'overview'], how='outer')


# Display the cleaned and integrated data
print(merged_df.head())

# Save the combined dataset to a new CSV file
merged_df.to_csv('Datasets/Combined_Dataset/tmdb_dataset.csv', index=False)
