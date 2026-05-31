# ==========================================================
# dataset.py
# Carregamento do dataset Sudoku
# ==========================================================

import pandas as pd
import numpy as np


def load_dataset(path):

    data = pd.read_csv(path, header=None)

    data = data.values

    X = data[:, :16]
    Y = data[:, 16:]

    X = np.array(X, dtype=np.float32)
    Y = np.array(Y, dtype=np.float32)

    return X, Y


if __name__ == "__main__":

    X, Y = load_dataset("train.csv")

    print("Entradas:", X.shape)
    print("Saídas:", Y.shape)

    print("\nPrimeiro exemplo:")
    print(X[0])

    print("\nSolução:")
    print(Y[0])
