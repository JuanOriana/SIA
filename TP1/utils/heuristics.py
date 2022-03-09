from TP1.data_structs.EightState import EightState


def basic_heuristic(state: EightState) -> int:
    estimation = 0
    for x in range(state.width):
        for y in range(state.height):
            estimation += 1 if state.board[x, y] != EightState.finished_state[x, y] else 0
    return estimation
