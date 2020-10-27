from datetime import datetime, timedelta


def diff_days(base_date: str, target_date: str) -> int:
    if isinstance(base_date, str) and isinstance(target_date, str):
        base_date = base_date.replace('-', '')
        target_date = target_date.replace('-', '')

        base_time = datetime(int(base_date[0:4]), int(base_date[4:6]), int(base_date[6:8]))
        target_time = datetime(int(target_date[0:4]), int(target_date[4:6]), int(target_date[6:8]))
    else:
        raise TypeError('diff_days Type error')

    return (target_time - base_time).days


def diff_days_to_list(from_date: str, to_date: str):
    diff = diff_days(from_date, to_date)
    base = datetime(int(from_date[0:4]), int(from_date[4:6]), int(from_date[6:8]))
    date_list = [(base + timedelta(days = x)).strftime('%Y%m%d') for x in range(diff + 1)]

    return date_list


days_list = diff_days_to_list('20191101', '20191107')
print(days_list)
print(diff_days('20191101', '20191107'))

for day in days_list:
    print(diff_days('20191101', day))
