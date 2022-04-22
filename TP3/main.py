import numpy as np

from TP3.data_structs.Layer import Layer, NeuralNetwork
from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, linear_activation, sigmoid_classic_activation, \
    sigmoid_classic_activation_derivative, sigmoid_tanh_activation, sigmoid_tanh_activation_derivative
from TP3.utils.parser import parse


def main():

    test_cases = parse("assets/train_set.txt")
    expected = parse("assets/expected.txt").flatten()

    inputs_y = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_outputs_y = np.array([-1, -1, -1, 1])
    #expected_outputs_o = np.array([1, 1, -1, -1])

    # perceptron = SimplePerceptron(inputs_y[0].size,step_activation ,0.01)


    # Create layer 1 (8 neurons, each with 3 inputs)
    layer1 = Layer(8, 3)

    # Create layer 2 (4 neurons with 8 inputs)
    layer2 = Layer(4, 8)

    # Create layer 3 (a single neuron with 4 inputs)
    layer3 = Layer(1,4)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork([layer1, layer2,layer3],sigmoid_tanh_activation,sigmoid_tanh_activation_derivative,1)

    "Stage 1) Random starting synaptic weights: "
    neural_network.print_weights()

    # The training set. We have 7 examples, each consisting of 3 input values
    # and 1 output value.
    training_set_inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    training_set_outputs = np.array([[0, 1, 1, 1, 1, 0, 0]]).T

    # Train the neural network using the training set.
    # Do it 60,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    "Stage 2) New synaptic weights after training: "
    neural_network.print_weights()

    # Test the neural network with a new situation.
    "Stage 3) Considering a new situation [1, 1, 0] -> ?: "
    outputs = neural_network.activate(np.array([0, 0, 0]))
    print (outputs[-1])


if __name__ == "__main__":
    main()