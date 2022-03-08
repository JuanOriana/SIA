import numpy as np

from TP1.data_structs.EightState import EightState

board = EightState(np.matrix([[1,2,3],[4,5,6],[7,0,8]],dtype=int))
print(board)
print("________________________________________________________________________")
for move in board.possible_moves():
    print(move)
    print("_________I WON!_________" if move.is_winning() else "_________________________________")
