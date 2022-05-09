import sys

import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import linear_activation,sigmoid_tanh_activation,sigmoid_tanh_activation_derivative
from TP3.perceptron_funcs.errors import scaling_identity, scaling_tanh
from TP3.utils.parameters import Parameters
from TP3.utils.parser import parse


def main():

    if len(sys.argv) != 2:
        print("Invalid usage: ex2.py <config.json>")
        quit(1)
    params = Parameters(sys.argv[1])
    inputs, _, _ = parse("../assets/train_set.txt")
    normalization = "TANH" if params.activation == sigmoid_tanh_activation else "LINEAL"
    expected, max_value, min_value = parse("../assets/expected.txt",normalize=normalization)

    if params.activation == sigmoid_tanh_activation:
        activation = sigmoid_tanh_activation
        derivative = sigmoid_tanh_activation_derivative
        scaling = scaling_tanh
    elif params.activation == linear_activation:
        activation = linear_activation
        derivative = None
        scaling = scaling_identity
    else:
        print("Activation has to be sigmoid_tanh or lineal")
        exit(1)
    perceptron = SimplePerceptron(inputs[0].size,activation ,params.learning_rate,derivative=derivative)
    perceptron.train(inputs,expected,params.iters,perceptron.secuencially_learn,scaling,max_value=max_value,min_value=min_value)
    print("Achieved error using activation " + sigmoid_tanh_activation.__name__ + " :", perceptron.error)



if __name__ == "__main__":
    main()