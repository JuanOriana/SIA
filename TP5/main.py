import time

import numpy as np

from TP5.data_structs.Layer import Layer, NeuralNetwork
from TP5.perceptron_funcs.activations import step_activation, linear_activation, sigmoid_classic_activation, \
    sigmoid_classic_activation_derivative, sigmoid_tanh_activation, sigmoid_tanh_activation_derivative
from TP5.resources.fonts import get_parsed_fonts, print_letters, create_alphabet


def main():



    layer1 = Layer(5, 35)
    layer2 = Layer(2, 5)
    layer3 = Layer(5,2)
    layer4 = Layer(35,5)

    inputs = get_parsed_fonts()

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork([layer1,layer2,layer3,layer4],sigmoid_classic_activation,sigmoid_classic_activation_derivative,0.1)

    "Stage 1) Random starting synaptic weights: "
    #neural_network.print_weights()

    # training_set_inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    # training_set_outputs = np.array([[0, 1, 1, 1, 1, 0, 0]]).T

    # Train the neural network using the training set.
    # Do it 60,000 times and make small adjustments each time.
    start_time = time.time()
    print("training...")
    neural_network.train(inputs, inputs, 1)
    end_time = time.time()
    print(end_time - start_time)

    # layer1 = neural_network.layers[0]
    # layer2 = neural_network.layers[1]

    # neural_network1 = NeuralNetwork([layer1,layer2],sigmoid_tanh_activation,sigmoid_tanh_activation_derivative,0.1)
    # output = neural_network1.activate(inputs[0])
    # print(output[-1])

    "Stage 2) New synaptic weights after training: "
    #neural_network.print_weights()

    # Test the neural network with a new situation.
    "Stage 3) Considering a new situation [1, 1, 0] -> ?: "
    for i in range(len(inputs)):
        print("EXPECTED LETTER")
        print_letters(create_alphabet([inputs[i]]))
        print("FINAL LETTER")
        print_letters(create_alphabet([(neural_network.activate(inputs[i])[-1])]))
        print("/////////////////////////////////")
    print(neural_network.eval_error(inputs,inputs))
    # print(neural_network.eval_error(training_set_inputs,training_set_inputs))




if __name__ == "__main__":
    main()