import numpy as np

from joblib import Memory

mem = Memory('cache')


def _my_function(i):
    return np.sqrt((i * np.arange(1000)) ** 2)

my_function = mem.cache(_my_function)
