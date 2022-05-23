import sys
from statistics import mean, stdev

import numpy as np
import copy

import pandas as pd

def parse_csv_opt(file_path):
    df = pd.read_csv(file_path)
    countries = df.values[:,0]
    df.set_index('Country', drop=True, inplace=True)
    data = df.values

    # Standardize the data
    data_standarized = copy.deepcopy(data)

    for i in range(len(data[0])):
        aux = data_standarized[:, i]
        mean_aux = mean(aux)
        stdev_aux = stdev(aux)
        data_standarized[:, i] = (data_standarized[:, i] - mean_aux) / stdev_aux

    return data, data_standarized,countries , ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']
