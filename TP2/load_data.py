import numpy as np
# 10^-7
from TP2.data_structs.Individual import Individual
from TP2.data_structs.TestCase import TestCase
from TP2.utils.aptitude import loaded_aptitude, big_f

solution = Individual(np.array([18.198890215902043, 19.887470841120884, 17.738368717311303,
       0.6652017218928963, 0.335103249657387, 5.854675779470559,
       0.5791663670483601, -0.7423788891309104, 7.785770197567634,
       -0.9460407296950941, -1.3617190069927492]),loaded_aptitude)

for i in range(3):
  rand_arr = np.random.rand(3)*8-4
  rand_data = TestCase(1.0,rand_arr.tolist())
  print(rand_arr)
  print(big_f(solution,rand_data))

# results of test:
#[-3.10572066 -1.22058696  1.18943874]
# 0.9999999960102027
# [ 2.36450485 -0.22315417 -3.49505961]
# 1.2483102208380704e-08
# [-1.59391869 -1.08726703  3.47960297]
# 0.9999999963441942