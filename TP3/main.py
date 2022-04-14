import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation
from TP3.perceptron_funcs.errors import step_error


def main():

    inputs_y = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_outputs_y = np.array([-1, -1, -1, 1])
    # expected_outputs_o = np.array(1, 1, -1, -1)

    perceptron = SimplePerceptron()

    print(perceptron.solve(inputs_y,expected_outputs_y,10000,0.1,step_error, step_activation))



if __name__ == "__main__":
    main()