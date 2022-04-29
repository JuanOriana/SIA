import numpy as np
import pandas as pd


def parse(file_name: str, normalize= None):
    df = pd.read_csv(file_name, sep=' +', engine='python', header=None)
    max_num = df.values.max()
    min_num = df.values.min()
    if normalize:
        if normalize == "TANH":
            for i in range(len(df.values)):
                df.values[i] = 2 * (df.values[i] - min_num) / (max_num - min_num) - 1
        else:
            for i in range(len(df.values)):
                df.values[i] = (df.values[i] - min_num) / (max_num - min_num)

    return df.to_numpy(), max_num , min_num


def parse_nums(file_name: str, height: int):
    df = pd.read_csv(file_name, sep=' +', engine='python', header=None)
    arrayed = df.to_numpy()
    chunked = []
    base = 0
    while base < len(arrayed) - height + 1:
        grouped = np.array([], dtype=int)
        for i in range(height):
            grouped = np.append(grouped, arrayed[base + i])
        chunked.append(np.copy(grouped))
        base += height

    return np.array(chunked)


def nums_out_float():
    return np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])


def nums_out_arr():
    return [[1,0,0,0,0,0,0,0,0,0], #0
            [0,1,0,0,0,0,0,0,0,0], #1
            [0,0,1,0,0,0,0,0,0,0], #2
            [0,0,0,1,0,0,0,0,0,0], #3
            [0,0,0,0,1,0,0,0,0,0], #4
            [0,0,0,0,0,1,0,0,0,0], #5
            [0,0,0,0,0,0,1,0,0,0], #6
            [0,0,0,0,0,0,0,1,0,0], #7
            [0,0,0,0,0,0,0,0,1,0], #8
            [0,0,0,0,0,0,0,0,0,1]] #9
