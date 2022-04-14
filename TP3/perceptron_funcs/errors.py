import numpy as np

from TP3.perceptron_funcs.activations import step_activation, linear_activation


def activation_based_error(inputs: np.ndarray, expected_outputs: np.ndarray, w: np.ndarray, activation):
    error = 0
    for i in range(inputs.shape[0]):
        h = np.dot(inputs[i], w)
        O = activation(h)
        error += (expected_outputs[i] - O) ** 2
    return error / 2


def step_error(inputs: np.ndarray, expected_outputs: np.ndarray, w: np.ndarray):
    return activation_based_error(inputs, expected_outputs, w, step_activation)


def linear_error(inputs: np.ndarray, expected_outputs: np.ndarray, w: np.ndarray):
    return activation_based_error(inputs, expected_outputs, w, linear_activation)
