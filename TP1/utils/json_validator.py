import json

from TP1.data_structs.EightState import EightState
from TP1.utils.searcher_picker import not_informed_algorithms, informed_algorithms, heuristics_functions


def json_validator(data):
    return_value = {'is_valid': True, 'matrix': None, 'algorithm_name': '', 'heuristic': 'basic', 'error_msg': ""}
    if 'algorithm' not in data or 'start_state' not in data:
        return_value['error_msg'] = "Fields algorithm and start_state must be on json"
        return_value['is_valid'] = False
        return return_value

    if not EightState.is_matrix_solvable(
            [data['start_state']['0'], data['start_state']['1'], data['start_state']['2']]):
        return_value['error_msg'] = "This matrix does not correspond to a valid state in the game"
        return_value['is_valid'] = False
        return return_value

    if not (informed_algorithms.__contains__(data['algorithm']) or not_informed_algorithms.__contains__(
            data['algorithm'])):
        return_value['error_msg'] = "No such algorithm name"
        return_value['is_valid'] = False
        return return_value

    if informed_algorithms.__contains__(data['algorithm']):
        if 'heuristic' not in data or not heuristics_functions.__contains__(data['heuristic']):
            return_value[
                'error_msg'] = "A valid Heuristic field must be included when using informed algorithms and must have a valid"
            return_value['is_valid'] = False
            return return_value
        else:
            return_value['heuristic'] = data['heuristic']

    return_value['algorithm_name'] = data['algorithm']
    return_value['matrix'] = [data['start_state']['0'], data['start_state']['1'], data['start_state']['2']]

    return return_value


def file_validator(file_name):
    try:
        input_file = open(file_name)
    except Exception:
        print("File error: Invalid json file passed as config")
        quit(1)
    data = json.load(input_file)
    json_information = json_validator(data)
    if not json_information['is_valid']:
        print("Invalid JSON: " + json_information['error_msg'])
        quit(2)
    return json_information
