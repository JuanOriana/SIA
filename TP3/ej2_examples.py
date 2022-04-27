import matplotlib.pyplot as plt
import numpy as np
from TP3.utils.parser import parse
from TP3.data_structs.SimplePerceptron import SimplePerceptron
from TP3.perceptron_funcs.activations import step_activation, linear_activation
import gif


@gif.frame
def helper_plot_1(perceptron,inputs_h,expected_h, batch, alpha):
    learned = perceptron.train_by_batch(inputs_h, expected_h, batch, perceptron.random_learn)
    normal = learned[0][0:3]
    x, y = np.linspace(-4, 4, 100), np.linspace(-4, 4, 100)
    xx, yy = np.meshgrid(x, y)
    # z = (-normal[0] * xx - normal[1] * yy - point) * 1. / normal[2] TODO: Ver el umbral a q hace ref
    z = (-normal[0] * xx - normal[1] * yy) * 1. / normal[2]
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    c = expected
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    img = ax.scatter(inputs[:, 0], inputs[:, 1], inputs[:, 2], c=c, cmap='viridis', alpha=1)
    fig.colorbar(img)
    ax.plot_wireframe(xx, yy, z, colors='blue', alpha=alpha)
    alpha += 0.1
    ax.view_init(elev=10, azim=0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plane: z=f(x,y). Gen size : ' + str(learned[4]))




if __name__ == "__main__":
    inputs = parse("assets/train_set.txt")
    expected = parse("assets/expected.txt").flatten()

    perceptron = SimplePerceptron(inputs[0].size, linear_activation, 0.01)
    alpha = 0.1
    frames = []
    for batch in [10,40,50,100,300,500]:
        frames.append(helper_plot_1(perceptron,inputs,expected,batch,alpha))

    gif.save(frames, "linear_perceptron.gif")


