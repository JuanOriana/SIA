import collections
import seaborn as sn
import matplotlib.pyplot as plt
import  numpy as np
from TP4.kohonen.KohonenSolver import *
from TP4.kohonen.KohonenSolver import KohonenSolver


def plot_boxplot(data: [], box_plot_title: str):
    areas = []
    GDP = []
    inflations = []
    life_expectations = []
    militaries = []
    pop_growth = []
    unemployment = []
    for i in range(len(data)):
        areas.append(data[i][0])
        GDP.append(data[i][1])
        inflations.append(data[i][2])
        life_expectations.append(data[i][3])
        militaries.append(data[i][4])
        pop_growth.append(data[i][5])
        unemployment.append(data[i][6])

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111)
    x = np.array(['Areas', 'GDP',
                  'Inflations', 'Life_expectations', 'Military', 'Pop_growth', 'Unemployment'])
    ax.set_xticklabels(x)
    plt.title(box_plot_title)
    plt.boxplot([areas, GDP, inflations, life_expectations, militaries, pop_growth, unemployment])
    plt.show()

def plot_single_variable(var:int,k,data_standarized,solver:KohonenSolver,descr:str):
    matrix = np.zeros((k, k))


    for i in range(len(data_standarized)):
        k,j = solver.find_closest(data_standarized[i],data_standarized)
        matrix[k][j] += data_standarized[i][var]
    plt.suptitle(descr)
    sn.heatmap(matrix, cmap='YlGnBu', annot=True)
    plt.show()

def plot_heatmap(inputs,countries,solver,k,learn_rate,radius):
    results = []

    for i in inputs:
        results.append(solver.find_closest(i, inputs))

    matrix = np.zeros((k, k))
    set_values = collections.Counter(results)

    result_to_country = {}
    for i in range(len(results)):
        if results[i] not in result_to_country.keys():
            result_to_country.update({results[i]: []})
        result_to_country[results[i]].append(countries[i])
        matrix[results[i]] += 1

    plt.title("Classification heatmap. Learn_rate: "+ str(learn_rate)+" and radius: "+ str(radius))
    sn.heatmap(matrix, cmap='YlGnBu', annot=True)
    print(result_to_country)

    plt.show()


def plot_neighbours_distance(solver:KohonenSolver,k):
    w_mean = np.zeros((k, k))
    for i in range(len(solver.weights)):
        for j in range(len(solver.weights[0])):
            neighbors = solver.get_neighbours((i, j))
            aux = []
            for n in neighbors:
                if i != n[0] or j != n[1]:
                    aux.append(np.linalg.norm(np.subtract(solver.weights[i][j], solver.weights[n[0]][n[1]])))
            w_mean[i][j] = np.mean(aux)
    plt.title("Neighbours distance")
    sn.heatmap(w_mean, cmap='Greys', annot=True)

    plt.show()