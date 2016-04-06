import sys
import os


def get_size(start_path='.'):
    total_size = {}

    for dirpath, dirnames, filenames in os.walk(start_path):
        if os.path.isfile(os.path.join(dirpath, 'metadata.json')):
            full_filenames = [os.path.join(dirpath, fn) for fn in filenames]
            # print(full_filenames)
            total_size[dirpath] = sum(os.path.getsize(fn)
                                      for fn in full_filenames)

    return total_size


if __name__ == '__main__':
    size_info = get_size(sys.argv[1])
    # print(size_info)
