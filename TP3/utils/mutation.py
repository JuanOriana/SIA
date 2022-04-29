import numpy as np


def mutate_set(set: np.ndarray, mutation_p: float):
    for elem in set:
        for i in range(len(elem)):
            if np.random.random() < mutation_p:
                elem[i] = (elem[i] + 1) % 2
