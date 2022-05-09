import matplotlib.pyplot as plt
import numpy as np

from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation
import gif


@gif.frame
def helper_plot_1(perceptron,inputs_h,expected_h, batch, alpha_value, batch_num):
    learned = perceptron.train_by_batch(inputs_h, expected_h, batch, perceptron.random_learn)
    print(learned)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    w = learned[0]
    x = np.linspace(-2, 2, 100)
    y = (w[0] * x + w[2]) / -w[1]
    alpha_value += 0.2
    plt.plot(x, y, label='line', alpha=alpha_value, linewidth=3)
    plt.xlabel('Coordinate x of ζ')
    plt.ylabel('Coordinate y of ζ')
    graph_title = "Iteration number: {gen_num}"
    plt.title(graph_title.format(gen_num=batch_num))
    for i in range(len(inputs)):
        if expected[i] < 0:
            plt.plot(inputs[i][0], inputs[i][1], marker='o', markersize=20, markerfacecolor="black",
                     markeredgecolor="white")
        else:
            plt.plot(inputs[i][0], inputs[i][1], marker='o', markersize=20, markerfacecolor="white",
                     markeredgecolor="black")

if __name__ == "__main__":

    ### XOR EXAMPLE
    inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected = np.array([1, 1, -1, -1])

    ## AND EXAMPLE
    # inputs = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    # expected = np.array([-1, -1, -1, 1])

    perceptron = SimplePerceptron(inputs[0].size, step_activation, 0.01)
    alpha_value = 0.1
    frames = []
    for batch in range(1,50):
        frames.append(helper_plot_1(perceptron,inputs,expected,1,alpha_value, batch))

    gif.save(frames,"step_perceptron.gif", duration=200)
