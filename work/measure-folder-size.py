import sys
import os
import collections
import datetime
import operator

CacheItemInfo = collections.namedtuple('CacheItemInfo',
                                       'path size last_access')


def get_info(start_path='.'):
    cache_info = []

    for dirpath, dirnames, filenames in os.walk(start_path):
        # Need something to decide whether it is a cache folder or not
        # ... Could be improved
        output_filename = os.path.join(dirpath, 'output.pkl')
        if os.path.isfile(output_filename):
            last_access = datetime.datetime.fromtimestamp(
                os.path.getatime(output_filename))
            full_filenames = [os.path.join(dirpath, fn) for fn in filenames]
            # print(full_filenames)
            dirsize = sum(os.path.getsize(fn)
                          for fn in full_filenames)

            cache_info.append(CacheItemInfo(dirpath, dirsize, last_access))

    return cache_info


def get_folders_to_delete(start_path, gigabytes_limit):
    cache_info = get_info(start_path)
    cache_size = sum(item.size for item in cache_info)

    to_delete_size = cache_size - gigabytes_limit * 1024 ** 3
    if to_delete_size < 0:
        return []

    cache_info.sort(key=operator.attrgetter('last_access'))

    folders_to_delete = []
    size_so_far = 0

    for item in cache_info:
        if size_so_far > to_delete_size:
            return folders_to_delete

        folders_to_delete.append(item.path)
        size_so_far += item.size

    # TODO I could potentially clean-up if I removed all the hashes
    # from a given function. Otherwise it will never be cleaned up
    # ... At the same time it doesn't take that much space it is just
    # untidy
    raise ValueError('Hmmm looks like something went wrong somewhere. '
                     'Unable to reduce cache size to gygabytes_limit {0}.'
                     .format(gigabytes_limit))


if __name__ == '__main__':
    import pprint
    # size_info = get_info(sys.argv[1])
    # pprint.pprint(size_info)

    folders_to_delete = get_folders_to_delete(sys.argv[1], float(sys.argv[2]))

    size_to_remove = sum(os.path.getsize(os.path.join(dirname, fn))
                         for dirname in folders_to_delete
                         for fn in os.listdir(dirname))
    print('size_to_remove in GB:', size_to_remove / 1024 ** 3)
