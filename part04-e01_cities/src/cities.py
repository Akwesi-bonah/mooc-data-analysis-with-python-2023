#!/usr/bin/env python3

import pandas as pd

def cities():
    data = {
        'Population': [643272, 279044, 231853, 223027,  201810],
        'Total area': [715.48, 528.03, 689.59, 240.35, 3817.52]
    }
    cites = ['Helsinki','Espoo', 'Tampere', 'Vantaa','Oulu']
    return pd.DataFrame(data, index=cites)
    
def main():
    print(cities())
    return
    
if __name__ == "__main__":
    main()