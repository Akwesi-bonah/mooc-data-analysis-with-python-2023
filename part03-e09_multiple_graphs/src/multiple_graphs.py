#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.array([2,4,6,7])
    y = np.array([4,3,5,1])

    x1 = np.array([1,2,3,4])
    y1 = np.array([4,2,3,1])
    plt.plot(x,y)
    plt.plot(x1,y1)
    plt.title("title")
    plt.ylabel("y-axis")
    plt.xlabel("x-axis")
    plt.show()

if __name__ == "__main__":
    main()
