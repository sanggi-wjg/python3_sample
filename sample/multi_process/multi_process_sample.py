import multiprocessing

import numpy
import psutil


class SampleClass:

    def __init__(self):
        self._dataList = { 1: 'a', 2: 'b', 3: 'c' }

    def divide_data(self, sample, count):
        return numpy.array_split(sample, count)

    def get_cpu_count(self):
        return psutil.cpu_count()

    def multi_process_func(self, data):
        res = dict()

        for d in data:
            if d in self._dataList.keys():
                res.setdefault(d, self._dataList.get(d))
            else:
                res.setdefault(d, str(d))

        return res

    def main(self):
        sampleData = [1, 4, 5, 2, 6, 7, 3]
        # sampleData_2 = [1, 2, 3, 4, 5, 6, 7, 8]
        # sampleData_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        result = list()

        pool = multiprocessing.Pool(processes = self.get_cpu_count())
        result.append(pool.map(self.multi_process_func, self.divide_data(sampleData, self.get_cpu_count())))
        pool.close()
        pool.join()

        return result


if __name__ == '__main__':
    # sampleClass = SampleClass()
    # result = sampleClass.main()
    # print(result)

    # print("1".rjust(4, '0'))

    sample = ['1']
    if sample:
        print('IF')
    else:
        print('ELSE')
