def create_generator():
    print('1')
    yield 1

    print('2')
    yield 2
    
    print('3')
    yield 3


g = create_generator()
next(g)
next(g)
next(g)
