import numpy as np
import pandas as pd


def parse(file_name: str):
    df = pd.read_csv(file_name, sep=' +', engine='python', header=None)
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
