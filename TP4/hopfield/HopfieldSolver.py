import numpy as np

from TP4.show_letters import parse, print_letter


class HopfieldSolver:

    def solve(self, query: np.ndarray, inputs: np.ndarray):
        # Estimating weights
        count, dimension = inputs.shape
        K = np.zeros((count, dimension))
        for i in range(len(inputs)):
            K[i, :] = inputs[i]
        weights = (1 / dimension) * (np.matmul(K.T, K))
        np.fill_diagonal(weights, 0)

        t = 0
        S = query
        old_S = None

        while not np.array_equal(S, old_S):
            old_S = S
            S = np.sign(np.dot(weights, S))
            t += 1

        return S, t


if __name__ == "__main__":
    solver = HopfieldSolver()
    letters = parse('../letters_matrix.txt')

    inputs = np.array([letters[0], letters[6], letters[8], letters[11]])

    print("\nInput letters: \n")
    for input in inputs:
        print_letter(input)
        print()

    print("\n ------------------ \n")

    # print(inputs)
    #inputs = np.array([[1, 1, -1, -1], [-1, -1, 1, 1]])
    predict_letter = letters[6]
    # letters[9] es un estado espureo
    bitmap_solved, iterations = solver.solve(np.array(predict_letter), inputs)
    print("Letter to predict: \n")
    print_letter(predict_letter)
    print("\nLetter predicted: \n")
    print_letter(bitmap_solved)

