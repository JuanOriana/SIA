class GeneticSelectionParams:
    def __init__(self, k:int, threshold: float, inital_temp:float, change_factor:float,decrease_factor:float):
        self.k = k
        self.threshold = threshold
        self.initial_temp = inital_temp
        self.change_factor = change_factor
        self.decrease_factor = decrease_factor
        self.current_gen_number = 0
