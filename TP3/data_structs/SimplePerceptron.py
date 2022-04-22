import numpy as np

from TP3.perceptron_funcs.errors import activation_based_error


class SimplePerceptron:

    def __init__(self, activation_f, learning_rate: float, derivative=None):
        self.activation_f = activation_f
        self.derivative = derivative
        self.learning_rate = learning_rate
        self.current_gen = 0
        self.w = np.zeros(1)
        self.error = 1
        self.min_error = 1
        self.min_w = None
        self.min_gen = -1

    def learn(self, learn_set: np.ndarray, expected_outputs: np.ndarray, max_gen: int):
        test_count = learn_set.shape[0]
        if test_count != expected_outputs.shape[0]:
            raise Exception("Not enough outputs for the given inputs")

        self.reset(learn_set[0].size)
        # Adding constant value to the end of each input for threshold
        learn_set = np.append(learn_set, np.zeros((test_count, 1)) + 1, axis=1)

        while self.current_gen < max_gen and self.error > 0:
            chosen_idx = np.random.choice(np.arange(test_count))
            h = np.dot(learn_set[chosen_idx], self.w)
            estimation = self.activation_f(h)
            delta_w = self.learning_rate * (expected_outputs[chosen_idx] - estimation) * learn_set[chosen_idx]
            if self.derivative is not None:
                delta_w *= self.derivative(estimation)
            self.w += delta_w
            self.error = activation_based_error(learn_set, expected_outputs, self.w, self.activation_f)
            if self.error < self.min_error:
                self.min_error = self.error
                self.min_w = self.w
                self.min_gen = self.current_gen

            self.current_gen += 1

        return self.w, self.min_w, self.min_error, self.min_gen

    def evaluate(self, test):
        if self.current_gen == 0:
            raise Exception("Has not learnt yet!")
        if test.size != (self.w.size - 1):
            raise Exception("Wrong input size")
        test = np.append(test, 1)
        return self.activation_f(np.dot(test, self.w))

    def reset(self, dimension: int):
        self.current_gen = 0
        self.w = np.zeros(dimension + 1)
        self.error = 1
        self.min_error = float("inf")
        self.min_w = None
        self.min_gen = -1
