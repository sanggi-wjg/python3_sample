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


test = {
    'Response':
        {
            'code'   : '3001',
            'success': 'false',
            'reason' : '处理失败.请求校验签名失败'
        }
}

test = {
    'ufinterface': {
        'Result': {
            'WaybillProcessInfo': [
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/02/27 11:28:40', 'ProcessInfo': '【当地快递公司】 已收件 取件人: HW韩国国际3部1 (95554)' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/02/27 19:18:55', 'ProcessInfo': '韩国仁川国际转运仓,已收入' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/02/28 05:21:43', 'ProcessInfo': '韩国仁川国际转运仓,上车扫描' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/02/28 07:03:26', 'ProcessInfo': '韩国仁川,航班起飞' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/02/28 09:41:09', 'ProcessInfo': '上海,航班到达' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/02/28 12:59:27', 'ProcessInfo': '上海,目的地清关中' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/03/01 13:28:23', 'ProcessInfo': '【上海市嘉定区江桥公司】 已收件 取件人: 高响 (17821805727)' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/03/01 13:28:33', 'ProcessInfo': '【上海市嘉定区江桥】 已发出 下一站 【上海转运中心】' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/03/01 18:22:16', 'ProcessInfo': '【上海转运中心公司】 已打包' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/03/01 18:24:01', 'ProcessInfo': '【上海转运中心公司】 已收入' },
                { 'Waybill_No': 'YTG000838706720', 'Upload_Time': '2020/03/01 19:17:43', 'ProcessInfo': '【上海转运中心】 已发出 下一站 【南昌转运中心】' }
            ]
        }
    }
}

if 'Response' in test.keys():
    code = test.get('Response').get('code')
    success = test.get('Response').get('success')
    reason = test.get('Response').get('reason')

    print(code, success, reason)
