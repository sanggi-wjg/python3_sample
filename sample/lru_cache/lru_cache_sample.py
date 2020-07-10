from datetime import datetime
from functools import lru_cache


@lru_cache(maxsize = 10)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


@lru_cache(maxsize = 10)
def sum_t(n):
    res = 0
    for i in range(n):
        res += n
    return res


def fib_not_cached(n):
    if n < 2:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def sum_not_cached(n):
    res = 0
    for i in range(n):
        res += n
    return res


if __name__ == '__main__':
    # print([fib(p) for p in range(100, 200)])
    fibonacci_sample = [400, 401, 402]
    sum_sample = [100000000, 100000001, 100000002]

    for f, s in zip(fibonacci_sample, sum_sample):
        fib(f)
        sum_t(s)
    print('cache done')

    start_time = datetime.now()
    for f, s in zip(fibonacci_sample, sum_sample):
        fib(f)
        sum_t(s)
        print('done')
    finish_time = datetime.now()
    print('SPENT TIME : {}\n'.format(finish_time - start_time))
    del start_time, finish_time

    start_time = datetime.now()
    for f, s in zip(fibonacci_sample, sum_sample):
        fib_not_cached(f)
        sum_not_cached(s)
        print('done')
    finish_time = datetime.now()
    print('SPENT TIME : {}'.format(finish_time - start_time))
