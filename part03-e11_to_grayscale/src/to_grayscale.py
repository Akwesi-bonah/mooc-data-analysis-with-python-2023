#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    print(image.shape)
    multiplicators = [0.2126, 0.7152, 0.0722]
    grayscaled = np.sum(multiplicators * image, axis = 2)
    return grayscaled



def to_red(image):
    red = image.copy()
    return red * [1, 0,0]


def to_green(image):
    green = image.copy()
    return green * [0,1,0]

def to_blue(image):
    blue = image.copy()
    return blue


def main():
    pass

if __name__ == "__main__":
    main()
