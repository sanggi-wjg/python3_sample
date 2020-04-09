from time import sleep

LIMIT = 10
dataCount = 25
completeCount = 0

while True:
    if completeCount >= dataCount:
        break

    for i in range(LIMIT):
        if completeCount >= dataCount:
            break
        sleep(0.1)

        completeCount += 1
        print('completeCount : ', completeCount)
