from statistics import mean

import numpy as np

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


if __name__ == "__main__":
    data_standarized, countries, data, labels = parse_csv_opt("../europe.csv")
    mean_ = 0
    for i in range(len(data[0])):  # Dejo la matriz de datos con media 0
        aux = data_standarized[:, i]
        mean_aux = mean(aux)
        data_standarized[:, i] = (data_standarized[:, i] - mean_aux)

    solver = OjaSolver(0.01, data.shape[1], 50000)
    vec = solver.solve(data_standarized)
    pca = np.matmul(data_standarized, vec)

    print(pca)
