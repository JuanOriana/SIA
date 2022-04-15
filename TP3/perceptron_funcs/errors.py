import numpy as np

from TP3.perceptron_funcs.activations import step_activation, linear_activation


def activation_based_error(inputs: np.ndarray, expected_outputs: np.ndarray, w: np.ndarray, activation):
    error = 0
    for i in range(inputs.shape[0]):
        h = np.dot(inputs[i], w)
        estimation = activation(h)
        error += (expected_outputs[i] - estimation)*(expected_outputs[i] - estimation)
    return error / 2

