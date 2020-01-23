def get_digit_generator(num: int) -> str:
    base = '1'

    while True:
        divideSum = int(base)
        for x in range(0, base.__len__()):
            divideSum = divideSum + int(base[x])

        if divideSum == num:
            break
        elif divideSum > num:
            base = 0
            break

        print(base)
        base = str(int(base) + 1)

    return base


N = int(input())

print("target", get_digit_generator(N))

# print(9 + 9 + 9 + 9 + 5 + 4 + 999954)