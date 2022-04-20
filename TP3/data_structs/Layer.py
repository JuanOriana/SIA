import numpy as np


class Layer():
    def __init__(self, neuron_count, input_size):
        self.synaptic_weights = 2 * np.random.random((input_size, neuron_count)) - 1
        self.delta = None
        self.adjustment = None

    def calc_delta(self, error, derivative, activation):
        self.delta = error * derivative(activation)

    def calc_adjustment(self, last_activation):
        self.adjustment = last_activation.T.dot(self.delta)

    def apply_adjustment(self):
        self.synaptic_weights += self.adjustment

    def __str__(self):
        return str(self.synaptic_weights)


class NeuralNetwork:
    def __init__(self, layers, learn_f, learn_d):
        self.layers = layers
        self.learn_f = learn_f
        self.learn_d = learn_d

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, max_iteration):
        for iteration in range(max_iteration):
            # Pass the training set through our neural network
            activations = self.activate(training_set_inputs)
            self.layers[-1].calc_delta(training_set_outputs - activations[-1], self.learn_d, activations[-2])
            for i in range(len(self.layers)-1, 0, -1):
                print(i)
                next_layer = self.layers[i + 1]
                error = next_layer.delta.dot(next_layer.synaptic_weights.T)
                self.layers[i].calc_delta(error * self.learn_d(activations[i + 1],self.learn_d,activations[i]))

            for i in range(len(self.layers)):
                curr_layer = self.layers[i]
                curr_layer.calc_adjustment(activations[i].T.dot(curr_layer.delta))
                curr_layer.apply_adjustment()

    # The neural network thinks.
    def activate(self, inputs):
        activations = []
        activations.append(inputs)
        last = inputs
        for i in range(len(activations)):
            activations.append(self.learn_f(np.dot(last, self.layers[i].synaptic_weights)))
            last = activations[-1]
        return activations

    # The neural network prints its weights
    def print_weights(self):
        for i in range(len(self.layers)):
            print("   Layer " + str(i))
            print(self.layers[i])
