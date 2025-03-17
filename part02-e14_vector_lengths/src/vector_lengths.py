#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a**2,axis=1))

def main():
    arr = np.array([[1,2],[4,5],[7,8]])
    print(vector_lengths(arr))
    

if __name__ == "__main__":
    main()
