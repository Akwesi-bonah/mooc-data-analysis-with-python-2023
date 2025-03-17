#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    len = int(a.shape[1]/2)
    arr = np.sum(a[:,:len], 1) > np.sum(a[:,len:], 1)
    return a[arr]

def main():
    pass

if __name__ == "__main__":
    main()
