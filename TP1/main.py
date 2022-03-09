import numpy as np

from TP1.data_structs.EightState import EightState
from TP1.algos.not_informed import bfs

board = EightState(np.matrix([[1,2,3],[4,5,6],[7,0,8]],dtype=int))


bfs(board)