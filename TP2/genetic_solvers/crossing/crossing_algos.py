import numpy as np


def simple_cross(indiv1: np.ndarray, indiv2: np.ndarray) -> list[np.ndarray]:
    change_idx = np.random.choice(len(indiv1))
    new_indiv1 = np.copy(indiv1)
    new_indiv2 = np.copy(indiv2)
    new_indiv1[change_idx:] = indiv2[change_idx:]
    new_indiv2[change_idx:] = indiv1[change_idx:]
    return [new_indiv1, new_indiv2]


def double_cross(indiv1: np.ndarray, indiv2: np.ndarray) -> list[np.ndarray]:
    change_idx1 = np.random.choice(len(indiv1))
    change_idx2 = change_idx1
    while change_idx2 == change_idx1:
        change_idx2 = np.random.choice(len(indiv1))
    if change_idx1 > change_idx2:
        change_idx1, change_idx2 = change_idx2, change_idx1
    new_indiv1 = np.copy(indiv1)
    new_indiv2 = np.copy(indiv2)
    new_indiv1[change_idx1:change_idx2 + 1] = indiv2[change_idx1:change_idx2 + 1]
    new_indiv2[change_idx1:change_idx2 + 1] = indiv1[change_idx1:change_idx2 + 1]
    return [new_indiv1, new_indiv2]


def rand_cross(indiv1: np.ndarray, indiv2: np.ndarray) -> list[np.ndarray]:
    new_indiv1 = np.copy(indiv1)
    new_indiv2 = np.copy(indiv2)
    for i in range(len(indiv1)):
        if np.random.uniform(0, 1) < 0.5:
            new_indiv1[i], new_indiv2[i] = new_indiv2[i], new_indiv1[i]
    return [new_indiv1, new_indiv2]
