def fibonacci(num: int) -> int:
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    n = int(input())

    print(fibonacci(n))


