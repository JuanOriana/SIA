import numpy as np

from TP2.data_structs.GeneticSelectionParams import GeneticSelectionParams
from TP2.data_structs.Individual import Individual


class GeneticSolver():

    def __init__(self, gen_size: int, indiv_size: int, max_generations: int, crossing_fun,
                 mutation_fun, selection_fun, apitude_fun, mutation_prob, mutation_std, k=None, threshold=None,
                 inital_temp: float = None, change_factor: float = None, decrease_factor: float = None):
        self.gen_size = gen_size
        self.indiv_size = indiv_size
        self.max_generations = max_generations
        self.crossing_fun = crossing_fun
        self.mutation_fun = mutation_fun
        self.selection_fun = selection_fun
        self.aptitude_fun = apitude_fun
        self.current_gen_number = 0
        self.current_gen = self.init_gen()
        self.mutation_prob = mutation_prob
        self.mutation_std = mutation_std
        self.max_aptitude = -1
        self.avg_aptitude = -1
        self.max_individual = None
        # TODO: En vez de fijarnos si el nombre de la funcion es tal, pq no seteamos valores default para los parametros
        if selection_fun.__name__ == 'boltzmann_selection' and (
                k is None or threshold is None or inital_temp is None or change_factor is None or decrease_factor is None): raise Exception(
            "ERROR: Required parameters for boltzmann_selection are not passed.")
        self.selection_params = GeneticSelectionParams(k, threshold, inital_temp, change_factor, decrease_factor)

    def init_gen(self) -> list[Individual]:
        gen = []
        sum_apt = 0
        for i in range(self.gen_size):
            gen.append(Individual(np.random.rand(self.indiv_size), self.aptitude_fun))
            sum_apt += gen[-1].aptitude_concrete
        self.max_aptitude = max([indiv.aptitude_concrete for indiv in gen])
        self.avg_aptitude = sum_apt / self.gen_size;
        return gen

    def next_gen(self):
        if self.current_gen_number > self.max_generations:
            raise RuntimeError
        max = sum([c.aptitude_concrete for c in self.current_gen])
        selection_probs = [c.aptitude_concrete / max for c in self.current_gen]
        for i in range(self.gen_size // 2):
            indexes = np.random.choice(self.gen_size, p=selection_probs, size=2, replace=False)
            new_indivs = self.crossing_fun(self.current_gen[indexes[0]], self.current_gen[indexes[1]])
            self.current_gen.append(self.mutation_fun(new_indivs[0], self.mutation_prob, self.mutation_std))
            self.current_gen.append(self.mutation_fun(new_indivs[1], self.mutation_prob, self.mutation_std))
        self.selection_params.current_gen_number = self.current_gen_number
        self.current_gen = self.selection_fun(self.current_gen, self.gen_size, self.selection_params)
        sum_apt = 0
        max_apt = 0

        for indiv in self.current_gen:
            sum_apt += indiv.aptitude_concrete
            if indiv.aptitude_concrete > max_apt:
                self.max_individual = indiv
                max_apt = indiv.aptitude_concrete

        self.max_aptitude = max_apt
        self.avg_aptitude = sum_apt / self.gen_size

        self.current_gen_number += 1

    def evolve_limited(self, n):
        limit = min(self.current_gen_number + n, self.max_generations)
        while self.current_gen_number <= limit:
            self.next_gen()
        return self.max_aptitude, self.avg_aptitude, self.current_gen_number, self.max_individual

    def evolve(self):
        return self.evolve_limited(self.max_generations)

    def evolve_until_error_bound(self, error_bound):
        while abs(self.max_aptitude - 3) < error_bound:
            self.next_gen()
        return self.max_aptitude, self.avg_aptitude, self.current_gen_number, self.max_individual

    def restart_solver(self):
        self.avg_aptitude = -1
        self.max_aptitude = -1
        self.current_gen_number = 0
