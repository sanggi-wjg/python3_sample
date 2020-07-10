def create_infinite_generator():
    n = 0
    while True:
        n += 1
        yield n


g = create_infinite_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
