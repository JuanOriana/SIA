import matplotlib.pyplot as plt
from TP5.data_structs.Layer import NeuralNetwork
import numpy as np
from TP5.resources.fonts import symbols1


def plot_latent_space_2D(latent_space:np.array, decoder:NeuralNetwork):

    fig, ax = plt.subplots(1, 2)

    ax[0].set_title("Espacio latente")
    ax[0].set_ylim((0,1.1))
    ax[0].set_xlim((0,1.1))
    ax[1].set_title("Imagen generada")
    # plt.scatter(latent_space[:, 0], latent_space[:, 1])

    for i in range(len(latent_space[:,0])):
        ax[0].annotate(symbols1[i],(latent_space[i][0], latent_space[i][1]))


    def onclick(event):
        global flag
        ix, iy = event.xdata, event.ydata
        latent_vector = np.array([[ix, iy]])
        
        decoded_img = decoder.activate(latent_vector)[-1]
        decoded_img = decoded_img.reshape(7, 5)
        ax[1].imshow(decoded_img, cmap='gray')
        plt.draw()

    cid = fig.canvas.mpl_connect('motion_notify_event', onclick)
    plt.show()

def plot_error(error:np.array, title):

    plt.title("Denoising error con mutacion:"+ str(mutation))
    plt.ylabel("Error obtenido")
    plt.xlabel("Iteracion")
    plt.plot(error[:, 0], error[:, 1])
    plt.show()