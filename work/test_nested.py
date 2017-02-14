import time

import numpy as np

from joblib import Parallel, delayed


def func(arg):
    print('func({})'.format(arg))
    result = np.zeros(int(1e7))
    result[0] = arg
    return result


def parallel_func():
    return Parallel(n_jobs=2, return_iterator=False,
                    verbose=2)(delayed(func)(i) for i in range(10))


Parallel(n_jobs=2)(delayed(parallel_func)() for _ in range(3))
