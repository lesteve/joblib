import os
import multiprocessing


def f(arg):
    x = 1
    y = 2
    z = 3
    return arg

def mypid(_):
    return os.getpid()


def test_f():
    pool = multiprocessing.Pool(2)
    print(pool.map(mypid, range(4)))
    pool.apply(f, (1,))
    # Parallel(n_jobs=2)(delayed(f)(i) for i in range(3))

test_f()
