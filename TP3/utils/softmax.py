import numpy as np
import math


def softmax(og_outs: np.ndarray):
    z_exp = [math.exp(i) for i in og_outs]
    sum_z_exp = sum(z_exp)
    return [i / sum_z_exp for i in z_exp]
