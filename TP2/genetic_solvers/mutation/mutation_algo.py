import numpy as np

from TP2.data_structs.Individual import Individual


def mutate(indiv: Individual, prob: float, std: float) -> Individual:
    for i in range(len(indiv.get_state())):
        if np.random.uniform(0, 1) < prob:
            indiv.get_state()[i] += np.random.normal(0, std)
    indiv.aptitude_concrete = indiv.aptitude(indiv)
    return indiv
