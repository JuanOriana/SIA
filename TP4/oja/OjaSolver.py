from statistics import mean
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

from TP4.parse_csv_opt import parse_csv_opt


class OjaSolver:
    def __init__(self, learn_rate: float, data_dimension, max_epochs: int):
        self.learn_rate = learn_rate
        self.w = 2 * np.random.random(data_dimension) - 1
        self.max_epochs = max_epochs

    def valid_inputs(self, inputs: np.array):
        mean_aux = 0
        for i in range(len(inputs[0])):
            aux = inputs[:, i]
            mean_aux += mean(aux)
        return np.abs(mean_aux) < 0.000001

    def solve(self, inputs: np.array):
        if not self.valid_inputs(inputs):
            print("Mean must be 0 for inputs")
            return
        for epoch in range(self.max_epochs):
            for input in inputs:
                s = np.dot(self.w, input)
                self.w = self.w + self.learn_rate * s * (input - s * self.w)
        return self.w


def plot_pca(vec,labels,descr):
    print(vec)
    x = list(labels)
    y = list(vec)
    plt.rc('font',size=15)

    fig, ax = plt.subplots(figsize=(15, 10))
    width = 0.5  # the width of the bars
    ind = np.arange(len(y))  # the x locations for the groups

    cc = ['colors'] * len(y)
    for n, val in enumerate(y):
        if val < 0:
            cc[n] = 'orange'
        elif val >= 0:
            cc[n] = 'teal'

    ax.barh(ind, y, width, color=cc)

    ax.set_yticks(ind + width / 4)
    ax.set_yticklabels(x, minor=False)

    plt.title(descr)
    plt.xlabel('Cargas')
    plt.show()

if __name__ == "__main__":
    data_standarized, countries, data, labels = parse_csv_opt("../europe.csv")
    mean_ = 0
    for i in range(len(data[0])):  # Dejo la matriz de datos con media 0
        aux = data_standarized[:, i]
        mean_aux = mean(aux)
        data_standarized[:, i] = (data_standarized[:, i] - mean_aux)

    solver = OjaSolver(0.01, data.shape[1], 500)
    vec = solver.solve(data_standarized)
    plot_pca(vec,labels,"Primer componente obtenida con Oja")

    print('-COUNTRIEs-')

    pca = np.matmul(data_standarized, vec)
    print(countries)
    print('-OUR-')

    print(pca)
    print('-TEIR-')


    pca = PCA()
    components = pca.fit_transform(data_standarized)
    plot_pca(pca.components_[0],labels,"Primer componente obtenida con libreria")
    print(components[:, 0:2][:, 0])
    error = 0
    for i in range(len(vec)):
        error = np.abs(vec[i]-components[0][i])
    print(error)

