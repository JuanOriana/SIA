import json

from TP3.perceptron_funcs.activations import step_activation, linear_activation, sigmoid_classic_activation, \
    sigmoid_tanh_activation, sigmoid_classic_activation_derivative, sigmoid_tanh_activation_derivative
from TP3.utils.parser import parse

activation_functions = {'step_activation': step_activation, 'linear_activation': linear_activation,
                        'sigmoid_classic_activation': sigmoid_classic_activation,
                        'sigmoid_tanh_activation': sigmoid_tanh_activation,
                        'sigmoid_classic_activation_derivative': sigmoid_classic_activation_derivative,
                        'sigmoid_tanh_activation_derivative': sigmoid_tanh_activation_derivative}


class Parameters(object):

    def __init__(self, input_json_file_name):
        self.activation = None
        self.learning_rate = None
        self.batch_size = None
        self.from_json(input_json_file_name)

    def load_parameters(self, activation, learning_rate, iters):

        if not activation:
            raise Exception("ERROR: An activation function must be defined.")
        elif not learning_rate:
            raise Exception("ERROR: A learning rate must be specified.")
        elif not iters:
            raise Exception("ERROR: A batch size must be specified.")
        else:
            if not activation_functions.__contains__(activation):
                raise Exception("ERROR: Activation function: " + activation + " - is not a valid one")
            else:
                self.activation = activation_functions[activation]

            self.learning_rate = learning_rate
            self.iters = iters

    def from_json(self, input_json_file_name):
        input_file = ""
        try:
            input_file = open(input_json_file_name)
        except Exception:
            print("File error: Invalid json file passed as config")
            quit(1)
        data = json.load(input_file)

        self.load_parameters(data['activation_function'], data['learning_rate'], data['iters'])
        input_file.close()

    def __str__(self) -> str:
        toRet = "Parameters: \n - activation function = {activation}\n - learning rate = {learning_rate}\n - iters = {iters}\n"
        return toRet.format(activation=self.activation.__name__, learning_rate=str(self.learning_rate),
                            iters=str(self.iters))
