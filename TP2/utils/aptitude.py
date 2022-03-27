from TP2.data_structs.Individual import Individual
from TP2.data_structs.TestCase import TestCase
from TP2.utils.logistic_function import logistic_function

test_cases = [TestCase(1, [-3.9429, -0.7689, 4.8830]), TestCase(1, [4.1793, -4.9218, 1.7664]),
              TestCase(0, [4.4793, -4.0765, -4.0765])]

def big_f(indiv: Individual, case: TestCase):
    x = 0
    for j in range(0, 2):
        y = 0
        for k in range(0, 3):
            y += indiv.get_little_w(j)[k] * case.params[k]
        y -= indiv.get_w_0()[j]  # TODO: Preguntar si es w0 a lo que se refiere
        x += indiv.get_big_w()[j] * logistic_function(y)
    return logistic_function(x - indiv.get_big_w()[0])


def aproximation_error(indiv: Individual, test_cases: list[TestCase]):
    err = 0
    for u in range(len(test_cases)):
        err += pow(test_cases[u].result - big_f(indiv, test_cases[u]), 2)
    return err


# worst value = 0. best value = amount of test_cases
def aptitude(indiv: Individual, test_cases: list[TestCase]):
    e = aproximation_error(indiv, test_cases)
    return len(test_cases) - e


def loaded_aptitude(indiv: Individual):
    return aptitude(indiv, test_cases)
