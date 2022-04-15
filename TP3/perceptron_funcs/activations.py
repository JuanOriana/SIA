import numpy as np

betha = 0.5


def step_activation(h: np.ndarray):
    return np.sign(h)


def linear_activation(h: np.ndarray):
    return h


def sigmoid_classic_activation(h: np.ndarray):
    return 1 / (1 + np.exp(-2 * betha * h))


def sigmoid_tanh_activation(h: np.ndarray):
    return np.tanh(betha * h)


def sigmoid_classic_activation_derivative(g: float):
    return 2 * betha * g * (1 - g)


def sigmoid_tanh_activation_derivative(g: float):
    return betha * (1 - fg * g)
