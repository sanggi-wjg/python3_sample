from datetime import datetime


def get_today_year():
    return datetime.today().year


def get_today_month():
    # return datetime.today().month
    return datetime.today().strftime('%m')


def get_today_day():
    return datetime.today().strftime('%d')


def get_today_format(format: str = '%Y-%m-%d %H:%M:%S'):
    return datetime.today().strftime(format)


def is_valid_date_format_dep():
    def is_valid_date_format(date: str, dateFormat: str = '%Y%m%d') -> str:
        try:
            datetime.strptime(date, dateFormat)

            return 'Yes True'

        except ValueError:
            return 'No False'

    target = {
        '2010-01-01',
        '20101010',
        '20111301',
        '99990101',
    }

    for date in target:
        print(date, ' : ', is_valid_date_format(date))


def return_long_word(lst):
    return [word for word in lst]


if __name__ == '__main__':
    # print(get_today_month())
    # print(get_today_day())

    # lst = { 'blog', 'blog1', 'blog12' }
    # print(return_long_word(lst))

    print(get_today_format('%Y-%m-%d %H:%M:%S'))
