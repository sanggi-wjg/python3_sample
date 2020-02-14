import json
import threading
from typing import Optional, Callable, Any, Iterable, Mapping
from urllib.request import urlopen


class MyThread(threading.Thread):

    def run(self) -> None:

        try:
            # res = urlopen('http://192.168.1.241:8080/cron/invoice/test_get')
            res = urlopen('http://192.168.1.241:8000/test/rand')
            print(self.getName(), ':', json.loads(res.read()))

        except Exception as e:
            print(e)
