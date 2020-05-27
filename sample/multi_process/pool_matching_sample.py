import multiprocessing
import os

from sample.multi_process.pool_sample_2 import get_cpu_count

READ_DATA = [
    {
        'invoiceNo': 'S-1',
        'where'    : 'Seoul'
    },
    {
        'invoiceNo': 'S-2',
        'where'    : 'Seoul'
    },
    {
        'invoiceNo': 'B-1',
        'where'    : 'Busan'
    },
    {
        'invoiceNo': 'J-1',
        'where'    : 'Jeju'
    },
]

ORIGIN_DATA = {
    'S-1': { 'partner': 'GangNam-Gu' },
    'J-1': { 'partner': 'SeoGuiPo-Gu' },
    'D-1': { 'partner': 'DalSeo-Gu' },
}


def matching_data(read_data):
    result = { }
    print('read_data:', read_data, ' | PID:', os.getpid())
    read_invoice = read_data['invoiceNo']

    if read_invoice in ORIGIN_DATA:
        result.setdefault(read_invoice, {
            'invoice': read_invoice,
            'partner': ORIGIN_DATA[read_invoice]['partner'],
            'where'  : read_data['where'],
        })

    else:
        result.setdefault(read_invoice, {
            'invoice': read_invoice,
            'where'  : read_data['where'],
        })

    return result


if __name__ == '__main__':
    cpu_count = get_cpu_count()

    pool = multiprocessing.Pool(processes = cpu_count)
    pool_result = pool.map(
        func = matching_data,
        iterable = READ_DATA
    )
    print(type(pool_result), pool_result)
