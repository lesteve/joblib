from joblib import Memory

mem = Memory(cachedir='cache', verbose=1)

import numpy as np

a = np.vander(np.arange(3)).astype(np.float)
square = mem.cache(np.square)
b = square(a)

square(a)

