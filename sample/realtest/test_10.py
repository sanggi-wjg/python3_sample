from datetime import datetime, timedelta


def today_dateformat(time_format = '%Y-%m-%d %H:%M:%S'):
    return datetime.today().strftime(time_format)


def days_to_list(date_range: int) -> list:
    date_list = []

    for n in range(1, date_range):
        day = datetime.strptime(today_dateformat('%Y%m%d'), '%Y%m%d') - timedelta(days = n)
        date_list.append(day.strftime('%Y%m%d'))

    return date_list


print(days_to_list(113))
