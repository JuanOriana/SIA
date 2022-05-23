import numpy as np
from sklearn.decomposition import PCA

from TP4.parse_csv import getInputsStandard

# https://stackoverflow.com/questions/39216897/plot-pca-loadings-and-loading-in-biplot-in-sklearn-like-rs-autoplot

data_standarized, countries, data, column_labels = getInputsStandard('./../../TP4/europe.csv')

print(column_labels)
print(countries)
# print(data_standarized)
print(np.array(data_standarized).T)

print('------------------')

pca = PCA(n_components=7)
aux = pca.fit_transform(np.array(data_standarized))

variance = pca.explained_variance_
print(variance)

print('------------------')

print(aux)
