import numpy as np


def mutate(indiv: np.ndarray, prob: float, std: float):
    for i in range(len(indiv)):
        if np.random.uniform(0, 1) < prob:
            indiv[i] += np.random.normal(0, std)
    return indiv
