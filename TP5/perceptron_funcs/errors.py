import numpy as np

from TP3.perceptron_funcs.activations import step_activation, linear_activation


def scaling_identity(value, max_value, min_value):
    return value


def activation_based_error(inputs: np.ndarray, expected_outputs: np.ndarray, w: np.ndarray, activation,
                           scaling_function=scaling_identity,max_value=0, min_value=0):
    error = 0
    for i in range(inputs.shape[0]):
        h = np.dot(inputs[i], w)
        estimation = activation(h)
        # error += (expected_outputs[i] - estimation) * (expected_outputs[i] - estimation)
        error += (scaling_function(expected_outputs[i],max_value, min_value) - scaling_function(estimation,max_value, min_value)) ** 2
    return error / inputs.shape[0]


def scaling_tanh(value, max_value, min_value):
    return (1 + value / 2) * (max_value - min_value) + min_value
