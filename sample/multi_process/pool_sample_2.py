import multiprocessing
import os
import time

import psutil


def get_cpu_count() -> int:
    return psutil.cpu_count()


def sample_work(x: int) -> int:
    print('Value:', x, ' | PID:', os.getpid())
    time.sleep(1)
    return x * x


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes = get_cpu_count())
    pool_result = pool.map(
        func = sample_work,
        iterable = range(1, 11)
    )
    print(pool_result)
