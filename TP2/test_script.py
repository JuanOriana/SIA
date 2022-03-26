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
    chunked_generations = [5, 10, 30, 150, 450, 500]
    crossing_functions = {'simple_cross': simple_cross, 'double_cross': double_cross, 'rand_cross': rand_cross}
    selection_functions = {'elite_selection': elite_selection, 'roulette_selection': roulette_selection,
                           'boltzmann_selection': boltzmann_selection, 'truncated_selection': truncated_selection,
                           'rank_selection': rank_selection, 'tournament_selection': tournament_selection}

    # Generaciones : 500,800
    params = {"gen_size": default_gen_size,
              "max_generations": 500,
              "crossing_fun": crossing_functions["double_cross"],
              "selection_fun": selection_functions["tournament_selection"],
              "mutation_prob": default_mutation_prob,
              "mutation_std": default_mutation_std
              }

    # Medir :
    # gen_size_default 100 . mutation_prob_default = 0.09 , mutation_std=1
    # Crossing usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk)con rank y  roulete
    # gen_size mostrar como aumentar el gen_size no afecta linealemnte a la convergencia [16,64,128,256,512]
    # selection usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk) con simple_cross
    # mutation usando el chunked max_gens y con select fun (rank,roulete,boltzman) (0.01, 1)
    # mutation_std usando el chunked max_gens (0.1,4)
    # Boltzmann variando parametros de temparutra
    # Limited variando el k
    # Y tournament varios el umbral

    genetic_solver = GeneticSolver(gen_size=params["gen_size"], indiv_size=11,
                                   max_generations=params["max_generations"],
                                   crossing_fun=params["crossing_fun"],
                                   mutation_fun=mutate,
                                   selection_fun=params["selection_fun"], apitude_fun=loaded_aptitude,
                                   mutation_prob=params["mutation_prob"],
                                   mutation_std=params["mutation_std"], k=1, threshold=2)
    crossing_tests = {}
    names = chunked_generations

    # Crossing usando el chunked max_gens y dejando tod fijo  max_gen[5,5,10,30,450,500](con estos chunk)con rank y  roulete
    for select_fun in ['rank_selection','roulette_selection']:
        crossing_tests.update({select_fun:{}})
        genetic_solver.selection_fun = selection_functions[select_fun]
        for cross_func in crossing_functions:
            crossing_tests[select_fun].update({cross_func:list()})
            genetic_solver.crossing_fun = crossing_functions[cross_func]
            for i in chunked_generations:
                crossing_tests[select_fun][cross_func].append(genetic_solver.evolve_limited(i))


    print(crossing_tests)
    # for i in range(len(chunked_generations)):
    #     max_aptitudes.append(genetic_test[i][1])
    #
    # plt.suptitle("Generation change test")
    # plt.ylabel("Max aptitude")
    # plt.xlabel("Gen size")
    # plt.bar(names,max_aptitudes,width=8.0)
    # plt.axis([-1,550,2.0,3.0])
    # plt.show()
