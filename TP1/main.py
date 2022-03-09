import numpy as np

from TP1.data_structs.EightState import EightState
from TP1.algos.not_informed import bfs

board = EightState(np.matrix([[7,3,6],[4,8,2],[1,0,5]],dtype=int))


bfs(board)