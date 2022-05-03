import sys

import numpy as np

from TP3.data_structs.Layer import Layer, NeuralNetwork
from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, sigmoid_tanh_activation, \
    sigmoid_tanh_activation_derivative
from TP3.perceptron_funcs.errors import scaling_identity
from TP3.utils.parameters import Parameters


def main():

    if len(sys.argv) != 2:
        print("Invalid usage: ex3.py <config.json>")
        quit(1)
    params = Parameters(sys.argv[1])

    inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_outputs_o = np.array([1, 1, -1, -1])

    layer1 = Layer(4, 2)
    layer2 = Layer(1, 4)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork([layer1, layer2], sigmoid_tanh_activation, sigmoid_tanh_activation_derivative, params.learning_rate)
    neural_network.train(inputs,expected_outputs_o,params.iters)
    print("Achieved error in XOR: ", neural_network.eval_error(inputs,expected_outputs_o))
    print("Achived accuracy in XOR: ", neural_network.accuracy(inputs,expected_outputs_o,[-1,1]))



if __name__ == "__main__":
    main()