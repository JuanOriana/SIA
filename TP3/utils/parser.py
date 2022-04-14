import pandas as pd


def parse(file_name: str):
    df = pd.read_csv(file_name, sep=' +', engine='python')
    return df.to_numpy()
