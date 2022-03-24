import numpy as np

from TP2.data_structs.Individual import Individual


def simple_cross(indiv1: Individual, indiv2: Individual) -> list[Individual]:
    indiv1_arr = indiv1.get_state()
    indiv2_arr = indiv2.get_state()
    change_idx = np.random.choice(len(indiv1_arr))
    new_indiv1_arr = np.copy(indiv1_arr)
    new_indiv2_arr = np.copy(indiv2_arr)
    new_indiv1_arr[change_idx:] = indiv2_arr[change_idx:]
    new_indiv2_arr[change_idx:] = indiv1_arr[change_idx:]
    return [Individual(new_indiv1_arr,indiv1.aptitude), Individual(new_indiv2_arr,indiv1.aptitude)]


def double_cross(indiv1: Individual, indiv2: Individual) -> list[Individual]:
    indiv1_arr = indiv1.get_state()
    indiv2_arr = indiv2.get_state()
    indexes = np.random.choice(len(indiv1_arr),size=2,replace=False)
    change_idx1 = indexes[0]
    change_idx2 = indexes[1]
    if change_idx1 > change_idx2:
        change_idx1, change_idx2 = change_idx2, change_idx1

    new_indiv1_arr = np.copy(indiv1_arr)
    new_indiv2_arr = np.copy(indiv2_arr)
    new_indiv1_arr[change_idx1:change_idx2 + 1] = indiv2_arr[change_idx1:change_idx2 + 1]
    new_indiv2_arr[change_idx1:change_idx2 + 1] = indiv1_arr[change_idx1:change_idx2 + 1]
    return [Individual(new_indiv1_arr,indiv1.aptitude), Individual(new_indiv2_arr,indiv1.aptitude)]


def rand_cross(indiv1: Individual, indiv2: Individual) -> list[Individual]:
    new_indiv1_arr = np.copy(indiv1.get_state())
    new_indiv2_arr = np.copy(indiv2.get_state())
    for i in range(len(new_indiv1_arr)):
        if np.random.uniform(0, 1) < 0.5:
            new_indiv1_arr[i], new_indiv2_arr[i] = new_indiv2_arr[i], new_indiv1_arr[i]
    return [Individual(new_indiv1_arr, indiv1.aptitude), Individual(new_indiv2_arr, indiv1.aptitude)]
