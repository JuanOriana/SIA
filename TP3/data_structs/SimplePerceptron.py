import numpy as np

from TP3.perceptron_funcs.errors import activation_based_error, scaling_identity


class SimplePerceptron:

    def __init__(self, input_size, activation_f, learning_rate: float, derivative=None):
        self.activation_f = activation_f
        self.derivative = derivative
        self.learning_rate = learning_rate
        self.input_size = input_size
        self.reset()

    def train(self, learn_set: np.ndarray, expected_outputs: np.ndarray, max_gen: int, learning_function,scaling_function, max_value , min_value):
        learn_count = learn_set.shape[0]
        # Adding constant value to the end of each input for threshold
        learn_set = np.append(learn_set, np.zeros((learn_count, 1)) + 1, axis=1)
        while self.current_gen < max_gen and self.error > 0:
            learning_function(learn_count, learn_set, expected_outputs,scaling_function,max_value,min_value)
        return self.w, self.min_w, self.min_error, self.min_gen

    def random_learn(self,learn_count,learn_set,expected_outputs,scaling_function,max_value,min_value):
        chosen_idx = np.random.choice(np.arange(learn_count))
        self.learn(learn_set, expected_outputs, chosen_idx,scaling_function,max_value,min_value)

    def secuencially_learn(self,learn_count,learn_set,expected_outputs,scaling_function,max_value,min_value):
        for chosen_idx in range(learn_count):
            self.learn(learn_set, expected_outputs, chosen_idx,scaling_function,max_value,min_value)

    def learn(self, learn_set: np.ndarray, expected_outputs: np.ndarray, chosen_idx: int,scaling_function,max_value,min_value):
        h = np.dot(learn_set[chosen_idx], self.w)
        estimation = self.activation_f(h)
        delta_w = self.learning_rate * (expected_outputs[chosen_idx] - estimation) * learn_set[chosen_idx]
        if self.derivative is not None:
            delta_w *= self.derivative(estimation)
        self.w += delta_w
        self.error = activation_based_error(learn_set, expected_outputs, self.w, self.activation_f,scaling_function,max_value,min_value)
        if self.error < self.min_error:
            self.min_error = self.error
            self.min_w = self.w
            self.min_gen = self.current_gen
        self.current_gen += 1

    def train_by_batch(self, learn_set: np.ndarray, expected_outputs: np.ndarray, batch_size: int,
                       learning_function,scaling_error_function=scaling_identity,max_value = 0, min_value = 0):
        learn_count = learn_set.shape[0]
        if learn_count != expected_outputs.shape[0]:
            raise Exception("Not enough outputs for the given inputs")
        return self.train(learn_set=learn_set, expected_outputs=expected_outputs, max_gen=self.current_gen + batch_size, learning_function=learning_function,scaling_function=scaling_error_function,max_value= max_value , min_value= min_value)

    def evaluate(self, test):
        if self.current_gen == 0:
            raise Exception("Has not learnt yet!")
        if test.size != (self.w.size - 1):
            raise Exception("Wrong input size")
        test = np.append(test, 1)
        return self.activation_f(np.dot(test, self.w))

    def accuracy(self,test_set,expected_out,tolerance:float):
        matches = 0
        for case_idx in range(len(test_set)):
            guess = self.evaluate(test_set[case_idx])
            if np.absolute(guess - expected_out[case_idx]) < tolerance:
                matches += 1
        return matches/len(test_set)

    def reset(self):
        self.current_gen = 0
        self.w = np.zeros(self.input_size + 1)
        self.error = 1
        self.min_error = float("inf")
        self.min_w = None
        self.min_gen = -1
