from TP1.data_structs.EightState import EightState
from TP1.utils.searcher_picker import not_informed_algorithms, informed_algorithms, heuristics_functions


def json_validator(data):
    return_value = {'is_valid': True, 'matrix': None, 'algorithm_name': '', 'heuristic': 'basic', 'error_msg': ""}
    if 'algorithm' not in data or 'start_state' not in data:
        return_value['error_msg'] = "Invalid JSON.Fields algorithm and start_state must be on json"
        return_value['is_valid'] = False
        return return_value

    if not EightState.is_matrix_solvable(
            [data['start_state']['0'], data['start_state']['1'], data['start_state']['2']]):
        return_value['error_msg'] = "Invalid JSON: This matrix does not correspond to a valid state in the game"
        return_value['is_valid'] = False
        return return_value

    if not (informed_algorithms.__contains__(data['algorithm']) or not_informed_algorithms.__contains__(
            data['algorithm'])):
        return_value['error_msg'] = "Invalid JSON: No such algorithm name"
        return_value['is_valid'] = False
        return return_value

    if informed_algorithms.__contains__(data['algorithm']):
        if 'heuristic' not in data or not heuristics_functions.__contains__(data['heuristic']):
            return_value['error_msg'] = "Invalid JSON: A valid Heuristic field must be included when using informed algorithms and must have a valid"
            return_value['is_valid'] = False
            return return_value
        else:
            return_value['heuristic'] = data['heuristic']

    return_value['algorithm_name'] = data['algorithm']
    return_value['matrix'] = [data['start_state']['0'], data['start_state']['1'], data['start_state']['2']]

    return return_value
