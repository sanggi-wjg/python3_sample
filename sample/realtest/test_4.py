from datetime import time, datetime


# print(datetime.strptime(sample, '%Y%m%d%H%M%S').strftime('%Y-%m-%d %H:%M:%S'))


def is_valid_date_format(date: str, dateFormat: str = '%Y%m%d') -> bool:
    """
    @param date: 입력 날짜
    @param dateFormat: 날짜 포맷
    @return: 포맷이 이상하면 False, 정상이면 True
    """
    try:
        result = datetime.strptime(date, dateFormat)
        print('@', result)
    except ValueError:
        return False

    return True


def ret_date_format(timeFormat: str = '%Y-%m-%d %H:%M:%S', strDate: str = '', strDateFormat: str = '%Y%m%d%H%M%S'):
    if not strDate:
        result = datetime.today().strftime(timeFormat)

    else:
        result = datetime.strptime(strDate, strDateFormat).strftime(timeFormat)

    return result


if __name__ == '__main__':
    sample = '202004051501'
    print(sample)

    sample = ret_date_format(strDate = sample)
    # print(is_valid_date_format(sample, '%Y-%m-%d %H:%M:%S'))
