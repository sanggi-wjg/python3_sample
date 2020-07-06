data = {
    '02': 1,
    '10': 2,
    '11': 3,
    '23': 4,
    '31': 5,
    '99': 6,
}

result = dict(filter(lambda x: int(x[0]) > 30, data.items()))
print(result)
print(sum(result.values()))

