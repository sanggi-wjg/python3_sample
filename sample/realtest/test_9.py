import psutil

# cpu_count = psutil.cpu_count()
cpu_count = 4
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def divide_list(data, n):
    for i in range(0, len(data), n):
        yield data[i:i + n]


result = divide_list(sample, len(sample) // cpu_count)
print([r for r in result])
