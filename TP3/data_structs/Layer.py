import numpy as np


class Layer():
    def __init__(self, neuron_count, input_size, isFirst=False):
        self.synaptic_weights = 2 * np.random.random((input_size + (1 if isFirst else 0), neuron_count ))
        self.error_d = None
        self.delta = None

    def calc_error_d(self, inherited_error, derivative, activation):
        self.error_d = inherited_error * derivative(activation)

    def calc_delta(self, last_activation,learn_rate):
        act_mat = np.matrix(last_activation)
        err_mat = np.matrix(self.error_d)
        self.delta = learn_rate*act_mat.T.dot(err_mat)

    def apply_delta(self):
        self.synaptic_weights += self.delta

    def __str__(self):
        return str(self.synaptic_weights)


class NeuralNetwork:
    def __init__(self, layers, learn_f, learn_d,learn_rate):
        self.layers = layers
        self.learn_f = learn_f
        self.learn_d = learn_d
        self.learn_rate = learn_rate

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, max_iteration):

        training_set_inputs = np.append(training_set_inputs, np.zeros((training_set_inputs.shape[0], 1)) + 1, axis=1)
        for iteration in range(max_iteration):
            for i in range(len(training_set_inputs)):
                # Pass the training set through our neural network
                activations = self.activate(training_set_inputs[i])
                self.layers[-1].calc_error_d(training_set_outputs[i] - activations[-1], self.learn_d, activations[-1])
                for i in range(len(self.layers) - 2, -1, -1):
                    inherit_layer = self.layers[i + 1]
                    self.layers[i].calc_error_d(inherit_layer.synaptic_weights.dot(inherit_layer.error_d), self.learn_d,
                                                activations[i + 1])

                for i in range(len(self.layers)):
                    curr_layer = self.layers[i]
                    curr_layer.calc_delta(activations[i],self.learn_rate)
                    curr_layer.apply_delta()

    # The neural network thinks.
    def activate(self, init_input):
        activations = [init_input]
        for i in range(len(self.layers)):
            activations.append(self.learn_f(np.dot(activations[-1], self.layers[i].synaptic_weights)))
        return activations

    # The neural network prints its weights
    def print_weights(self):
        for i in range(len(self.layers)):
            print("   Layer " + str(i))
            print(self.layers[i])
