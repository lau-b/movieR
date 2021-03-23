import pandas as pd
import pickle
from datetime import datetime
from sklearn.decomposition import NMF

print(datetime.now(), '## start reading csv')
user_matrix = pd.read_csv('../../data/processed/user_movie_matrix.csv', index_col=0)
print(datetime.now(), '## finished reading csv')
print(datetime.now(), '## start filling NaNs')
user_matrix.fillna(3.53, inplace=True)
print(datetime.now(), '## finished reading csv')
print(datetime.now(), '## start transposing matrix')
user_matrix = user_matrix.T
print(user_matrix)
print(datetime.now(), '## finished transposing')
print(datetime.now(), '## initiating model')
nmf = NMF(n_components=50, max_iter=2000)
nmf.fit(user_matrix)
print(datetime.now(), '## model fitted')

movie_list = list(user_matrix.columns)
print(movie_list[-1], len(movie_list))



print(datetime.now(), '## Saving model')
with open('../../data/nmf.pickle', 'wb') as file:
    pickle.dump(nmf, file)

print(datetime.now(), '## Model saved')
