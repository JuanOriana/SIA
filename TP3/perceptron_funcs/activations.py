import numpy as np


def step_activation(h: np.ndarray):
    return np.sign(h)


def linear_activation(h: np.ndarray):
    return h
