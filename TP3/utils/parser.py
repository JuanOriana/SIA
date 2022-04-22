import pandas as pd


def parse(file_name: str,normalize=False):
    df = pd.read_csv(file_name, sep=' +', engine='python')

    if normalize:
        max_num = df.values.max()
        min_num = df.values.min()
        for i in range(len(df.values)):
            df.values[i] = 2 * (df.values[i]-min_num)/(max_num-min_num) - 1
            print(df.values[i])

    return df.to_numpy()
