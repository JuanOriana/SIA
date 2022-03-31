import numpy as np

from TP2.data_structs.Individual import Individual


# can be done as multi_point(indiv1,indiv2,1), but this performs better
def simple_cross(indiv1: Individual, indiv2: Individual) -> list[Individual]:
    indiv1_arr = indiv1.get_state()
    indiv2_arr = indiv2.get_state()
    change_idx = np.random.choice(len(indiv1_arr))
    new_indiv1_arr = np.copy(indiv1_arr)
    new_indiv2_arr = np.copy(indiv2_arr)
    new_indiv1_arr[change_idx:] = indiv2_arr[change_idx:]
    new_indiv2_arr[change_idx:] = indiv1_arr[change_idx:]
    return [Individual(new_indiv1_arr, indiv1.aptitude), Individual(new_indiv2_arr, indiv1.aptitude)]


def multi_point(indiv1: Individual, indiv2: Individual, points: int) -> list[Individual]:
    indiv1_arr = indiv1.get_state()
    indiv2_arr = indiv2.get_state()
    indexes = np.random.choice(len(indiv1_arr), size=points, replace=False)
    indexes.sort()
    new_indiv1_arr = np.copy(indiv1_arr)
    new_indiv2_arr = np.copy(indiv2_arr)
    for i in range(0, len(indexes) - 1, 2):
        change_idx1 = indexes[i]
        change_idx2 = indexes[i + 1]
        new_indiv1_arr[change_idx1:change_idx2 + 1] = indiv2_arr[change_idx1:change_idx2 + 1]
        new_indiv2_arr[change_idx1:change_idx2 + 1] = indiv1_arr[change_idx1:change_idx2 + 1]

    # If points are odd, we swap the last chunk
    if points % 2 == 1:
        change_idx1 = indexes[-1]
        change_idx2 = len(indiv1_arr) - 1

        new_indiv1_arr[change_idx1:change_idx2 + 1] = indiv2_arr[change_idx1:change_idx2 + 1]
        new_indiv2_arr[change_idx1:change_idx2 + 1] = indiv1_arr[change_idx1:change_idx2 + 1]

    return [Individual(new_indiv1_arr, indiv1.aptitude), Individual(new_indiv2_arr, indiv1.aptitude)]


def double_cross(indiv1: Individual, indiv2: Individual) -> list[Individual]:
    return multi_point(indiv1, indiv2, 2)


def rand_cross(indiv1: Individual, indiv2: Individual) -> list[Individual]:
    new_indiv1_arr = np.copy(indiv1.get_state())
    new_indiv2_arr = np.copy(indiv2.get_state())
    for i in range(len(new_indiv1_arr)):
        if np.random.uniform(0, 1) < 0.5:
            new_indiv1_arr[i], new_indiv2_arr[i] = new_indiv2_arr[i], new_indiv1_arr[i]
    return [Individual(new_indiv1_arr, indiv1.aptitude), Individual(new_indiv2_arr, indiv1.aptitude)]
