import pandas as pd

from src.config import DATASET_PATH


def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    df = df.drop('id', 1)
    return df


def map_boolean_to_real(df, columns):
    x = (df[columns] == 'T').astype(int)
    df[columns] = x
    return df
