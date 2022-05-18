import os


def parse(path_to_file):
    file = open(path_to_file, 'r')
    lines = file.readlines()
    letters = []
    letter = []
    for line in lines:
        if line[0] != "-" and line[0] != "1":
            letters.append(letter)
            letter = []
        else:
            i = 0
            while i < len(line):
                if line[i] == "1":
                    letter.append(1.)
                    i += 1
                elif line[i] == "-":
                    letter.append(-1.)
                    i += 2
                else:
                    i += 1
    return letters


def printLetter(letter):
    edited = []
    if letter is False:
        return False
    for i in range(len(letter)):
        if letter[i] == -1:
            edited.append(" ")
        else:
            edited.append("*")
    for i in range(5):
        print(edited[i*5], edited[(i*5)+1], edited[(i*5)+2], edited[(i*5)+3], edited[(i*5)+4])

def main():
    letters = parse('letters_matrix.txt')
    print(letters)
    for letter in letters:
        printLetter(letter)
        print()


if __name__ == "__main__":
    main()