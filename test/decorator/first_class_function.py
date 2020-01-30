def mul(x):
    return x * x


def mul_third(x):
    return x * x * x


def ret_map(func, numList):
    result = []

    for i in numList:
        result.append(func(i))

    return result


if __name__ == '__main__':
    numList = [1, 2, 3, 4, 5]

    mulMap = ret_map(mul, numList)
    mulThirdMap = ret_map(mul_third, numList)

    print(mulMap)
    print(mulThirdMap)
