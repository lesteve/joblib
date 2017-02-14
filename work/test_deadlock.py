import time

import multiprocessing, logging
logger = multiprocessing.log_to_stderr()
logger.setLevel(multiprocessing.SUBDEBUG)
import numpy as np

from joblib import Parallel, delayed


def func(arg):
    print('func({})'.format(arg))
    result = np.zeros(int(1e7))
    result[0] = arg
    return result

parallel = Parallel(n_jobs=2, return_iterator=True,
                    verbose=2, backend='multiprocessing')

result = parallel(delayed(func)(i) for i in range(10))
gen = result.__iter__()
next(gen)
next(gen)
# parallel._backend._pool.close()
# print('closed')
# parallel._backend._pool.join()
# print('joined')
parallel._backend.terminate()
# print('applied:', parallel._backend._pool.apply(func, (-1,)))
# for i in result: pass
# del result
