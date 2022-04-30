import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import linear_activation,sigmoid_tanh_activation,sigmoid_tanh_activation_derivative
from TP3.perceptron_funcs.errors import scaling_identity, scaling_tanh
from TP3.utils.parser import parse


def main():
    method = "TANH"
    inputs, _, _ = parse("../assets/train_set.txt")
    expected, max_value, min_value = parse("../assets/expected.txt",normalize=method)

    if method == "TANH":
        activation = sigmoid_tanh_activation
        derivative = sigmoid_tanh_activation_derivative
        scaling = scaling_tanh
    else:
        activation = linear_activation
        derivative = None
        scaling = scaling_identity
    perceptron = SimplePerceptron(inputs[0].size,activation ,0.05,derivative=derivative)
    perceptron.train(inputs,expected,200*10,perceptron.secuencially_learn,scaling,max_value=max_value,min_value=min_value)
    print("Achieved error using activation " + method+ " :", perceptron.error)



if __name__ == "__main__":
    main()