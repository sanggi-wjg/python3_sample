from haversine import haversine

# from datetime import datetime, date
#
#
# def calculate_age(birthday: str):
#     birth = datetime.strptime(birthday, '%Y-%m-%d')
#     today = date.today()
#     return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
#
#
# print(type(calculate_age('1991-11-14')))
# print(calculate_age('1991-01-14'))

base = '126.9683104,37.344701'
target = '127.0292881,37.5108295'


def calculate_diff_location(base: str, target: str) -> int:
    base = tuple(map(float, base.split(',')))
    target = tuple(map(float, target.split(',')))
    return int(haversine(base, target, unit = 'km'))


print(
    calculate_diff_location(base, target)
)
