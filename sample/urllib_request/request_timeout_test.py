import socket
import time
import urllib.request
from datetime import datetime


def ret_date_format(timeFormat: str = '%Y-%m-%d %H:%M:%S', strDate: str = '', strDateFormat: str = '%Y%m%d%H%M%S'):
    if not strDate:
        result = datetime.today().strftime(timeFormat)

    else:
        result = datetime.strptime(strDate, strDateFormat).strftime(timeFormat)

    return result


def request():
    socket.setdefaulttimeout(0.01)

    urllib.request.urlretrieve(
        url = 'http://www.naver.com',
        filename = '{}.txt'.format(ret_date_format('%Y%m%d_%H_%M_%S'))
    )

    time.sleep(5)


if __name__ == '__main__':

    for i in range(1, 11):
        print('TRY : ', i, socket.getdefaulttimeout())
        request()
