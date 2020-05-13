import base64
import hashlib
from datetime import datetime, timedelta

sample = [
    {
        'detailDc'    : None,
        'nowLc'       : '서울마포우체국',
        'processDe'   : '2020-02-20 17:31',
        'processSttus': '접수'
    },
    {
        'detailDc'    : None,
        'nowLc'       : '서울마포우체국',
        'processDe'   : '2020-02-21 18:52',
        'processSttus': '발송'
    },
    {
        'detailDc'    : None,
        'nowLc'       : '국제우편물류센터',
        'processDe'   : '2020-02-21 20:55',
        'processSttus': '발송교환국에 도착'
    },
    {
        'detailDc'    : None,
        'nowLc'       : '국제우편물류센터',
        'processDe'   : '2020-02-28 07:41',
        'processSttus': '발송준비'
    },
    {
        'detailDc'    : None,
        'nowLc'       : 'INCHEON',
        'processDe'   : '2020-02-28 14:23',
        'processSttus': '운송사 인계'
    }
]


# for s in sample:
#     print(s)

def ret_subtract_date_format(subtractType: str = '', subtract: int = '', timeFormat: str = '%Y-%m-%d %H:%M:%S'):
    if subtractType == 'hour':
        result = datetime.today() - timedelta(hours = subtract)

    else:
        raise TypeError('Unknown Subtract Type')

    return result.strftime(timeFormat)


def ret_add_date_format(type: str = '', subtract: int = '', timeFormat: str = '%Y-%m-%d %H:%M:%S'):
    if type == '-hour':
        result = datetime.today() - timedelta(hours = subtract)

    elif type == '-day':
        result = datetime.today() - timedelta(days = subtract)

    else:
        raise TypeError('Unknown Subtract Type')

    return result.strftime(timeFormat)


print(ret_add_date_format('-day', 1, '%Y%m%d'))
