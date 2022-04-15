import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, linear_activation, sigmoid_classic_activation, \
    sigmoid_classic_activation_derivative
from TP3.utils.parser import parse


def main():

    test_cases = parse("assets/train_set.txt")
    expected = parse("assets/expected.txt").flatten()

    inputs_y = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_outputs_y = np.array([-1, -1, -1, 1])
    #expected_outputs_o = np.array([1, 1, -1, -1])

    perceptron = SimplePerceptron(linear_activation ,0.01)
    print(perceptron.learn(inputs_y,expected_outputs_y,10000))


if __name__ == "__main__":
    main()