import numpy as np

from TP2.utils.logistic_function import logistic_function


def big_f(indiv: np.ndarray, params):
    y = 0
    x = 0
    for j in range(1, 2):
        for k in range(1, 3):
            y += indiv[(3 * j) + k - 1] * params[k]
        y -= indiv[(3 * j)]
        x += indiv[j] * logistic_function(y)
    return logistic_function(x - indiv[0])


def aptitude(indiv: np.ndarray, params):
    x = 0
    for u in range(1, 3):
        x += pow(params.result - big_f(indiv, params.values), 2)
        
    return x
