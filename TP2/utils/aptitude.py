from typing import List

from TP2.data_structs.Individual import Individual
from TP2.data_structs.TestCase import TestCase
from TP2.utils.logistic_function import logistic_function


def big_f(indiv:Individual, case:TestCase):
    x = 0
    for j in range(0, 2):
        y = 0
        for k in range(0, 3):
            y += indiv.get_little_w(j)[k] * case.params[k]
        y -= indiv.get_w_0()[j] # TODO: Preguntar si es w0 a lo que se refiere
        x += indiv.get_big_w()[j] * logistic_function(y)
    return logistic_function(x - indiv.get_big_w()[0])


def aptitude(indiv:Individual, test_cases: List[TestCase]):
    x = 0
    for u in range(len(test_cases)):
        x += pow(test_cases[u].result - big_f(indiv, test_cases[u]), 2)
    return x
