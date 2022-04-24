import sys

from scipy import optimize
import numpy as np

from TP2.utils.aptitude import loaded_error


def main():
    if len(sys.argv) != 2 or (sys.argv[1] != "CG" and sys.argv[1] != "L-BFGS-B"):
        print("Invalid usage: conugate.py <CG|L-BFGS-B>")
        quit(1)

    status = optimize.minimize(loaded_error, np.zeros(11), method=sys.argv[1])
    print("Method: ", sys.argv[1])
    print("Success: ", status.success)
    print("Number of iterations: ", status.nit)
    print("Number of function evals: ", status.nfev)
    print("Number of jacbian evals: ", status.njev)
    print("Found weights: ", status.x)


if __name__ == "__main__":
    main()
