import sys

import matplotlib.pyplot as plt
import numpy as np

from TP3.perceptron_funcs.errors import scaling_tanh, scaling_identity
from TP3.utils import splitter
from TP3.utils.parameters import Parameters
from TP3.utils.parser import parse
from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import *
import gif

from TP3.utils.splitter import split_train_and_learn, k_splitting

k = 5
# @gif.frame
# def helper_plot_1(perceptron, inputs_h, expected_h, batch, alpha,):
#     learned = perceptron.train_by_batch(inputs_h, expected_h, batch, perceptron.random_learn)
#     normal = learned[0][0:3]
#     x, y = np.linspace(-4, 4, 100), np.linspace(-4, 4, 100)
#     xx, yy = np.meshgrid(x, y)
#     # z = (-normal[0] * xx - normal[1] * yy - point) * 1. / normal[2] TODO: Ver el umbral a q hace ref
#     z = (-normal[0] * xx - normal[1] * yy) * 1. / normal[2]
#     fig = plt.figure()
#     ax = fig.add_subplot(projection='3d')
#     c = expected
#     ax.set_xlim(-5, 5)
#     ax.set_ylim(-5, 5)
#     ax.set_zlim(-5, 5)
#     img = ax.scatter(inputs[:, 0], inputs[:, 1], inputs[:, 2], c=c, cmap='viridis', alpha=1)
#     fig.colorbar(img)
#     ax.plot_wireframe(xx, yy, z, colors='blue', alpha=alpha)
#     alpha += 0.1
#     ax.view_init(elev=10, azim=0)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Plane: z=f(x,y). Gen size : ' + str(learned[4]))

def plot_sigmoid_tanh_k(limit, train_inputs, train_expected, test_inputs, test_expected, learning_factor, min_value, max_value):
    accuracy_train = {}
    accuracy_test = {}
    batch = [1, 4, 5, 10, 10, 20]
    for j in range(k):
        accuracy_test.update({j: list()})
        perceptron = SimplePerceptron(train_inputs.shape[2], sigmoid_tanh_activation,
                                      derivative=sigmoid_tanh_activation_derivative, learning_rate=learning_factor)
        for i in batch:
            perceptron.train_by_batch(train_inputs[j], train_expected[j], i, perceptron.secuencially_learn,
                                      scaling_error_function=scaling_tanh, max_value=max_value,
                                      min_value=min_value)
            accuracy_test[j].append(perceptron.accuracy(test_inputs[j], test_expected[j], 0.008))

    x_axis = np.array([1, 2, 3, 4, 5, 6])
    widht = [-0.2, -0.1, 0, 0.1, 0.2]
    colors = ['b', 'r', 'y', '#1b9e77', 'g']
    for j in range(k):
        plt.suptitle("Accuracy for tanh.")
        plt.ylabel("Accuracy")
        plt.xlabel("Iteration number")
        plt.bar(x_axis + widht[j], accuracy_test[j], color=colors[j], width=0.1, align='edge', label="k = " + str(j))
        plt.legend()
        plt.xticks(np.array([1, 2, 3, 4, 5, 6]), ['1', '5', '10', '20', '30', '50'])
    plt.show()

    max_accuracy = -1
    best_k = -1
    for idx in range(k):
        if max(accuracy_test[idx]) > max_accuracy:
            best_k = idx
            max_accuracy = max(accuracy_test[idx])
    print("BEST k", best_k)

    # plt.suptitle("Error for linear.")
    # plt.ylabel("Error")
    # plt.ylabel("Iteration number")
    # plt.plot(range(limit), error, 'bo')
    # plt.show()
def plot_sigmoid_tanh(limit, train_inputs, train_expected, test_inputs, test_expected, learning_factor, min_value,
                      max_value):
    perceptron = SimplePerceptron(train_inputs[0].size, sigmoid_tanh_activation, learning_factor,
                                  derivative=sigmoid_tanh_activation_derivative)

    accuracy_train = []
    accuracy_test = []
    error = []
    for i in range(limit):
        perceptron_ret = perceptron.train_by_batch(train_inputs, train_expected, 1, perceptron.secuencially_learn,
                                                   scaling_error_function=scaling_tanh, max_value=max_value,
                                                   min_value=min_value)
        accuracy_train.append(perceptron.accuracy(train_inputs, train_expected, 0.01))
        accuracy_test.append(perceptron.accuracy(test_inputs, test_expected, 0.01))
        error.append(perceptron.error)
        print(i)

    plt.suptitle("Accuracy for sigmoid tanh.")
    plt.ylabel("Accuracy")
    plt.ylabel("Iteration number")
    plt.plot(range(limit), accuracy_train, 'bo')
    plt.plot(range(limit), accuracy_test, 'gx')
    plt.legend(["Train set", "Test set"], loc="lower right")
    plt.show()

    plt.suptitle("Error for sigmoid tanh.")
    plt.ylabel("Error")
    plt.xlabel("Iteration number")
    plt.plot(range(limit), error, 'bo')
    plt.show()


def plot_linear(limit, train_inputs, train_expected, test_inputs, test_expected, learning_factor, min_value, max_value):
    perceptron = SimplePerceptron(train_inputs[0].size, linear_activation, learning_factor, )

    accuracy_train = []
    accuracy_test = []
    error = []

    for i in range(limit):
        perceptron_ret = perceptron.train_by_batch(train_inputs, train_expected, 1, perceptron.secuencially_learn,
                                                   scaling_error_function=scaling_identity, max_value=max_value,
                                                   min_value=min_value)
        accuracy_train.append(perceptron.accuracy(train_inputs, train_expected, 1))
        accuracy_test.append(perceptron.accuracy(test_inputs, test_expected, 1))
        error.append(perceptron.error)
        print(i)

    plt.suptitle("Accuracy for linear.")
    plt.ylabel("Accuracy")
    plt.xlabel("Iteration number")
    plt.plot(range(limit), accuracy_train, 'bo')
    plt.plot(range(limit), accuracy_test, 'gx')
    plt.legend(["Train set", "Test set"], loc="upper right")
    plt.show()

    plt.suptitle("Error for linear.")
    plt.ylabel("Error")
    plt.ylabel("Iteration number")
    plt.plot(range(limit), error, 'bo')
    plt.show()


def main():
    inputs, _, _ = parse("assets/train_set.txt")
    expected, max_value, min_value = parse("assets/expected.txt","TANH")
    batches = [10, 40, 50, 100, 300, 500]
    limit = 50
    inputs_train, expected_train, inputs_test, expected_test = k_splitting(inputs, expected.flatten(), k)

    # plot_sigmoid_tanh(limit, inputs_train[0], expected_train[0], inputs_test[0], expected_test[0], 0.01,min_value,max_value)
    # plot_linear(limit, inputs_train, expected_train, inputs_test, expected_test, 0.01, min_value, max_value)
    plot_sigmoid_tanh_k(limit, inputs_train, expected_train, inputs_test, expected_test, 0.01, min_value, max_value)

if __name__ == "__main__":
    main()
