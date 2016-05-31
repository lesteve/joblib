import time

from math import sqrt
from joblib import Memory


mem = Memory('cache', bytes_limit='10K', verbose=100)
my_sqrt = mem.cache(sqrt)

while True:
    time.sleep(0.1)
    mem.clean()
