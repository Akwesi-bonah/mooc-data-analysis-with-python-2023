#!/usr/bin/env python3
import pandas as pd
import numpy as np


def read_series():
    s = pd.Series([], dtype="object")
    values = []
    indexs = []

    while True:
        print("Enter values: ")
        data = input()
        if len(data) == 0:
            return pd.Series(values, indexs)
        else:
            try:
                index, value = data.split()
                indexs.append(index)
                values.append(value)
            except:
                raise Exception("Error with input")

def main():
    pass

if __name__ == "__main__":
    main()
