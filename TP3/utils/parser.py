import numpy as np
import pandas as pd


def parse(file_name: str,normalize=False):
    df = pd.read_csv(file_name, sep=' +', engine='python', header=None)
    if normalize:
        max_num = df.values.max()
        min_num = df.values.min()
        for i in range(len(df.values)):
            df.values[i] = 2 * (df.values[i]-min_num)/(max_num-min_num) - 1
            print(df.values[i])

    return df.to_numpy()


def parse_nums(file_name: str, height: int):
    df = pd.read_csv(file_name, sep=' +', engine='python', header=None)
    arrayed = df.to_numpy()
    print(arrayed)
    chunked = []
    base = 0
    while base < len(arrayed) - height + 1:
        grouped = np.array([], dtype=int)
        for i in range(height):
            grouped = np.append(grouped, arrayed[base + i])
        chunked.append(np.copy(grouped))
        base += height

    return np.array(chunked)
