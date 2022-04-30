import numpy as np

from TP3.data_structs.Layer import Layer, NeuralNetwork
from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, sigmoid_tanh_activation, \
    sigmoid_tanh_activation_derivative
from TP3.perceptron_funcs.errors import scaling_identity
from TP3.utils.parser import parse_nums, nums_out_parity
from TP3.utils.splitter import k_splitting


def main():
    numbers = parse_nums("../assets/numbers.txt",7)
    numbers_o = nums_out_parity()

    layer1 = Layer(16, 35)
    layer2 = Layer(10, 16)
    layer3 = Layer(1, 10)
    XTrainSet,YTrainSet,XTestSet,YTestSet = k_splitting(numbers,numbers_o,5)

    for i in range (len(XTrainSet)):
        print("-----------------------------")
        print("Testing partition set + " + str(i))
        print("Train set: " + str(XTrainSet[i]) + "\n")
        print("Test set: " + str(XTestSet[i]) + "\n")

        # Combine the layers to create a neural network
        neural_network = NeuralNetwork([layer1, layer2,layer3], sigmoid_tanh_activation, sigmoid_tanh_activation_derivative, 0.1)
        neural_network.train(XTrainSet[i],YTrainSet[i],300)

        print("Achieved error in parity: ", neural_network.eval_error(XTestSet[i],YTestSet[i]))
        print("Achived accuracy in parity: ", neural_network.accuracy(XTestSet[i],YTestSet[i],[-1,1]))



if __name__ == "__main__":
    main()