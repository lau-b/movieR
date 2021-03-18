import os
from pathlib import Path
import pandas as pd


def get_project_root():
    return Path(__file__).parent.parent.parent.parent

processed_dir = f'{get_project_root()}/data/processed/'
raw_dir = f'{get_project_root()}/data/raw/'


## creates a user_movie_matrix based on the ratings
df_ratings = pd.read_csv(f'{raw_dir}/ratings.csv')
df_ratings = df_ratings.drop(['timestamp'], axis=1)
user_movie_matrix = df_ratings.pivot(
    index='movieId',
    columns='userId',
    values='rating'
)
user_movie_matrix.to_csv(f'{processed_dir}/user_movie_matrix.csv')

df_movies = pd.read_csv(f'{raw_dir}/movies.csv', index_col=0)
df_movies = df_movies.drop(['genres'], axis=1)

movies_ranked_average = user_movie_matrix.mean(axis=1).sort_values()
rating_filter = user_movie_matrix.T.count() > 10  # more for lager datasets
movies_for_dummy_rec = movies_ranked_average.loc[rating_filter]
movies_for_dummy_rec.to_csv(f'{processed_dir}/rec_list.csv')



test_rec = movies_for_dummy_rec[-3:].index
print(df_movies.loc[test_rec])  # Malte fragen



print('im done')

