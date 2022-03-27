import json
import runpy
import sys

import matplotlib.pyplot as plt

from TP2.data_structs.GeneticSolver import GeneticSolver
from TP2.genetic_solvers.crossing.crossing_algos import simple_cross, double_cross, rand_cross
from TP2.genetic_solvers.mutation.mutation_algo import mutate
from TP2.genetic_solvers.selection.selection_algos import elite_selection, roulette_selection, boltzmann_selection, \
    truncated_selection, tournament_selection, rank_selection
from TP2.utils.aptitude import aptitude, loaded_aptitude

if __name__ == '__main__':
    default_gen_size = 100
    default_mutation_prob = 0.09
    default_mutation_std = 1
    chunked_generations = [5, 10, 30,150]
    # chunked_generations = [5, 10]
    crossing_functions = {'simple_cross': simple_cross, 'double_cross': double_cross, 'rand_cross': rand_cross}
    selection_functions = {'elite_selection': elite_selection, 'roulette_selection': roulette_selection,
                           'boltzmann_selection': boltzmann_selection, 'truncated_selection': truncated_selection,
                           'rank_selection': rank_selection, 'tournament_selection': tournament_selection}

    # Medir :
    # gen_size_default 100 . mutation_prob_default = 0.09 , mutation_std=1
    # gen_size mostrar como aumentar el gen_size no afecta linealemnte a la convergencia [16,64,128,256,512]
    # Boltzmann variando parametros de temparutra
    # Y tournament varios el umbral
    genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
                                   max_generations=500,
                                   crossing_fun=crossing_functions["double_cross"],
                                   mutation_fun=mutate,
                                   selection_fun=selection_functions["tournament_selection"],
                                   apitude_fun=loaded_aptitude,
                                   mutation_prob=default_mutation_prob,
                                   mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
                                   decrease_factor=2)

    # Crossing usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk)con rank y  roulete
    crossing_tests = {}
    names = chunked_generations
    for select_fun in ['rank_selection', 'roulette_selection']:
        crossing_tests.update({select_fun: {}})
        genetic_solver.selection_fun = selection_functions[select_fun]
        for cross_func in crossing_functions:
            crossing_tests[select_fun].update({cross_func: list()})
            genetic_solver.crossing_fun = crossing_functions[cross_func]
            for i in chunked_generations:
                crossing_tests[select_fun][cross_func].append(genetic_solver.evolve_limited(i))
            genetic_solver.restart_solver()

    average_aptitudes = {}
    for select_fun in ['rank_selection', 'roulette_selection']:
        for cross_func in crossing_functions:
            average_aptitudes.update({cross_func: list()})
            for i in range(len(chunked_generations)):
                average_aptitudes[cross_func].append(crossing_tests[select_fun][cross_func][i][1])

            plt.suptitle("Generation change test " + select_fun + " y " + cross_func)
            plt.ylabel("AVG aptitude")
            plt.xlabel("Gen size")
            plt.bar(names, average_aptitudes[cross_func], width=8.0)
            plt.axis([-1, 520, 2.5, 3.0])
            plt.show()


    # selection usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk) con simple_cross
    selection_tests = {}
    genetic_solver.crossing_fun = crossing_functions['simple_cross']
    for select_fun in selection_functions:
        genetic_solver.selection_fun = selection_functions[select_fun]
        selection_tests.update({select_fun: list()})
        for i in chunked_generations:
            selection_tests[select_fun].append(genetic_solver.evolve_limited(i))
        genetic_solver.restart_solver()

    # mutation usando el chunked max_gens y con select fun (rank,roulete,boltzman) (0.01, 1)
    mutation_prob_tests = {}
    genetic_solver.crossing_fun = crossing_functions['simple_cross']
    for select_fun in [rank_selection, roulette_selection, boltzmann_selection]:
        mutation_prob_tests.update({select_fun: {}})
        for mutation_prob in [0.01, 1]:
            mutation_prob_tests[select_fun].update(({mutation_prob: list()}))
            genetic_solver.mutation_prob = mutation_prob
            for i in chunked_generations:
                mutation_prob_tests[select_fun][mutation_prob].append(genetic_solver.evolve_limited(i))
            genetic_solver.restart_solver()


    # mutation_std usando el chunked max_gens (0.1,4)
    mutation_std_tests = {}
    genetic_solver.selection_fun = selection_functions['elite_selection']

    for std in [0.1, 4]:
        mutation_std_tests.update({std: list()})
        for i in chunked_generations:
            mutation_std_tests[std].append(genetic_solver.evolve_limited(i))
        genetic_solver.restart_solver()

    # Limited variando el k ( ESTE TEST REVISARLO)
    truncated_k_test = {}
    genetic_solver.selection_fun = selection_functions['truncated_selection']
    genetic_solver.crossing_fun = crossing_functions['simple_cross']
    genetic_solver.mutation_prob = default_mutation_prob
    genetic_solver.mutation_std = default_mutation_std
    for i in chunked_generations:
        truncated_k_test.update({i: list()})
        for k in range(0, int(i / 2), int(i / 4)):
            genetic_solver.k = k
            truncated_k_test[i].append(genetic_solver.evolve_limited(i))
