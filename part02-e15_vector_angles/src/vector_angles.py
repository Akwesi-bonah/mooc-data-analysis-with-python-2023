#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    dot = np.sum(X * Y, axis=1)
    mX = np.sqrt(np.sum(X**2, axis=1))
    mY = np.sqrt(np.sum(Y**2, axis=1))

    angle = dot / (mX * mY)

    ang = np.arccos(angle)
    result = np.degrees(ang)
    return result

def main():
    x = np.array([[0,2]])
    y = np.array([[3,3]])
    vector_angles(x, y)

if __name__ == "__main__":
    main()
