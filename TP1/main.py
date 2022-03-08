import numpy as np

from TP1.data_structs.EightState import EightState

board = EightState(np.matrix([[1,5,8],[3,2,7],[4,6,0]],dtype=int))
print(board)
possible_moves = board.possible_moves();
print("A MOVERSE!!!\n")
for move in possible_moves:
    print(move)