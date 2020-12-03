import threading
from datetime import datetime

import requests


def sample_func():
    response = requests.get('http://192.168.10.6:8000/zzz/sleep/5')
    print(response.text)


COUNT = 5

start = datetime.now()
for _ in range(COUNT):
    sample_func()
finish = datetime.now()
print('Single : {}'.format(finish - start))
del start, finish

thread_list = []
start = datetime.now()
for i in range(COUNT):
    thread_list.append(threading.Thread(name = '{} 쓰레드'.format(i + 1), target = sample_func))

for th in thread_list:
    print(th.name)
    th.start()

for th in thread_list:
    th.join()
finish = datetime.now()
print('Multi-Thread : {}'.format(finish - start))
