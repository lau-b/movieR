import pandas as pd
import numpy as np
from sklearn.decomposition import NMF


# make sure to run this file from project root!
user_matrix = pd.read_csv('data/processed/user_movie_matrix.csv')
user_matrix.fillna(user_matrix.mean(), inplace=True)  # ist mean besser als 2.0?


nmf = NMF(n_components=3, max_iter=300)
nmf.fit(user_matrix)

Q = nmf.n_components_
print('\n\n\n',Q)
