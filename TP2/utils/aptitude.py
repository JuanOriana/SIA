import numpy as np

from TP2.data_structs.Individual import Individual
from TP2.data_structs.TestCase import TestCase
from TP2.utils.logistic_function import logistic_function


def big_f(indiv:Individual, test_case:TestCase):
    y = 0
    x = 0
    for j in range(1, 2):
        for k in range(1, 3):
            y += indiv.get_little_w(j)[k] * test_case.values[k]
        y -= indiv.get_w_0()[j] # Revisar por que en el enunciado no queda clara que  w es..
        x += indiv.get_big_w()[j] * logistic_function(y)
    return logistic_function(x - indiv.get_big_w()[0])


def aptitude(indiv:Individual, test_case: TestCase):
    x = 0
    for u in range(1, 3):
        x += pow(test_case.result[u] - big_f(indiv, test_case.values[u]), 2)
        
    return x
