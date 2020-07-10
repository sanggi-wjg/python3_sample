def create_number_generator():
    for i in range(1, 11):
        yield i


if __name__ == '__main__':
    """
    제너레이터는 이터레이터지만 단 한 번만 반복합니다. 
    메모리에 모든 값을 저장하지 않기 때문에 값을 사용할 때 즉시 생성합니다. 
    'for'루프를 사용하거나 반복하는 함수나 구조에 생성된 값들을 전달하여 반복을 통해 사용합니다. 
    대부분의 제너레이터들은 함수로 구현 됩니다. 
    그러나, 값을 반환하지않고, 산출(yield)될 뿐입니다
    """
    for n in create_number_generator():
        print(n)
