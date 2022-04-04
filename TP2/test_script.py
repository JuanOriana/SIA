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
from TP2.utils.aptitude import loaded_aptitude

if __name__ == '__main__':
    default_gen_size = 50
    default_mutation_prob = 0.09
    default_mutation_std = 1
    runs = 5.0
    chunked_generations = np.array([5, 10, 35, 100, 150, 200])
    chunked_generations_positions = np.array([0.85, 1.85, 2.85, 3.85, 4.85, 5.85])
    chunked_generations_str = ['5', '15', '50', '150', '300', '500']
    colors = {'max apt': 'blue', 'avg apt': 'green'}

    # chunked_generations = [5, 10]
    crossing_functions = {'simple_cross': simple_cross, 'multiple_cross': double_cross, 'rand_cross': rand_cross}
    selection_functions = {'elite_selection': elite_selection, 'roulette_selection': roulette_selection,
                           'boltzmann_selection': boltzmann_selection, 'truncated_selection': truncated_selection,
                           'rank_selection': rank_selection, 'tournament_selection': tournament_selection}

    # Medir :
    # gen_size_default 100 . mutation_prob_default = 0.09 , mutation_std=1
    # gen_size mostrar como aumentar el gen_size no afecta linealemnte a la convergencia [16,64,128,256,512]
    # Boltzmann variando parametros de temparutra
    # genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                max_generations=500,
    #                                crossing_fun=crossing_functions["simple_cross"],
    #                                mutation_fun=mutate,
    #                                selection_fun=selection_functions["tournament_selection"],
    #                                apitude_fun=loaded_aptitude,
    #                                mutation_prob=default_mutation_prob,
    #                                mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
    #                                decrease_factor=2)
    #
    # # Crossing usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk)con rank y  roulete
    crossing_tests = {}
    max_aptitudes = {}
    average_aptitudes = {}
    # for run in range(int(runs)):
    #     crossing_tests.clear()
    #     for select_fun in ['roulette_selection']:
    #         crossing_tests.update({select_fun: {}})
    #         if run == 0: average_aptitudes.update({select_fun: {}})
    #         if run == 0: max_aptitudes.update({select_fun: {}})
    #         for cross_func in crossing_functions:
    #             crossing_tests[select_fun].update({cross_func: list()})
    #             if run == 0:average_aptitudes[select_fun].update({cross_func: list()})
    #             if run == 0:max_aptitudes[select_fun].update({cross_func: list()})
    #             genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                            max_generations=500,
    #                                            crossing_fun=crossing_functions[cross_func],
    #                                            mutation_fun=mutate,
    #                                            selection_fun=selection_functions[select_fun],
    #                                            apitude_fun=loaded_aptitude,
    #                                            mutation_prob=default_mutation_prob,
    #                                            mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
    #                                            decrease_factor=2)
    #             for i in range(500):
    #                 crossing_tests[select_fun][cross_func].append(genetic_solver.evolve_limited(1))
    #                 if run > 0:
    #                     average_aptitudes[select_fun][cross_func][i] += (crossing_tests[select_fun][cross_func][i][1])/runs
    #                     max_aptitudes[select_fun][cross_func][i] += (crossing_tests[select_fun][cross_func][i][0])/runs
    #                 else:
    #                     average_aptitudes[select_fun][cross_func].append(crossing_tests[select_fun][cross_func][i][1]/runs)
    #                     max_aptitudes[select_fun][cross_func].append(crossing_tests[select_fun][cross_func][i][0]/runs)
    #             genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                            max_generations=500,
    #                                            crossing_fun=crossing_functions[cross_func],
    #                                            mutation_fun=mutate,
    #                                            selection_fun=selection_functions[select_fun],
    #                                            apitude_fun=loaded_aptitude,
    #                                            mutation_prob=default_mutation_prob,
    #                                            mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
    #                                            decrease_factor=2)
    #
    # for select_fun in ['roulette_selection']:
    #     for cross_func in crossing_functions:
    #         plt.suptitle("Generation change test " + select_fun + " y " + cross_func)
    #         plt.ylabel("aptitude")
    #         plt.xlabel("Gen size")
    #         plt.plot(range(500), max_aptitudes[select_fun][cross_func],'bo', markersize=3)
    #         x1, x2, _, _ = plt.axis()
    #         plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #         labels = list(colors.keys())
    #         handles = [plt.Rectangle((0, 0), 0.2, 0,2, color=colors[label]) for label in labels]
    #         plt.legend(handles, labels)
    #         plt.show()


    # # selection usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk) con simple_cross
    # selection_tests = {}
    # max_aptitudes.clear()
    # average_aptitudes.clear()
    #
    # for run in range(int(runs)):
    #     selection_tests.clear()
    #     for select_fun in selection_functions:
    #         genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                        max_generations=500,
    #                                        crossing_fun=crossing_functions['simple_cross'],
    #                                        mutation_fun=mutate,
    #                                        selection_fun=selection_functions[select_fun],
    #                                        apitude_fun=loaded_aptitude,
    #                                        mutation_prob=default_mutation_prob,
    #                                        mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
    #                                        decrease_factor=2)
    #         selection_tests.update({select_fun: list()})
    #         if run == 0: average_aptitudes.update({select_fun: list()})
    #         if run == 0: max_aptitudes.update({select_fun: list()})
    #         for i in range(500):
    #             selection_tests[select_fun].append(genetic_solver.evolve_limited(1))
    #             if run > 0:
    #                 max_aptitudes[select_fun][i] += (selection_tests[select_fun][i][0]) / runs
    #                 average_aptitudes[select_fun][i] += (selection_tests[select_fun][i][1]) / runs
    #             else:
    #                 average_aptitudes[select_fun].append(selection_tests[select_fun][i][1] / runs)
    #                 max_aptitudes[select_fun].append(selection_tests[select_fun][i][0] / runs)
    #
    # for select_fun in selection_functions:
    #     plt.suptitle("Generation change test " + select_fun)
    #     plt.ylabel("AVG aptitude")
    #     plt.xlabel("Gen size")
    #     plt.plot(range(500), max_aptitudes[select_fun],'bo', markersize=3)
    #     x1, x2, _, _ = plt.axis()
    #     plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #     labels = list(colors.keys())
    #     handles = [plt.Rectangle((0, 0), 0.2, 0,2, color=colors[label]) for label in labels]
    #     plt.legend(handles, labels)
    #     plt.show()
    #
    # # # mutation usando el chunked max_gens y con select fun (rank,roulete,boltzman) (0.01, 1)
    # mutation_prob_tests = {}
    # max_aptitudes.clear()
    # average_aptitudes.clear()
    # for run in range(int(runs)):
    #     mutation_prob_tests.clear()
    #     for select_fun in ['roulette_selection']:
    #         mutation_prob_tests.update({select_fun: {}})
    #         if run == 0: average_aptitudes.update({select_fun: {}})
    #         if run == 0: max_aptitudes.update({select_fun: {}})
    #         for mutation_prob in [0.01,0.09, 0.5]:
    #             genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                            max_generations=500,
    #                                            crossing_fun=crossing_functions['simple_cross'],
    #                                            mutation_fun=mutate,
    #                                            selection_fun=selection_functions[select_fun],
    #                                            apitude_fun=loaded_aptitude,
    #                                            mutation_prob=mutation_prob,
    #                                            mutation_std=default_mutation_std, k=1, threshold=2, change_factor=1,
    #                                            decrease_factor=2)
    #             mutation_prob_tests[select_fun].update(({mutation_prob: list()}))
    #             if run == 0:
    #                 average_aptitudes[select_fun].update({mutation_prob: list()})
    #                 max_aptitudes[select_fun].update({mutation_prob: list()})
    #             for i in range(500):
    #                 mutation_prob_tests[select_fun][mutation_prob].append(
    #                     genetic_solver.evolve_limited(1))
    #                 if run > 0:
    #                     max_aptitudes[select_fun][mutation_prob][i] += (
    #                                 mutation_prob_tests[select_fun][mutation_prob][i][0] / runs)
    #                     average_aptitudes[select_fun][mutation_prob][i] += (
    #                                 mutation_prob_tests[select_fun][mutation_prob][i][1] / runs)
    #                 else:
    #                     average_aptitudes[select_fun][mutation_prob].append(
    #                         mutation_prob_tests[select_fun][mutation_prob][i][1] / runs)
    #                     max_aptitudes[select_fun][mutation_prob].append(
    #                         mutation_prob_tests[select_fun][mutation_prob][i][0] / runs)
    #
    # for select_fun in ['roulette_selection']:
    #     for mutation_prob in [0.01, 0.09,0.5]:
    #         plt.suptitle("Generation change test " + select_fun + " mutation prob:" + str(mutation_prob))
    #         plt.ylabel("aptitude")
    #         plt.xlabel("Gen size")
    #         plt.plot(range(500), max_aptitudes[select_fun][mutation_prob],'bo', markersize=3)
    #         x1, x2, _, _ = plt.axis()
    #         plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #         labels = list(colors.keys())
    #         handles = [plt.Rectangle((0, 0), 0.2, 0,2, color=colors[label]) for label in labels]
    #         plt.legend(handles, labels)
    #         plt.show()

    ##

    # mutation_std_tests = {}
    # max_aptitudes.clear()
    # average_aptitudes.clear()
    # # genetic_solver.selection_fun = selection_functions['elite_selection']
    # #
    # for run in range(int(runs)):
    #     mutation_std_tests.clear()
    #     for std in [0.01, 0.5, 4]:
    #         genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                        max_generations=500,
    #                                        crossing_fun=crossing_functions['simple_cross'],
    #                                        mutation_fun=mutate,
    #                                        selection_fun=selection_functions['rank_selection'],
    #                                        apitude_fun=loaded_aptitude,
    #                                        mutation_prob=default_mutation_prob,
    #                                        mutation_std=std, k=1, threshold=2, change_factor=1,
    #                                        decrease_factor=2)
    #         mutation_std_tests.update({std: list()})
    #         if run == 0:
    #             average_aptitudes.update({std: list()})
    #             max_aptitudes.update({std: list()})
    #
    #         for i in range(500):
    #             mutation_std_tests[std].append(genetic_solver.evolve_limited(1))
    #             if run > 0:
    #                 max_aptitudes[std][i] += (
    #                             mutation_std_tests[std][i][0] / runs)
    #                 average_aptitudes[std][i] += (
    #                             mutation_std_tests[std][i][1] / runs)
    #             else:
    #                 average_aptitudes[std].append(
    #                     mutation_std_tests[std][i][1] / runs)
    #                 max_aptitudes[std].append(
    #                     mutation_std_tests[std][i][0] / runs)
    #
    #
    # for std in [0.01, 0.5, 4]:
    #     plt.suptitle("Generation change test mutation std:" + str(std))
    #     plt.ylabel("aptitude")
    #     plt.xlabel("Gen size")
    #     plt.plot(range(500), max_aptitudes[std],'bo', markersize=3)
    #     x1, x2, _, _ = plt.axis()
    #     plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #     labels = list(colors.keys())
    #     handles = [plt.Rectangle((0, 0), 0.2, 0, 2, color=colors[label]) for label in labels]
    #     plt.legend(handles, labels)
    #     plt.show()

    # Limited variando el k ( Por alguna razon esta fallando el truncate la segunda vez)
    #
    # truncated_k_test = {}
    # max_aptitudes.clear()
    # average_aptitudes.clear()
    #
    # for run in range(int(runs)):
    #     truncated_k_test.clear()
    #     for k in [0,int(default_gen_size/10),int(default_gen_size/6),int(default_gen_size/2)]:
    #         genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                        max_generations=500,
    #                                        crossing_fun=crossing_functions['simple_cross'],
    #                                        mutation_fun=mutate,
    #                                        selection_fun=selection_functions['truncated_selection'],
    #                                        apitude_fun=loaded_aptitude,
    #                                        mutation_prob=default_mutation_prob,
    #                                        mutation_std=default_mutation_std, k=k, threshold=2, change_factor=1,
    #                                        decrease_factor=2)
    #         truncated_k_test.update({k: {}})
    #         if run == 0:
    #             average_aptitudes.update({k: list()})
    #             max_aptitudes.update({k: list()})
    #         for i in range(500):
    #             truncated_k_test[k].update({i: genetic_solver.evolve_limited(1)})
    #             if run == 0:
    #                 max_aptitudes[k].append(truncated_k_test[k][i][0] / runs)
    #                 average_aptitudes[k].append(truncated_k_test[k][i][1] / runs)
    #             else:
    #                 max_aptitudes[k][i] += (truncated_k_test[k][i][0] / runs)
    #                 average_aptitudes[k][i]+= (truncated_k_test[k][i][1] / runs)
    #
    # for k in [0, int(default_gen_size / 10), int(default_gen_size / 6), int(default_gen_size / 2)]:
    #     plt.suptitle("Generation change test chunked size:" + str(k))
    #     plt.ylabel("aptitude")
    #     plt.xlabel("Gen size")
    #     plt.plot(range(500), max_aptitudes[k],'bo', markersize=3)
    #     x1, x2, _, _ = plt.axis()
    #     plt.axis([x1, x2, 6.50, 9.0])
    #     plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #     plt.show()

    # tournament varios el umbral
    # tournament_test = {}
    # average_aptitudes.clear()
    # max_aptitudes.clear()
    # for run in range(int(runs)):
    #     tournament_test.clear()
    #     for threshold in [0.5,0.75, 0.9]:
    #         best_err = 0
    #         genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                        max_generations=500,
    #                                        crossing_fun=crossing_functions['simple_cross'],
    #                                        mutation_fun=mutate,
    #                                        selection_fun=selection_functions['tournament_selection'],
    #                                        apitude_fun=loaded_aptitude,
    #                                        mutation_prob=default_mutation_prob,
    #                                        mutation_std=default_mutation_std, threshold=threshold)
    #         tournament_test.update({threshold: list()})
    #         if run == 0:
    #             average_aptitudes.update({threshold: list()})
    #             max_aptitudes.update({threshold: list()})
    #         for i in range(500):
    #             tournament_test[threshold].append(genetic_solver.evolve_limited(1))
    #             if run == 0:
    #                 max_aptitudes[threshold].append((tournament_test[threshold][i][0] / runs))
    #                 average_aptitudes[threshold].append(tournament_test[threshold][i][1] / runs)
    #             else:
    #                 max_aptitudes[threshold][i] += (tournament_test[threshold][i][0] / runs)
    #                 average_aptitudes[threshold][i] += (tournament_test[threshold][i][1] / runs)
    
    # for threshold in [0.5,0.75, 0.9]:
    #     plt.suptitle("Generation change test tournament distinct thresholds:" + str(threshold))
    #     plt.ylabel("aptitude")
    #     plt.xlabel("Gen size")
    #     plt.plot(range(500), max_aptitudes[threshold],'bo', markersize=3)
    #     x1, x2, _, _ = plt.axis()
    #     plt.axis([x1, x2, 2.0, 9.0])
    #     plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #     plt.show()


    ## Boltzman variando la temp inicial

    #
    # boltzman_test = {}
    # max_aptitudes.clear()
    # average_aptitudes.clear()
    #
    # for initial_temp in [5, 10, 20, 30, 50]:
    #     boltzman_test.update({initial_temp: list()})
    #     max_aptitudes.update({initial_temp:  list()})
    #     average_aptitudes.update({initial_temp:  list()})
    #     genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                    max_generations=500,
    #                                    crossing_fun=crossing_functions["simple_cross"],
    #                                    mutation_fun=mutate,
    #                                    selection_fun=selection_functions['boltzmann_selection'],
    #                                    apitude_fun=loaded_aptitude,
    #                                    mutation_prob=default_mutation_prob,
    #                                    mutation_std=default_mutation_std, change_factor=10,
    #                                    decrease_factor=0.5, inital_temp=initial_temp)
    #     for i in range(500):
    #         boltzman_test[initial_temp].append(genetic_solver.evolve_limited(1))
    #         max_aptitudes[initial_temp].append(boltzman_test[initial_temp][i][0])
    #         average_aptitudes[initial_temp].append(boltzman_test[initial_temp][i][1])
    #
    # for initial_temp in [5, 10, 20, 30, 50]:
    #     plt.suptitle("Generation change test Boltzman distinct initial_temp:" + str(initial_temp))
    #     plt.ylabel("aptitude")
    #     plt.xlabel("Gen size")
    #     plt.plot(range(500), max_aptitudes[initial_temp],'bo', markersize=3)
    #     plt.plot(range(500), average_aptitudes[initial_temp],'gx', markersize=3)
    #     x1, x2, _, _ = plt.axis()
    #     labels = list(colors.keys())
    #     handles = [plt.Rectangle((0, 0), 0.2, 0, 2, color=colors[label]) for label in labels]
    #     plt.legend(handles, labels)
    #     plt.axis([x1, x2, 2.0, 9.0])
    #     plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #     plt.show()

    # ## Boltzman variando el factor de decrecimiento
    #
    # boltzman_test.clear()
    # max_aptitudes.clear()
    # average_aptitudes.clear()
    # for decrease_factor in [1, 0.5 , 0.1]:
    #     boltzman_test.update({decrease_factor: list()})
    #     max_aptitudes.update({decrease_factor: list()})
    #     average_aptitudes.update({decrease_factor: list()})
    #     genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                    max_generations=500,
    #                                    crossing_fun=crossing_functions["simple_cross"],
    #                                    mutation_fun=mutate,
    #                                    selection_fun=selection_functions['boltzmann_selection'],
    #                                    apitude_fun=loaded_aptitude,
    #                                    mutation_prob=default_mutation_prob,
    #                                    mutation_std=default_mutation_std, change_factor=10,
    #                                    decrease_factor=decrease_factor, inital_temp=10)
    #     for i in range(500):
    #         boltzman_test[decrease_factor].append(genetic_solver.evolve_limited(1))
    #         max_aptitudes[decrease_factor].append(boltzman_test[decrease_factor][i][0])
    #         average_aptitudes[decrease_factor].append(boltzman_test[decrease_factor][i][1])
    #
    # for decrease_factor in [1, 0.5 , 0.1]:
    #     plt.suptitle("Generation change test Boltzman distinct decrease_factor:" + str(decrease_factor))
    #     plt.ylabel("aptitude")
    #     plt.xlabel("Gen size")
    #     plt.plot(range(500), max_aptitudes[decrease_factor],'bo', markersize=3)
    #     plt.plot(range(500), average_aptitudes[decrease_factor],'gx', markersize=3)
    #     x1, x2, _, _ = plt.axis()
    #     labels = list(colors.keys())
    #     handles = [plt.Rectangle((0, 0), 0.2, 0, 2, color=colors[label]) for label in labels]
    #     plt.legend(handles, labels)
    #     plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #     plt.show()
    #
    # ## Boltzman variando el factor de cambio
    # boltzman_test.clear()
    # max_aptitudes.clear()
    # average_aptitudes.clear()
    # for change_factor in [10, 20, 50]:
    #     boltzman_test.update({change_factor: list()})
    #     max_aptitudes.update({change_factor: list()})
    #     average_aptitudes.update({change_factor: list()})
    #     genetic_solver = GeneticSolver(gen_size=default_gen_size, indiv_size=11,
    #                                    max_generations=500,
    #                                    crossing_fun=crossing_functions["simple_cross"],
    #                                    mutation_fun=mutate,
    #                                    selection_fun=selection_functions['boltzmann_selection'],
    #                                    apitude_fun=loaded_aptitude,
    #                                    mutation_prob=default_mutation_prob,
    #                                    mutation_std=default_mutation_std, change_factor=change_factor,
    #                                    decrease_factor=0.5, inital_temp=10)
    #     for i in range(500):
    #         boltzman_test[change_factor].append(genetic_solver.evolve_limited(1))
    #         max_aptitudes[change_factor].append(boltzman_test[change_factor][i][0])
    #         average_aptitudes[change_factor].append(boltzman_test[change_factor][i][1])
    #
    # for change_factor in [10, 20, 50]:
    #     plt.suptitle("Generation change test Boltzman distinct change_factor:" + str(change_factor))
    #     plt.ylabel("aptitude")
    #     plt.xlabel("Gen size")
    #     plt.plot(range(500), max_aptitudes[change_factor],'bo', markersize=3)
    #     plt.plot(range(500), average_aptitudes[change_factor],'gx', markersize=3)
    #     plt.bar(chunked_generations_positions, average_aptitudes[change_factor], color='g', width=0.3,
    #             align='center')
    #     x1, x2, _, _ = plt.axis()
    #     labels = list(colors.keys())
    #     handles = [plt.Rectangle((0, 0), 0.2, 0, 2, color=colors[label]) for label in labels]
    #     plt.legend(handles, labels)
    #     plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
    #     plt.show()

    gen_size_test = {}
    max_aptitudes.clear()
    average_aptitudes.clear()

    for run in range(int(runs)):
        gen_size_test.clear()
        for gen_size_iter in [8, 16, 64, 128]:
            gen_size_test.update({gen_size_iter:{}})
            if run ==0: average_aptitudes.update({gen_size_iter: {}})
            if run ==0:  max_aptitudes.update({gen_size_iter: {}})
            for select_fun in ['rank_selection']:
                gen_size_test[gen_size_iter].update({select_fun: list()})
                if run == 0: average_aptitudes[gen_size_iter].update({select_fun:list()})
                if run == 0: max_aptitudes[gen_size_iter].update({select_fun: list()})
                genetic_solver = GeneticSolver(gen_size=gen_size_iter, indiv_size=11,
                                               max_generations=500,
                                               crossing_fun=crossing_functions["simple_cross"],
                                               mutation_fun=mutate,
                                               selection_fun=selection_functions[select_fun],
                                               apitude_fun=loaded_aptitude,
                                               mutation_prob=default_mutation_prob,
                                               mutation_std=default_mutation_std)
                for i in range(500):
                    gen_size_test[gen_size_iter][select_fun].append(genetic_solver.evolve_limited(1))
                    if run == 0:
                        max_aptitudes[gen_size_iter][select_fun].append((gen_size_test[gen_size_iter][select_fun][i][0] / runs))
                        average_aptitudes[gen_size_iter][select_fun].append(gen_size_test[gen_size_iter][select_fun][i][1] / runs)
                    else:
                        max_aptitudes[gen_size_iter][select_fun][i] += (gen_size_test[gen_size_iter][select_fun][i][0] / runs)
                        average_aptitudes[gen_size_iter][select_fun][i] += (gen_size_test[gen_size_iter][select_fun][i][1] / runs)

    for gen_size_iter in [8,16, 64, 128]:
        for select_fun in ['rank_selection']:
            plt.suptitle("Generation change test " + select_fun + " distinct gen_size:" + str(gen_size_iter))
            plt.ylabel("aptitude")
            plt.xlabel("Gen size")
            plt.plot(range(500),max_aptitudes[gen_size_iter][select_fun],'bo',markersize=3)
            plt.plot(range(500),average_aptitudes[gen_size_iter][select_fun],'rx',markersize=3)
            x1, x2, _, _ = plt.axis()
            labels = list(colors.keys())
            handles = [plt.Rectangle((0, 0), 0.2, 0, 2, color=colors[label]) for label in labels]
            plt.legend(handles, labels)
            plt.xticks(np.array([1, 2, 3, 4, 5, 6]), chunked_generations_str)
            plt.show()




