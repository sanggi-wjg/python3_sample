import functools
import random
import sys
import time
import traceback


def ret_brief_except(short: bool = False):
    exc_type, exc_value, exc_tb = sys.exc_info()

    if short:
        return "(Type) : {} | (Line) : {} | (Msg) : {}".format(exc_type.__name__, exc_tb.tb_lineno, exc_value)
    else:
        return "(Type) : {} | (Line) : {} | (Msg) : {}\n{}".format(exc_type.__name__, exc_tb.tb_lineno, exc_value, traceback.format_exc())


def retry_decorate(total_try_cnt: int = 5, sleep_time: int = 1, retryable_exceptions: tuple = ()):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for cnt in range(total_try_cnt):
                print('[{}/{}] ({}) args : {} | kwargs : {}'.format(cnt, total_try_cnt, func.__name__, args, kwargs))

                try:
                    result = func(*args, **kwargs)
                    print('[{}/{}] ({}) Result : {}'.format(cnt, total_try_cnt, func.__name__, result))
                    return result

                except retryable_exceptions as e:
                    print('[{}/{}] ({}) Retry Exception : {}'.format(cnt, total_try_cnt, func.__name__, e))

                except Exception as e:
                    print('[{}/{}] ({}) Exception : {}'.format(cnt, total_try_cnt, func.__name__, e))
                    raise e

                finally:
                    time.sleep(sleep_time)
                    print()

        return wrapper

    return decorator


@retry_decorate(total_try_cnt = 3, retryable_exceptions = (KeyError, ValueError))
def is_odd_number(test, *args, **kwargs):
    rand_num = random.randint(1, 5)
    print('Rand Number', rand_num)

    if rand_num % 2 == 0:
        raise ValueError('ValueError')

    #return True


if __name__ == '__main__':
    for _ in range(1):
        try:
            is_odd_number('hello', 'args', key_word = 'keyword')

        except Exception as e:
            print(ret_brief_except(False))
