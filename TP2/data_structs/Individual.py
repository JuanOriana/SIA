import numpy as np

from TP2.data_structs.TestCase import TestCase
from TP2.utils.aptitude import aptitude


class Individual:

    def __init__(self, state: np.ndarray, test_case: TestCase):
        self.state = state
        self.aptitude = aptitude(self, test_case)

    def get_big_w(self):
        # (0W0, 1W1, 2W2, 3w11, 4w12, 5w13, 6w21, 7w22, 8w23, 9w01, 10w02)
        return self.state[0:3]

    def get_little_w(self, row):
        return self.state[3 * row:3 * row + 3]

    def get_w_0(self):
        return self.state[9:]
