import numpy as np

from TP1.data_structs.EightState import EightState
from TP1.algos.not_informed import bfs
from TP1.algos.informed import hill_climbing_local
from TP1.utils.heuristics import basic_heuristic


board = EightState(np.matrix([[1,0,3],[4,2,5],[6,7,8]],dtype=int))
hill_climbing_local(board,basic_heuristic)

