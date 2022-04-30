import numpy as np

from TP3.data_structs.Layer import Layer, NeuralNetwork
from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, sigmoid_tanh_activation, \
    sigmoid_tanh_activation_derivative
from TP3.perceptron_funcs.errors import scaling_identity
from TP3.utils.mutation import mutate_set
from TP3.utils.parser import parse_nums, nums_out_parity, nums_out_arr
from TP3.utils.splitter import k_splitting


def main():
    numbers = parse_nums("../assets/numbers.txt",7)
    numbers_o = nums_out_arr()

    layer1 = Layer(16, 35)
    layer2 = Layer(10, 16)
    layer3 = Layer(10, 10)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork([layer1, layer2,layer3], sigmoid_tanh_activation, sigmoid_tanh_activation_derivative, 0.1)
    neural_network.train(numbers,numbers_o,1000)

    mutate_set(numbers,0.1)
    print("Achieved error in numbers: ", neural_network.eval_error(numbers,numbers_o))
    print("Achived accuracy in numbers: ", neural_network.accuracy_by_node(numbers,numbers_o))



if __name__ == "__main__":
    main()