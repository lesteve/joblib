import os
import datetime

from joblib import Parallel, delayed

import pandas as pd


def write_timestamp(filename):
    timestamp = datetime.datetime.now().isoformat()
    # line = '-'*80 + '\n' + timestamp + '\n' + '-'*80 + '\n'
    line = timestamp + '\n'

    with open(filename, 'a') as f:
        f.write(line)


def check_file(filename, n_timestamps):
    with open(filename) as f:
        df = pd.read_csv(f, header=None)
    timestamps = pd.to_datetime(df.iloc[:, 0])
    assert len(timestamps) == n_timestamps
    return timestamps


def main():
    filename = '/tmp/test_timestamps.txt'
    if os.path.exists(filename):
        os.unlink(filename)

    n_timestamps = int(1e6)
    Parallel(n_jobs=-1, verbose=100)(
        delayed(write_timestamp)(filename) for i in range(n_timestamps))

    print(check_file(filename, n_timestamps).describe())
    return locals()

if __name__ == '__main__':
    locals().update(main())
