import numpy as np

from TP2.data_structs.GeneticSolver import GeneticSolver
import sys

from TP2.utils.aptitude import  test_cases, aproximation_error
from TP2.utils.parameters import Parameters


def main():
    if len(sys.argv) != 2:
        print("Invalid usage: main.py <config.json>")
        quit(1)
    np.set_printoptions(precision=20)
    # indiv1_arr = np.array([0.51, 0.31, 0.11, 1.1, 6.41, 1.11, 3.11, 1.91, 2.51, 0.21, 0.31])
    # indiv2_arr = np.array([2.62, 4.32, 1.22, 5.02, 1.92, 0.62, 0.72, 0.52, 1.12, 0.22, 0.32])
    # indiv3_arr = np.array([4.13, 8.23, 1.23, 1.03, 0.93, 3.23, 0.33, 0.73, 0.13, 0.23, 5.33])
    # indiv4_arr = np.array([1.14, 3.24, 5.24, 2.04, 1.94, 3.24, 1.34, 2.44, 1.24, 1.24, 5.34])
    #
    # indiv1 = Individual(indiv1_arr, loaded_aptitude)
    # indiv2 = Individual(indiv2_arr, loaded_aptitude)
    # indiv3 = Individual(indiv3_arr, loaded_aptitude)
    # indiv4 = Individual(indiv4_arr, loaded_aptitude)
    #
    # population = [indiv1, indiv2, indiv3, indiv4]
    #
    # print("Crossings")
    # print("simple")
    # print(simple_cross(indiv1, indiv2))
    # print()
    # print("cross")
    # print(multi_point(indiv1, indiv2,1))
    # print()
    # print("rand")
    # print(rand_cross(indiv1, indiv2))
    # print()
    #
    # print("Mutation")
    # print(mutate(indiv1, 0.5, 1))
    # print()
    #
    # print("Selection")
    # print("elite")
    # print(elite_selection(population, 2))
    # print()
    # print("roulete")
    # print(roulette_selection(population, 2))
    #
    # print("trouncate")
    # print(truncated_selection(population, 2, 1))
    #
    # print("rank")
    # print(rank_selection(population, 2))
    #
    # print("torunament")
    # print(tournament_selection(population, 2))

    # print(rand_cross(indiv1, indiv2))
    # print(tournament_selection([indiv1, indiv2, indiv3, indiv4], lambda indiv: sum(indiv)))

    # values = Parameters(sys.argv[1])
    # genetic_solver = GeneticSolver(gen_size=values.gen_size, indiv_size=11, max_generations=values.max_generations,
    #                                crossing_fun=values.crossing_fun,
    #                                mutation_fun=values.mutation_fun,
    #                                selection_fun=values.selection_fun, apitude_fun=values.aptitude_fun,
    #                                mutation_prob=values.mutation_prob,
    #                                mutation_std=values.mutation_std, k=4, threshold=0.7)
    # print("PARAMS:")
    # print("Gen size: "  +str(values.gen_size))
    # print("Max generations: "  +str(values.max_generations))
    # print("Crossing function: "  + values.crossing_fun.__name__)
    # print("Mutation function: "  + values.mutation_fun.__name__)
    # print("Selection function: "  + values.selection_fun.__name__)
    # print("Mutation probability: "  + str(values.mutation_prob))
    # print("Mutation deviation: "  + str(values.mutation_std))
    # print("\nThinking... \n")
    # max_apt, avg_apt, gen, max_indiv = genetic_solver.evolve()
    # print("Finished at generation: " + str(gen - 1))
    # print("The average aptitude at this generation was: " + avg_apt.astype(str))
    # print("The max aptitude at this generation was: " + max_apt.astype(str))
    # print("And it was obtained by: " + str(max_indiv))
    # print("The error for this individual was: " + str(aproximation_error(max_indiv,test_cases)))

    indiv_array = np.array([19.865102716912013 ,  27.10497507637139  ,  -4.639569819307013 ,  9.343331351438735  ,  2.5127792403584808 , 18.255298281126784,1.4844877845080662 , -2.7511366088017972  , 8.040562193920996 ,0.30709847960449843 , 1.7230177710634145 ])


if __name__ == "__main__":
    main()
