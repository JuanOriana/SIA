import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation
from TP3.perceptron_funcs.errors import scaling_identity


def main():
    inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_outputs_y = np.array([-1, -1, -1, 1])
    expected_outputs_o = np.array([1, 1, -1, -1])

    perceptron = SimplePerceptron(inputs[0].size,step_activation ,0.01)
    perceptron.train(inputs,expected_outputs_y,10,perceptron.random_learn,scaling_identity,1,1)
    print("Achieved error in AND:", perceptron.error)

    perceptron = SimplePerceptron(inputs[0].size,step_activation ,0.01)
    perceptron.train(inputs,expected_outputs_o,10,perceptron.random_learn,scaling_identity,1,1)
    print("Achieved error in XOR:", perceptron.error)



if __name__ == "__main__":
    main()