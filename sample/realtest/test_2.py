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


# print(ret_subtract_date_format('hour', 1))

def ret_add_date_format(type: str = '', subtract: int = '', timeFormat: str = '%Y-%m-%d %H:%M:%S'):
    if type == '-hour':
        result = datetime.today() - timedelta(hours = subtract)

    else:
        raise TypeError('Unknown Subtract Type')

    return result.strftime(timeFormat)


def make_param():
    xml = '<?xml version="1.0"?>' \
          '<Request service="RouteService" lang="zh-CN">' \
          '<Head>{}</Head>' \
          '<Body><Route tracking_type="1" tracking_number="{}"/></Body>' \
          '</Request>'.format('OSMS_1', '1234')
    # print(xml)

    xb = xml.encode('utf-8')
    xb = base64.b64encode(xb)
    print(xb.decode('utf-8'))
    ###########################

    xc = (xml + 'test').encode('utf-8')
    m = hashlib.md5(xc)
    print(m)

    vs = base64.b64encode(m.digest())
    print(vs)


make_param()
