

import numpy as np
from TP4.kohonen.test_scripts import *
from TP4.parse_csv import getInputsStandard
from TP4.parse_csv_opt import parse_csv_opt


class KohonenSolver:

    def __init__(self, k: int, learn_rate: float, radius: float, decrese_rate=1):
        self.k = k
        self.learn_rate = learn_rate
        self.radius = radius
        self.epochs = 0
        self.weights = None
        self.setup_state = False
        self.decrease_rate = decrese_rate

    def setup(self, data: np.ndarray):
        self.weights = np.zeros((self.k, self.k, len(data[0])))
        for i in range(self.k):
            for j in range(self.k):
                random_idx = np.random.choice(np.arange(len(data)))
                self.weights[i, j, :] = data[random_idx]
        self.setup_state = True

    def find_closest(self, choice, data):
        flattened = self.weights.reshape(self.k ** 2, len(data[0]))
        mean_dist = np.square(flattened - choice).sum(axis=1)
        return np.unravel_index(np.argmin(mean_dist), (self.k, self.k))

    def is_coord_valid(self, i, j):
        return 0 <= i < self.k and 0 <= j < self.k

    def get_neighbours(self, indices):
        base_i, base_j = indices
        neighbours = []
        for i in range(int(base_i - self.radius), int(base_i + self.radius + 1)):
            for j in range(int(base_j - self.radius), int(base_j + self.radius + 1)):
                if (i - base_i) ** 2 + (j - base_j) ** 2 <= self.radius ** 2 and self.is_coord_valid(i, j):
                    neighbours.append((i, j))

        return neighbours

    def update_weights(self, indices, choice):
        neighbours = self.get_neighbours(indices)
        for (i, j) in neighbours:
            self.weights[i, j] += self.learn_rate * (choice - self.weights[i, j])
        self.learn_rate /= self.decrease_rate

    def solve(self, data: np.ndarray, epochs: int):
        while self.epochs < epochs:
            random_idx = np.random.choice(np.arange(len(data)))
            choice = data[random_idx]
            i, j = self.find_closest(choice, data)
            self.update_weights((i, j), choice)
            self.epochs += 1





if __name__ == "__main__":
    k = 3
    area,gdp,inflation,life_expected,military,pop_growth,unemployment = range(0,7)
    solver = KohonenSolver(k, 0.2, 1.5, 2)
    # data_standarized,data,countries,_ = parse_csv_opt("../europe.csv")
    data_standarized,countries,data,_ = getInputsStandard("../europe.csv")
    inputs = np.array(data_standarized)
    solver.setup(inputs)
    solver.solve(np.array(inputs), 1000 * 28)
    plot_boxplot(data,"Box plot not standarized")
    plot_boxplot(data_standarized,"Box plot standarized")
    plot_heatmap(inputs,countries,solver,k)
    plot_single_variable(unemployment,k,data_standarized,solver)
    plot_single_variable(inflation,k,data_standarized,solver)




