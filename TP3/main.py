import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, linear_activation
from TP3.perceptron_funcs.errors import step_error, linear_error
from TP3.utils.parser import parse


def main():

    test_cases = parse("assets/train_set.txt")
    expected = parse("assets/expected.txt").flatten()

    inputs_y = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_outputs_y = np.array([-1, -1, -1, 1])
    #expected_outputs_o = np.array([1, 1, -1, -1])

    perceptron = SimplePerceptron(linear_error, linear_activation,0.1)
    print(perceptron.learn(inputs_y,expected_outputs_y,100000))



if __name__ == "__main__":
    main()