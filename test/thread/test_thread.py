# def make_sum():
#     sum_result = 0
#
#     for i in range(0, 1000000):
#         sum_result += sum_result + i


# def get_invoice(url: str):
#     try:
#         res = urlopen(url)
#         print(currentThread().getName(), ':', json.loads(res.read()))
#
#     except Exception as e:
#         print(e)

from test.thread.my_thread import MyThread


def main():
    """
    기본 Thread
    """
    total_count = 10
    complete_count = 0

    # while True:
    #     threads_list = []
    #
    #     if total_count <= complete_count: break;
    #
    #     for n in range(0, THREAD_LIMIT):
    #         thread = Thread(target = get_invoice, name = 'Thread @ {num} @ '.format(num = str(n)),
    #                         args = ('http://192.168.1.241:8080/cron/invoice/test_get',))
    #         threads_list.append(thread)
    #
    #     for t in threads_list:
    #         t.start()
    #
    #     for t in threads_list:
    #         t.join()
    #
    #     del threads_list
    #     complete_count = complete_count + THREAD_LIMIT

    while True:
        thread_list = []

        if total_count <= complete_count:
            break

        for n in range(0, THREAD_LIMIT):
            thread_list.append(MyThread(name = 'Thread @ {num} @ '.format(num = str(n))))

        for th in thread_list:
            th.start()

        for th in thread_list:
            th.join()

        del thread_list
        complete_count = complete_count + THREAD_LIMIT

    print('ALL THREAD IS DONE')


THREAD_LIMIT = 10

if __name__ == '__main__':
    main()

# if __name__ == '__main__':
"""
Thread  Pool Executor
Process Pool Executor
"""
#     pool = ThreadPoolExecutor(max_workers = 4, thread_name_prefix = 'Test')
#     # pool = ProcessPoolExecutor(max_workers = 4)
#
#     # future = pool.submit(get_invoice, 'http://192.168.1.241:8080/cron/invoice/test_get', str(0))
#     # future = pool.submit(make_thread)
#     print('Start Time : ', time.gmtime(time.time()))
#
#     future = pool.submit(make_sum)
#     print(future.result())
#     print(future.done())
#
#     print('Finish Time : ', time.gmtime(time.time()))
