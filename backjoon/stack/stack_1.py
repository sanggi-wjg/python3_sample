if __name__ == '__main__':
    K = int(input())
    stackList = []

    for k in range(0, K):
        inputNum = int(input())

        if inputNum != 0:
            stackList.append(inputNum)
        else:
            stackList.pop()

    result = 0
    for item in stackList:
        result = result + item

    print(result)
