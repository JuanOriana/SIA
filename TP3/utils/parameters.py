import json

from TP3.perceptron_funcs.activations import step_activation, linear_activation, sigmoid_classic_activation, sigmoid_tanh_activation, sigmoid_classic_activation_derivative, sigmoid_tanh_activation_derivative
from TP3.utils.parser import parse

activation_functions = { 'step_activation':step_activation, 'linear_activation':linear_activation, 'sigmoid_classic_activation':sigmoid_classic_activation, 'sigmoid_tanh_activation':sigmoid_tanh_activation, 'sigmoid_classic_activation_derivative':sigmoid_classic_activation_derivative, 'sigmoid_tanh_activation_derivative':sigmoid_tanh_activation_derivative }

class Parameters(object):

    def __init__(self, input_json_file_name):
        self.normalize = None
        self.inputs_file_name = None
        self.inputs = None
        self.expected_file_name = None
        self.expected = None
        self.activation = None
        self.learning_rate = None
        self.batch_size = None
        self.from_json(input_json_file_name)

    def load_parameters(self, inputs, normalize, expected, activation, learning_rate, batch_size):

        if not inputs: raise Exception("ERROR: An input data file name must be defined.")
        elif not expected: raise Exception("ERROR: An expected data file name must be defined.")
        elif not activation: raise Exception("ERROR: An activation function must be defined.")
        elif not learning_rate: raise Exception("ERROR: A learning rate must be specified.")
        elif not batch_size: raise Exception("ERROR: A batch size must be specified.")
        else:

            if not activation_functions.__contains__(activation): raise Exception("ERROR: Activation function: " + activation + " - is not a valid one")
            else: self.activation = activation_functions[activation]

            self.inputs_file_name = inputs
            self.normalize = normalize
            self.inputs = parse(inputs, self.normalize)
            self.expected_file_name = expected
            self.expected = parse(expected).flatten()
            self.learning_rate = learning_rate
            self.batch_size = batch_size


    def from_json(self, input_json_file_name):
        input_file = ""
        try:
            input_file = open(input_json_file_name)
        except Exception:
            print("File error: Invalid json file passed as config")
            quit(1)
        data = json.load(input_file)

        if "normalize" in data:
            normalize = True
        else:
            normalize = False

        self.load_parameters(data['inputs_data_file'], normalize, data['expected_data_file'], data['activation_function'], data['learning_rate'], data['batch_size'])
        input_file.close()

    def __str__(self) -> str:
        toRet = "Parameters: \n - inputs file name = {inputs}\n - expected file name = {expected}\n - activation function = {activation}\n - learning rate = {learning_rate}\n - batch size = {batch_size}\n"
        return toRet.format(inputs=self.inputs_file_name, expected=self.expected_file_name, activation=self.activation.__name__, learning_rate=str(self.learning_rate), batch_size=str(self.batch_size))

