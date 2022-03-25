import numpy as np

from TP2.data_structs.Individual import Individual


def elite_selection(population: list[Individual], size):
    population.sort(key=lambda indiv: indiv.aptitude_concrete, reverse=True)
    return population[:size]


# def roulette_selection(population: list[Individual], size):
#     selection = []
#     total_aptitude = sum([c.aptitude_concrete for c in population])
#     selection_probs = [c.aptitude_concrete / total_aptitude for c in population]
#     for i in range(size):
#         selection.append(np.random.choice(population, p=selection_probs))
#     return selection


def roulette_selection(population: list[Individual], size, fitness_func=lambda indiv: indiv.aptitude_concrete):
    selection = []
    total_aptitude = sum([fitness_func(c) for c in population])
    selection_probs = [fitness_func(c) / total_aptitude for c in population]
    for i in range(size):
        selection.append(np.random.choice(population, p=selection_probs))
    return selection


def boltzmann_selection(population: list[Individual], size, temp):
    return roulette_selection(population, size, fitness_func=lambda indiv: np.exp(indiv.aptitude(indiv) / temp))


# TODO: Ver como manejar los parametros desde geneticSolver para esta funcion
def boltzmann_temperature(initial_temp, change_factor, gen_num, decrease_factor):
    return change_factor + (initial_temp - change_factor) * np.exp(-decrease_factor * gen_num)


def truncated_selection(population: list[Individual], size, k):
    selection = []
    population.sort(key=lambda indiv: indiv.aptitude_concrete, reverse=True)
    visible_population = population[:len(population) - k]
    for i in range(size):
        selection.append(visible_population[np.random.choice(len(visible_population))])
    return selection


def rank_selection(population: list[Individual], size):
    selection = []
    population.sort(key=lambda indiv: indiv.aptitude_concrete, reverse=True)
    max = sum([idx + 1 for idx, c in enumerate(population)])
    selection_probs = [(len(population) - idx) / max for idx, c in enumerate(population)]
    for i in range(size):
        selection.append(np.random.choice(population, p=selection_probs))
    return selection


def tournament_selection(population: list[Individual], size):
    selection = []
    for i in range(size):
        indexes = np.random.choice(len(population), size=4, replace=False)
        winner_idx_1 = 0 if population[indexes[0]].aptitude_concrete > population[indexes[1]].aptitude_concrete else 1
        winner_idx_2 = 2 if population[indexes[2]].aptitude_concrete > population[indexes[3]].aptitude_concrete else 3
        winner_idx = winner_idx_1 if population[indexes[winner_idx_1]].aptitude_concrete > population[
            indexes[winner_idx_2]].aptitude_concrete else winner_idx_2
        selection.append(population[indexes[winner_idx]])
    return selection
