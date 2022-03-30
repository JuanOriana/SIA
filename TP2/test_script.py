import json
import runpy
import sys

import matplotlib.pyplot as plt
import numpy as np
from TP2.data_structs.GeneticSolver import GeneticSolver
from TP2.genetic_solvers.crossing.crossing_algos import simple_cross, double_cross, rand_cross
from TP2.genetic_solvers.mutation.mutation_algo import mutate
from TP2.genetic_solvers.selection.selection_algos import elite_selection, roulette_selection, boltzmann_selection, \
    truncated_selection, tournament_selection, rank_selection
from TP2.utils.aptitude import aptitude, loaded_aptitude

if __name__ == '__main__':
    default_gen_size = 50
    default_mutation_prob = 0.09
    default_mutation_std = 1
    runs = 3.0
    chunked_generations = np.array([5, 10, 30, 105, 150, 200])
    chunked_generations_positions = np.array([0.85, 1.85, 2.85, 3.85, 4.85, 5.85])
    chunked_generations_str = ['5', '15', '45', '150', '300', '500']

    # chunked_generations = [5, 10]
    crossing_functions = {'simple_cross': simple_cross, 'rand_cross': rand_cross}
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
                                   crossing_fun=crossing_functions["simple_cross"],
                                   mutation_fun=mutate,
                                   selection_fun=selection_functions["tournament_selection"],
                                   apitude_fun=loaded_aptitude,
                                   mutation_prob=default_mutation_prob,
                                   mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
                                   decrease_factor=2)

    # Crossing usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk)con rank y  roulete
    crossing_tests = {}
    max_aptitudes = {}
    average_aptitudes = {}
    # for run in range(runs):
    #     crossing_tests.clear()
    #     # for select_fun in ['rank_selection', 'roulette_selection']:
    #     for select_fun in ['rank_selection']:
    #         crossing_tests.update({select_fun: {}})
    #         genetic_solver.selection_fun = selection_functions[select_fun]
    #         for cross_func in crossing_functions:
    #             if run == 0:average_aptitudes.update({cross_func: list()})
    #             if run == 0:max_aptitudes.update({cross_func: list()})
    #             crossing_tests[select_fun].update({cross_func: list()})
    #             genetic_solver.crossing_fun = crossing_functions[cross_func]
    #             for i in range(len(chunked_generations)):
    #                 crossing_tests[select_fun][cross_func].append(genetic_solver.evolve_limited(chunked_generations[i]))
    #                 if run > 0:
    #                     average_aptitudes[cross_func][i] += (crossing_tests[select_fun][cross_func][i][1])/runs
    #                     max_aptitudes[cross_func][i] += (crossing_tests[select_fun][cross_func][i][0])/runs
    #                 else:
    #                     average_aptitudes[cross_func].append(crossing_tests[select_fun][cross_func][i][1]/runs)
    #                     max_aptitudes[cross_func].append(crossing_tests[select_fun][cross_func][i][0]/runs)
    #             genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                            max_generations=500,
    #                                            crossing_fun=crossing_functions[cross_func],
    #                                            mutation_fun=mutate,
    #                                            selection_fun=selection_functions[select_fun],
    #                                            apitude_fun=loaded_aptitude,
    #                                            mutation_prob=default_mutation_prob,
    #                                            mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
    #                                            decrease_factor=2)

    for select_fun in ['rank_selection']:
        for cross_func in crossing_functions:
            plt.suptitle("Generation change test " + select_fun + " y " + cross_func)
            plt.ylabel("AVG aptitude")
            plt.xlabel("Gen size")
            plt.bar(chunked_generations_positions + 0.3, max_aptitudes[cross_func], color='b', width=0.3,
                    align='center')
            plt.bar(chunked_generations_positions, average_aptitudes[cross_func], color='g', width=0.3, align='center')
            x1, x2, _, _ = plt.axis()
            plt.axis([x1, x2, 2.0, 3.0])
            plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
            plt.show()
    #
    #
    # # selection usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk) con simple_cross
    selection_tests = {}
    max_aptitudes.clear()
    average_aptitudes.clear()

    for run in range(int(runs)):
        selection_tests.clear()
        for select_fun in selection_functions:
            genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
                                           max_generations=500,
                                           crossing_fun=crossing_functions['simple_cross'],
                                           mutation_fun=mutate,
                                           selection_fun=selection_functions[select_fun],
                                           apitude_fun=loaded_aptitude,
                                           mutation_prob=default_mutation_prob,
                                           mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
                                           decrease_factor=2)
            selection_tests.update({select_fun: list()})
            if run == 0: average_aptitudes.update({select_fun: list()})
            if run == 0: max_aptitudes.update({select_fun: list()})
            for i in range(len(chunked_generations)):
                selection_tests[select_fun].append(genetic_solver.evolve_limited(chunked_generations[i]))
                if run > 0:
                    max_aptitudes[select_fun][i] += (selection_tests[select_fun][i][0]) / runs
                    average_aptitudes[select_fun][i] += (selection_tests[select_fun][i][1]) / runs
                else:
                    average_aptitudes[select_fun].append(selection_tests[select_fun][i][1] / runs)
                    max_aptitudes[select_fun].append(selection_tests[select_fun][i][0] / runs)

    for select_fun in selection_functions:
        plt.suptitle("Generation change test " + select_fun)
        plt.ylabel("AVG aptitude")
        plt.xlabel("Gen size")
        plt.bar(chunked_generations_positions + 0.3, max_aptitudes[select_fun], color='b', width=0.3,
                align='center')
        plt.bar(chunked_generations_positions, average_aptitudes[select_fun], color='g', width=0.3, align='center')
        x1, x2, _, _ = plt.axis()
        plt.axis([x1, x2, 2.0, 3.0])
        plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
        plt.show()
    #
    # # mutation usando el chunked max_gens y con select fun (rank,roulete,boltzman) (0.01, 1)
    # mutation_prob_tests = {}
    # genetic_solver.crossing_fun = crossing_functions['simple_cross']
    # for select_fun in [rank_selection, roulette_selection, boltzmann_selection]:
    #     mutation_prob_tests.update({select_fun: {}})
    #     for mutation_prob in [0.01, 1]:
    #         mutation_prob_tests[select_fun].update(({mutation_prob: list()}))
    #         genetic_solver.mutation_prob = mutation_prob
    #         for i in chunked_generations:
    #             mutation_prob_tests[select_fun][mutation_prob].append(genetic_solver.evolve_limited(i))
    #         genetic_solver.restart_solver()
    #
    #
    # # mutation_std usando el chunked max_gens (0.1,4)
    # mutation_std_tests = {}
    # genetic_solver.selection_fun = selection_functions['elite_selection']
    #
    # for std in [0.1, 4]:
    #     mutation_std_tests.update({std: list()})
    #     for i in chunked_generations:
    #         mutation_std_tests[std].append(genetic_solver.evolve_limited(i))
    #     genetic_solver.restart_solver()
    #
    # # Limited variando el k ( ESTE TEST REVISARLO)
    # truncated_k_test = {}
    # genetic_solver.selection_fun = selection_functions['truncated_selection']
    # genetic_solver.crossing_fun = crossing_functions['simple_cross']
    # genetic_solver.mutation_prob = default_mutation_prob
    # genetic_solver.mutation_std = default_mutation_std
    # for i in chunked_generations:
    #     truncated_k_test.update({i: list()})
    #     for k in range(0, int(i / 2), int(i / 4)):
    #         genetic_solver.k = k
    #         truncated_k_test[i].append(genetic_solver.evolve_limited(i))
