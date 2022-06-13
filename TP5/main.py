import numpy as np

from TP5.data_structs.Layer import Layer, NeuralNetwork
from TP5.perceptron_funcs.activations import step_activation, linear_activation, sigmoid_classic_activation, \
    sigmoid_classic_activation_derivative, sigmoid_tanh_activation, sigmoid_tanh_activation_derivative


def main():



    layer1 = Layer(1, 3)
    layer2 = Layer(3,1)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork([layer1,layer2],sigmoid_tanh_activation,sigmoid_tanh_activation_derivative,0.1)

    "Stage 1) Random starting synaptic weights: "
    neural_network.print_weights()

    training_set_inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    training_set_outputs = np.array([[0, 1, 1, 1, 1, 0, 0]]).T

    # Train the neural network using the training set.
    # Do it 60,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_inputs, 10000)

    "Stage 2) New synaptic weights after training: "
    neural_network.print_weights()

    # Test the neural network with a new situation.
    "Stage 3) Considering a new situation [1, 1, 0] -> ?: "
    outputs = neural_network.activate([0,1,1])
    print (outputs[-1])
    print(neural_network.eval_error(training_set_inputs,training_set_inputs))



if __name__ == "__main__":
    main()