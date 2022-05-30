import numpy as np


def mutate(letter: np.ndarray, prob: float):
    for i in range(letter.size):
        if np.random.random() > prob:
            letter[i] *= -1
