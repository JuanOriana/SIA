import time

from TP5.data_structs.Layer import Layer, NeuralNetwork
from TP5.perceptron_funcs.activations import *
from TP5.resources.fonts import get_parsed_fonts
from TP5.resources.fonts import get_parsed_fonts, print_letters
import numpy as np

from TP5.utils import mutation
from TP5.utils.mutation import mutate_set
from TP5.utils.plotting_scripts import plot_error


def denoiser():
    mutation_prob = 0.25
    # TODO Elegir una buena arquitectura para el denoiser
    # 35 15 10 5 10 15 35
    layer1 = Layer(15, 35)
    layer2 = Layer(10, 15)
    layer3 = Layer(5, 10)
    layer4 = Layer(10, 5)
    layer5 = Layer(15, 10)
    layer6 = Layer(35, 15)

    ## Obtenemos los numeros del set de datos
    numbers = get_parsed_fonts()[17:26]
    inputs = []
    outputs = []
    ## Cargamos los numeros al trainset
    for numb in numbers:
        inputs.append(numb)
        outputs.append(numb)
    # Cargamos una copia con ruido de los numberos
    for i in range(2):
        for numb in numbers:
            copy_ex = np.copy(numb)
            outputs.append(copy_ex)
            copy_in = np.copy(numb)
            mutate_set([copy_in],mutation_prob)
            inputs.append(copy_in)

    neural_network = NeuralNetwork([layer1, layer2, layer3, layer4,layer5,layer6], sigmoid_classic_activation,
                                   sigmoid_classic_activation_derivative, 0.1)

    # start_time = time.time()
    # print("training...")
    # neural_network.train(np.array(inputs), np.array(outputs), 1000)
    # end_time = time.time()
    # print(end_time - start_time)

    error = []
    for i in range(1000):
        neural_network.train(np.array(inputs), np.array(outputs), 1)
        error.append((i,neural_network.eval_error_uni(neural_network.net_as_uni())))

    plot_error(np.array(error),"Denoising error con mutacion:"+ str(mutation_prob))




    ## Vemos como aprende los inputs
    # for i in range(len(inputs)):
    #     print("EXPECTED LETTER")
    #     print_letters([inputs[i]])
    #     print("FINAL LETTER")
    #     print_letters([(neural_network.activate(inputs[i])[-1])])
    #     print("/////////////////////////////////")

    number_cp = np.copy(numbers)
    outputs_cp = []
    activations = []
    for numb in number_cp:
        copy_ex = np.copy(numb)
        outputs_cp.append(copy_ex)
        copy_in = np.copy(numb)
        mutate_set([copy_in],0.15)
        activations.append(copy_in)

    # Vemos como aprende los inputs
    for j in range(1):
        for i in range(len(activations)):
            print("EXPECTED LETTER")
            print_letters([outputs_cp[i]])
            print("MUTATION LETTER")
            print_letters([activations[i]])
            print("OBTAINED LETTER")
            print_letters([(neural_network.activate(activations[i])[-1])])
            print("/////////////////////////////////")


if __name__ == "__main__":
    denoiser()