import sys

import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation
from TP3.perceptron_funcs.errors import scaling_identity
from TP3.utils.parameters import Parameters


def main():
    if len(sys.argv) != 2:
        print("Invalid usage: ex1.py <config.json>")
        quit(1)

    params = Parameters(sys.argv[1])

    inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_outputs_y = np.array([-1, -1, -1, 1])
    expected_outputs_o = np.array([1, 1, -1, -1])
    perceptron = SimplePerceptron(inputs[0].size,params.activation ,params.learning_rate)
    perceptron.train(inputs,expected_outputs_y,params.iters,perceptron.random_learn,scaling_identity,1,1)
    print("Achieved error in AND:", perceptron.error)

    perceptron = SimplePerceptron(inputs[0].size,params.activation ,params.learning_rate)
    perceptron.train(inputs,expected_outputs_o,10,perceptron.random_learn,scaling_identity,1,1)
    print("Achieved error in XOR:", perceptron.error)



if __name__ == "__main__":
    main()