from joblib import Memory, Parallel, delayed

mem = Memory(cachedir='cache', verbose=0)

import numpy as np

a = np.vander(np.arange(3)).astype(np.float)
my_square = mem.cache(np.square)

if __name__ == '__main__':
    n_tasks = 1000

    # To cache it once
    my_square(a)

    Parallel(n_jobs=-1, verbose=1)(
        delayed(my_square)(a) for i in range(n_tasks))
