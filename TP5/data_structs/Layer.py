import numpy as np
from qiskit.algorithms.optimizers import ADAM
from scipy import optimize

class Layer():

    def __init__(self, neuron_count, input_size):
        self.synaptic_weights = 2 * np.random.random((input_size, neuron_count)) - 1
        self.bias = 2 * np.random.random(neuron_count) - 1
        self.error_d = None
        self.dim = (input_size,neuron_count)

    def calc_error_d(self, inherited_error, derivative, activation):
        self.error_d = inherited_error * derivative(activation)

    def apply_delta(self, last_activation, learn_rate):
        act_mat = np.matrix(last_activation)
        err_mat = np.matrix(self.error_d)
        self.synaptic_weights += learn_rate * act_mat.T.dot(err_mat)
        self.bias += learn_rate*self.error_d

    def activate(self, feed, learn_f):
        return learn_f(np.dot(feed, self.synaptic_weights) + self.bias)

    def __str__(self):
        return str(self.synaptic_weights)


class NeuralNetwork:
    def __init__(self, layers, learn_f, learn_d, learn_rate):
        self.layers = layers
        self.learn_f = learn_f
        self.learn_d = learn_d
        self.learn_rate = learn_rate
        self.train_in = None
        self.train_out = None
    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, max_iteration):

        for iteration in range(max_iteration):
            # Pass the training set through our neural network
            print(iteration)
            self.train_in = training_set_inputs
            self.train_out = training_set_outputs
            net_as_uni = self.net_as_uni()
            res = optimize.minimize(self.eval_error_uni, net_as_uni, method='L-BFGS-B',options={'maxiter':100})
            # for i in range(len(training_set_inputs)):
            #     # Pass the training set through our neural network
            #     activations = self.activate(training_set_inputs[i])
            #     self.layers[-1].calc_error_d(training_set_outputs[i] - activations[-1], self.learn_d, activations[-1])
            #     for i in range(len(self.layers) - 2, -1, -1):
            #         inherit_layer = self.layers[i + 1]
            #         self.layers[i].calc_error_d(inherit_layer.synaptic_weights.dot(inherit_layer.error_d), self.learn_d,
            #                                     activations[i + 1])
            #
            #     for i in range(len(self.layers)):
            #         self.layers[i].apply_delta(activations[i], self.learn_rate)

    # The neural network thinks.
    def activate(self, init_input):
        activations = [init_input]
        for i in range(len(self.layers)):
            activations.append(self.layers[i].activate(activations[-1],self.learn_f))
        return activations

    # The neural network prints its weights
    def print_weights(self):
        for i in range(len(self.layers)):
            print("   Layer " + str(i))
            print(self.layers[i])

    def eval_error(self,test_set,expected_out):
        error = 0
        for i in range(test_set.shape[0]):
            estimation = self.activate(test_set[i])[-1]
            error += (expected_out[i] - estimation) **2
        return np.sum(error) / test_set.shape[0]

    def eval_error_uni(self,uni):
        self.uni_as_net(uni)
        return self.eval_error(self.train_in,self.train_out)

    def accuracy(self,test_set,expected_out,out_classes):
        matches = 0
        for case_idx in range(len(test_set)):
            guess = self.activate(test_set[case_idx])[-1][0]
            closest_idx = (np.abs(out_classes-guess)).argmin()
            matches += 1 if out_classes[closest_idx] == expected_out[case_idx] else 0
        return matches/len(test_set)

    def accuracy_by_node(self,test_set,expected_out):
        matches = 0
        for case_idx in range(len(test_set)):
            guess = self.activate(test_set[case_idx])[-1]
            max_idx = guess.argmax()
            matches += 1 if expected_out[case_idx][max_idx] == 1 else 0
        return matches/len(test_set)

    def net_as_uni(self):
        all_flattened = []
        for layer in self.layers:
            all_flattened.append(layer.synaptic_weights.flatten())
        return np.concatenate(all_flattened)

    def uni_as_net(self,uni:np.ndarray):
        start = 0
        for layer in self.layers:
            end = start + layer.dim[0]*layer.dim[1]
            layer.synaptic_weights = uni[start:end].reshape(layer.dim)
            start = end
