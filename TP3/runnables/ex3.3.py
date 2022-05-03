import sys

import numpy as np

from TP3.data_structs.Layer import Layer, NeuralNetwork
from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, sigmoid_tanh_activation, \
    sigmoid_tanh_activation_derivative
from TP3.perceptron_funcs.errors import scaling_identity
from TP3.utils.mutation import mutate_set
from TP3.utils.parameters import Parameters
from TP3.utils.parser import parse_nums, nums_out_parity, nums_out_arr
from TP3.utils.splitter import k_splitting


def main():

    if len(sys.argv) != 2:
        print("Invalid usage: ex1.py <config.json>")
        quit(1)
    params = Parameters(sys.argv[1])

    numbers = parse_nums("../assets/numbers.txt",7)
    numbers_o = nums_out_arr()

    layer1 = Layer(16, 35)
    layer2 = Layer(10, 16)
    layer3 = Layer(10, 10)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork([layer1, layer2,layer3], sigmoid_tanh_activation, sigmoid_tanh_activation_derivative, params.learning_rate)
    neural_network.train(numbers,numbers_o,params.iters)

    mutate_set(numbers,0.2)
    print("Achieved error in numbers: ", neural_network.eval_error(numbers,numbers_o))
    print("Achieved accuracy in numbers: ", neural_network.accuracy_by_node(numbers,numbers_o))



if __name__ == "__main__":
    main()