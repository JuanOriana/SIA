import numpy as np

from TP2.data_structs.GeneticSelectionParams import GeneticSelectionParams
from TP2.data_structs.Individual import Individual


def elite_selection(population: list[Individual], size: int, selection_params: GeneticSelectionParams):
    population.sort(key=lambda indiv: indiv.aptitude_concrete, reverse=True)
    return population[:size]


# def roulette_selection(population: list[Individual], size):
#     selection = []
#     total_aptitude = sum([c.aptitude_concrete for c in population])
#     selection_probs = [c.aptitude_concrete / total_aptitude for c in population]
#     for i in range(size):
#         selection.append(np.random.choice(population, p=selection_probs))
#     return selection


def roulette_selection(population: list[Individual], size: int, selection_params: GeneticSelectionParams,
                       fitness_func=lambda indiv: indiv.aptitude_concrete):
    selection = []
    total_aptitude = sum([fitness_func(c) for c in population])
    selection_probs = [fitness_func(c) / total_aptitude for c in population]
    for i in range(size):
        selection.append(np.random.choice(population, p=selection_probs))
    return selection


def boltzmann_selection(population: list[Individual], size: int, selection_params: GeneticSelectionParams):
    temp = selection_params.gen_size
    return roulette_selection(population, size, selection_params,
                              fitness_func=lambda indiv: np.exp(indiv.aptitude(indiv) / temp))


# TODO: Ver como manejar los parametros desde geneticSolver para esta funcion
def boltzmann_temperature(initial_temp, change_factor, gen_num, decrease_factor):
    return change_factor + (initial_temp - change_factor) * np.exp(-decrease_factor * gen_num)


def truncated_selection(population: list[Individual], size: int, selection_params: GeneticSelectionParams):
    k = selection_params.k
    selection = []
    population.sort(key=lambda indiv: indiv.aptitude_concrete, reverse=True)
    visible_population = population[:len(population) - k]
    for i in range(size):
        selection.append(visible_population[np.random.choice(len(visible_population))])
    return selection


def rank_selection(population: list[Individual], size:int, selection_params: GeneticSelectionParams):
    selection = []
    population.sort(key=lambda indiv: indiv.aptitude_concrete, reverse=True)
    max = sum([idx + 1 for idx, c in enumerate(population)])
    selection_probs = [(len(population) - idx) / max for idx, c in enumerate(population)]
    for i in range(size):
        selection.append(np.random.choice(population, p=selection_probs))
    return selection


def tournament_selection(population: list[Individual], size:int, selection_params: GeneticSelectionParams):
    threshold = selection_params.threshold
    selection = []
    for i in range(size):
        picked = np.random.choice(len(population), size=4, replace=False)
        winner1 = choose_winner(population[picked[0]], population[picked[1]], threshold)
        winner2 = choose_winner(population[picked[2]], population[picked[3]], threshold)
        selection.append(choose_winner(winner1, winner2, threshold))
    return selection


def choose_winner(indiv1: Individual, indiv2: Individual, threshold: float):
    if indiv1.aptitude_concrete > indiv2.aptitude_concrete:
        best_indiv, worst_indiv = indiv1, indiv2
    else:
        best_indiv, worst_indiv = indiv2, indiv1

    r = np.random.uniform(0, 1)
    return best_indiv if r < threshold else worst_indiv
