from joblib import Parallel, delayed

from my_module import my_function


while True:
    Parallel(n_jobs=-1)(delayed(my_function)(i) for i in range(4))
