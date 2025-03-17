#!/usr/bin/env python3
import numpy as np
from functools import reduce
import math

def matrix_power(a, n):
    val = a
    num = n - 1

    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    elif n < 0:
        g_num = [a for i in range(abs(n))]
        fun = lambda  x,y : x @ y
        multi = reduce(fun, g_num)
        val = np.linalg.inv(multi)
    else:
        g_num = [a for i in range(abs(n))]
        fun = lambda x, y : x@ y
        val = reduce(fun, g_num)

    return (val)

def main():
    return

if __name__ == "__main__":
    main()
