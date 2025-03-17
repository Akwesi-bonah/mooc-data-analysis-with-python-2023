#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    rows = np.arange(n).reshape(-1, 1)
    cols = np.arange(n).reshape(1, -1)

    result = rows * cols
    return result

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
