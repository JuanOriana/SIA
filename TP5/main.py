import time

import numpy as np

from TP5.data_structs.Layer import Layer, NeuralNetwork
from TP5.perceptron_funcs.activations import step_activation, linear_activation, sigmoid_classic_activation, \
    sigmoid_classic_activation_derivative, sigmoid_tanh_activation, sigmoid_tanh_activation_derivative
from TP5.resources.fonts import get_parsed_fonts, print_letters
from TP5.utils.plotting_scripts import plot_latent_space_2D, plot_error


def main():
    layer1 = Layer(5, 35)
    layer2 = Layer(2, 5)
    layer3 = Layer(5, 2)
    layer4 = Layer(35, 5)

    inputs = get_parsed_fonts()

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork([layer1,layer2,layer3,layer4],sigmoid_classic_activation,sigmoid_classic_activation_derivative,0.1)
    encoder = NeuralNetwork([layer1,layer2],sigmoid_classic_activation,sigmoid_classic_activation_derivative,0.1)
    decoder = NeuralNetwork([layer3,layer4],sigmoid_classic_activation,sigmoid_classic_activation_derivative,0.1)
    "Stage 1) Random starting synaptic weights: "
    # neural_network.print_weights()

    # training_set_inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    # training_set_outputs = np.array([[0, 1, 1, 1, 1, 0, 0]]).T

    # Train the neural network using the training set.
    # Do it 60,000 times and make small adjustments each time.
    start_time = time.time()
    print("training...")
    neural_network.train(inputs, inputs, 150)
    end_time = time.time()
    print("Training time", end_time - start_time)

    print(neural_network.layers)
    i = 0
    for layer in neural_network.layers:
        print(i,layer)
        i+=1


    print(neural_network.eval_error_uni(neural_network.net_as_uni()))
    layer1 = neural_network.layers[0]
    layer2 = neural_network.layers[1]
    
    list = []
    neural_network1 = NeuralNetwork([layer1, layer2], sigmoid_classic_activation, sigmoid_classic_activation_derivative,
                                    0.1)
    for i in range(len(inputs)):
        value = neural_network1.activate(inputs[i])[-1]
        list.append(value)
        print("Latent space value: ", value, " for letter in index ", i)
    
    plot_latent_space_2D(np.array(list),decoder)
    print("error final ", neural_network.eval_error_uni(neural_network.net_as_uni()))
    # error = []
    # for i in range(100):
    #     neural_network.train(np.array(inputs), np.array(inputs), 1)
    #     error.append((i, neural_network.eval_error_uni(neural_network.net_as_uni())))
    # plot_error(np.array(error), "Error promedio con metodo: ACA AGREGA EL METODO") # TODO AGREGA EL NOMBRE DEL METODO JUAN

    print(neural_network.net_as_uni());
    "Stage 2) New synaptic weights after training: "
    # neural_network.print_weights()

    # Test the neural network with a new situation.
    "Stage 3) Considering a new situation [1, 1, 0] -> ?: "
    # for i in range(len(inputs)):
    #     print("EXPECTED LETTER")
    #     print_letters([inputs[i]])
    #     print("FINAL LETTER")
    #     print_letters([(neural_network.activate(inputs[i])[-1])])
    #     print("/////////////////////////////////")
    # print(neural_network.eval_error(inputs,inputs))
    # print(neural_network.net_as_uni())
    # print(neural_network.eval_error(training_set_inputs,training_set_inputs))


if __name__ == "__main__":
    main()
