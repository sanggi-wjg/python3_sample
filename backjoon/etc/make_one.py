if __name__ == '__main__':
    N = int(input())
    loopCnt = 0

    while True:
        if N == 1: break

        if N % 3 == 0:
            N = N / 3
        elif N % 2 == 0:
            if (N - 1) % 3 == 0:
                N = N - 1
            else:
                N = N / 2
        else:
            N = N - 1

        loopCnt = loopCnt + 1

    print(loopCnt)
