import numpy as np

from joblib import Memory


mem = Memory('cache')


@mem.cache
def my_function(i):
    return np.sqrt((i * np.arange(1000)) ** 2)


while True:
    for i in range(4):
        my_function(i)

