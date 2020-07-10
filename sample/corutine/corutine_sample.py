def grep_word(word):
    print('[Start Coroutine]')
    n = 0

    while True:
        line = yield
        if word in line:
            n += 1
            print(line, n)


"""
코루틴으로 시작하기 위해서는 next()를 꼭 실행주어야합니다.
제너레이터와 동일하게, 코루틴도 함수를 바로 시작할 수는 없습니다. 
대신 응답에서 __next__()와 send() 메소드를 사용해서 실행합니다. 
그러므로, yield문에서 실행될 수 있도록 next()를 실행 해 주어야합니다.
.close() 메소드를 사용해서 코루틴을 닫을 수도 있습니다.
"""
if __name__ == '__main__':
    search = grep_word('Python')
    next(search)

    search.send('Hello Java')
    search.send('Hello PHP')
    search.send('Hello Python')
    search.send('Hello Java')
    search.send('Hello PHP')
    search.send('Hello Python')

    search.close()

    search.send('Hello Java')
    search.send('Hello PHP')
    search.send('Hello Python')
