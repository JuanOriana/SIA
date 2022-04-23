import matplotlib.pyplot as plt
import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation

if __name__ == "__main__":

    ### XOR EXAMPLE
    # inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    # expected = np.array([1, 1, -1, -1])

    ## AND EXAMPLE
    inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected = np.array([-1, -1, -1, 1])

    perceptron = SimplePerceptron(inputs[0].size, step_activation, 0.01)
    alpha_value = 0.1
    for batch in [1, 2, 3, 4, 10]:
        learned = perceptron.train_by_batch(inputs, expected, batch, perceptron.random_learn)
        print(learned)
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        w = learned[0]
        x = np.linspace(-2, 2, 100)
        y = (w[0] * x + w[2]) / -w[1]
        plt.plot(x, y, label='line', alpha=alpha_value, linewidth=3)
        alpha_value += 0.2
        for i in range(len(inputs)):
            if expected[i] < 0:
                plt.plot(inputs[i][0], inputs[i][1], marker='o', markersize=20, markerfacecolor="black",
                         markeredgecolor="white")
            else:
                plt.plot(inputs[i][0], inputs[i][1], marker='o', markersize=20, markerfacecolor="white",
                         markeredgecolor="black")

    plt.show()
