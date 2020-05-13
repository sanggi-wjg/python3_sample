import functools
import logging
import time
from random import random

logging.basicConfig()
logger = logging.getLogger('retry_test')
logger.setLevel(logging.INFO)


def retry(total_try_cnt = 5, sleep_in_sec = 5, retryable_exceptions = ()):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for cnt in range(total_try_cnt):
                logger.info(f"trying {func.__name__}() [{cnt + 1}/{total_try_cnt}]")

                try:
                    result = func(*args, **kwargs)
                    logger.info(f"in retry(), {func.__name__}() returned '{result}'")

                    if result: return result
                except retryable_exceptions as e:
                    logger.info(f"in retry(), {func.__name__}() raised retryable exception '{e}'")
                    pass
                except Exception as e:
                    logger.info(f"in retry(), {func.__name__}() raised {e}")
                    raise e

                time.sleep(sleep_in_sec)
            logger.info(f"{func.__name__} finally has been failed")

        return wrapper

    return decorator


@retry(total_try_cnt = 3, sleep_in_sec = 3, retryable_exceptions = (OSError, ValueError))
def my_method():
    rand = random.randint(0, 9)
    logger.info(f"rand={rand}")

    if rand % 3 == 0:
        return True
    elif rand % 3 == 1:
        return False
    else:
        raise int("a")


my_method()
