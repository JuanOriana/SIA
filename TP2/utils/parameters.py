import json

from TP2.genetic_solvers.crossing.crossing_algos import simple_cross, double_cross, rand_cross
from TP2.genetic_solvers.mutation.mutation_algo import mutate
from TP2.genetic_solvers.selection.selection_algos import elite_selection, roulette_selection, boltzmann_selection, truncated_selection, rank_selection, tournament_selection
from TP2.utils.aptitude import loaded_aptitude

crossing_functions = { 'simple_cross':simple_cross, 'double_cross':double_cross, 'rand_cross':rand_cross }
selection_functions = { 'elite_selection':elite_selection , 'roulette_selection':roulette_selection , 'boltzmann_selection':boltzmann_selection , 'truncated_selection':truncated_selection , 'rank_selection':rank_selection , 'tournament_selection':tournament_selection }

class Parameters(object):

    def __init__(self, input_json_file_name):
        self.mutation_std = None
        self.mutation_prob = None
        self.aptitude_fun = None
        self.selection_fun = None
        self.mutation_fun = None
        self.crossing_fun = None
        self.gen_size = None
        self.max_generations = None
        self.from_json(input_json_file_name)

    def load_parameters(self, gen_size, max_generations, crossing_fun, selection_fun, mutation_prob, mutation_std):
        if not gen_size: raise Exception("ERROR: A generation size must be defined.")
        elif not max_generations: raise Exception("ERROR: A maximum number of generation must be defined.")
        elif not mutation_prob: raise Exception("ERROR: A mutation probability must be defined.")
        elif not mutation_std: raise Exception("ERROR: A mutation standard distribution must be defined.")
        else:
            self.gen_size = gen_size
            self.max_generations = max_generations
            if not crossing_functions.__contains__(crossing_fun): raise Exception("ERROR: Crossing function: " + crossing_fun + " - is not a valid one")
            else: self.crossing_fun = crossing_functions[crossing_fun]
            self.mutation_fun = mutate
            if not selection_functions.__contains__(selection_fun): raise Exception("ERROR: Selection function: " + selection_fun + " - is not a valid one")
            else: self.selection_fun = selection_functions[selection_fun]
            self.aptitude_fun = loaded_aptitude
            self.mutation_prob = mutation_prob
            self.mutation_std = mutation_std

    def from_json(self, input_json_file_name):
        input_file = ""
        try:
            input_file = open(input_json_file_name)
        except Exception:
            print("File error: Invalid json file passed as config")
            quit(1)
        data = json.load(input_file)
        self.load_parameters(data['gen_size'], data['max_generations'], data['crossing_fun'], data['selection_fun'], data['mutation_prob'], data['mutation_std'])
        input_file.close()

    def __str__(self) -> str:
        toRet = "Parameters: \n - mutation_std = {mutation_std}\n - mutation_prob = {mutation_prob}\n - aptitude_fun = {aptitude_fun}\n - selection_fun = {selection_fun}\n - mutation_fun = {mutation_fun}\n - crossing_fun = {crossing_fun}\n - gen_size = {gen_size}\n - max_generations = {max_generations}\n"
        return toRet.format(mutation_std=self.mutation_std, mutation_prob=self.mutation_prob, aptitude_fun=self.aptitude_fun, selection_fun=self.selection_fun, mutation_fun=self.mutation_fun, crossing_fun=self.crossing_fun, gen_size=self.gen_size, max_generations=self.max_generations)

