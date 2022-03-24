import numpy as np
from TP2.genetic_solvers.crossing.crossing_algos import rand_cross
from TP2.genetic_solvers.mutation.mutation_algo import mutate
from TP2.genetic_solvers.selection.selection_algos import tournament_selection


def main():
    indiv1 = np.array([0.5, 0.3, 0.1, 1, 0.4])
    indiv2 = np.array([0.65, 0.35, 0.25, 0.05, 0.95])
    indiv3 = np.array([4, 8, 10, 0.05, 0.95])
    indiv4 = np.array([0.3, 8, 5, 0.05, 0.95])

    # print(rand_cross(indiv1, indiv2))
    print(tournament_selection([indiv1,indiv2,indiv3,indiv4],lambda indiv: sum(indiv)))

if __name__ == "__main__":
    main()
