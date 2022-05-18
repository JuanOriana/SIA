import numpy as np


class HopfieldSolver:

    def solve(self, query: np.ndarray, inputs: np.ndarray):
        # Estimating weights
        count, dimension = inputs.shape
        K = np.zeros((count, dimension))
        for i in range(len(inputs)):
            K[i, :] = inputs[i]
        weights = (1 / dimension) * (np.matmul(K.T, K))
        np.fill_diagonal(weights, 0)

        t = 0
        S = query
        old_S = None

        while not np.array_equal(S, old_S):
            old_S = S
            S = np.sign(np.dot(weights, S))
            t += 1

        return S, t


if __name__ == "__main__":
    solver = HopfieldSolver()
    inputs = np.array([[1, 1, -1, -1], [-1, -1, 1, 1]])
    solver.solve(np.array([1, -1, -1, -1]), inputs)
