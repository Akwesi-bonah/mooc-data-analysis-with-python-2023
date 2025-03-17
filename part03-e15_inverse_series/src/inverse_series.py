#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    s1 = pd.Series(s)
    idx = [i for i in s1.index]
    val = [i for i in s1.values]

    result = pd.Series(idx,index=val)
    print(result)

    return  result

def main():
    d = { 2001 : "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017 : "Trump"}
    s4 = pd.Series(d, name="Presidents")
    print(inverse_series(s4))


    return

if __name__ == "__main__":
    main()
