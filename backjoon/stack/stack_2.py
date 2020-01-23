def isVps(psList: list):
    cnt = 0

    for i in range(0, psList.__len__()):
        ps = psList[i]

        if i == 0 and ps == ')':
            return 'NO'

        if ps == '(':
            cnt = cnt + 1
        elif ps == ')':
            if cnt == 0:
                return 'NO'
            else:
                cnt = cnt - 1

    if cnt != 0:
        return 'NO'

    return 'YES'


if __name__ == '__main__':
    T = int(input())
    result = []

    for t in range(0, T):
        result.append(isVps(list(input())))

    for res in result:
        print(res)
