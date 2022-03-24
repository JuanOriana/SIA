import numpy as np


def elite_selection(population, fitness_func):
    population.sort(key=fitness_func, reverse=True)
    return population[:len(population) // 2]


def roulette_selection(population, fitness_func):
    selection = []
    max = sum([fitness_func(c) for c in population])
    selection_probs = [fitness_func(c) / max for c in population]
    for i in range(len(population) // 2):
        selection.append(population[np.random.choice(len(population), p=selection_probs)])
    return selection


def truncated_selection(population, fitness_func, k):
    selection = []
    population.sort(key=fitness_func, reverse=True)
    visible_population = population[:len(population) - k]
    for i in range(len(population) // 2):
        selection.append(visible_population[np.random.choice(len(visible_population))])
    return selection


def boltzmann_selection(population, fitness_func, temp):
    new_fitness_func = lambda indiv: np.exp(fitness_func(indiv) / temp)
    return roulette_selection(population, new_fitness_func)


def rank_selection(population, fitness_func):
    selection = []
    population.sort(key=fitness_func, reverse=True)
    max = sum([idx+1 for idx,c in enumerate(population)])
    selection_probs = [(len(population) - idx) / max for idx,c in enumerate(population)]
    print(selection_probs)

    for i in range(len(population) // 2):
        selection.append(population[np.random.choice(len(population), p=selection_probs)])
    return selection

def tournament_selection(population, fitness_func):
    selection = []
    for i in range(len(population) // 2):
        indexes = np.random.choice(len(population),size=4,replace=False)
        winner_idx_1 = 0 if fitness_func(population[indexes[0]]) > fitness_func(population[indexes[1]]) else 1
        winner_idx_2 = 2 if fitness_func(population[indexes[2]]) > fitness_func(population[indexes[3]]) else 3
        winner_idx = winner_idx_1 if fitness_func(population[indexes[winner_idx_1]]) > fitness_func(population[indexes[winner_idx_2]]) else winner_idx_2
        selection.append(population[indexes[winner_idx]])
    return selection
