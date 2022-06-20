import matplotlib.pyplot as plt
import numpy as np


def plot_latent_space_2D(latent_space:np.array):

    plt.title("Espacio latente")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.ylim((0,1.1))
    plt.xlim((0,1.1))
    # plt.scatter(latent_space[:, 0], latent_space[:, 1])

    for i in range(len(latent_space[:,0])):
        plt.annotate(chr(ord(' ')+i),(latent_space[i][0], latent_space[i][1]))
    plt.show()

def plot_error(error:np.array, title):

    plt.title("Denoising error con mutacion:"+ str(mutation))
    plt.ylabel("Error obtenido")
    plt.xlabel("Iteracion")
    plt.plot(error[:, 0], error[:, 1])
    plt.show()