import numpy as np


class SimplePerceptron:

    def solve(self, inputs: np.ndarray, expected_outputs: np.ndarray, max_gen: int, learning_rate: float,
              error_f, activation_f):
        test_count = inputs.shape[0]
        if test_count != expected_outputs.shape[0]:
            raise Exception("Not enough outputs for the given inputs")

        current_gen = 0
        w = np.zeros(inputs[0].size + 1)
        error = 1

        # Ideal values
        min_error = test_count * 2
        min_w = None
        min_gen = -1
        # Adding constant value to the end of each input for threshold
        inputs = np.append(inputs, np.zeros((test_count, 1)) + 1, axis=1)

        while current_gen < max_gen and error > 0:
            chosen_idx = np.random.choice(np.arange(test_count))
            h = np.dot(inputs[chosen_idx], w)
            O = activation_f(h)
            delta_w = learning_rate * (expected_outputs[chosen_idx] - O) * inputs[chosen_idx]
            w += delta_w
            error = error_f(inputs, expected_outputs, w)
            if error < min_error:
                min_error = error
                min_w = w
                min_gen = current_gen

            current_gen += 1

        return [w, min_w, min_error, min_gen]
