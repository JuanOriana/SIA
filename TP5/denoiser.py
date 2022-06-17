import time

from TP3.data_structs.Layer import Layer, NeuralNetwork
from TP3.perceptron_funcs.activations import *
from TP5.resources.fonts import get_parsed_fonts
from TP5.resources.fonts import get_parsed_fonts, print_letters
import numpy as np

from TP5.utils import mutation
from TP5.utils.mutation import mutate_set


def denoiser():
    mutation_prob = 0.1
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
    for numb in numbers:
        copy_ex = np.copy(numb)
        outputs.append(copy_ex)
        copy_in = np.copy(numb)
        mutate_set([copy_in],mutation_prob)
        inputs.append(copy_in)

    neural_network = NeuralNetwork([layer1, layer2, layer3, layer4,layer5,layer6], sigmoid_classic_activation,
                                   sigmoid_classic_activation_derivative, 0.1)

    start_time = time.time()
    print("training...")
    neural_network.train(inputs, outputs, 5000)
    end_time = time.time()
    print(end_time - start_time)

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
        mutate_set([copy_in],mutation_prob)
        activations.append(copy_in)

    # Vemos como aprende los inputs
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