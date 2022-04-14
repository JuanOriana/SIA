import numpy as np


def step_error(inputs: np.ndarray, expected_outputs: np.ndarray, w: np.ndarray):
    error = 0
    for i in range(inputs.shape[0]):
        h = np.dot(inputs[i], w)
        O = np.sign(h) * 2 - 1
        error += (expected_outputs[i] - O) ** 2
    return error / 2
