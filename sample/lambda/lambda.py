print_sum = lambda a, b: print(a + b)
print_formatted = lambda a, b: print("A : {a} | B : {b}".format(a = a, b = b))
positive_int_list = list(filter(lambda x: x > 0, [-5, -6, 7, 8]))

print_to_server = lambda msg, *args: print('\033[91m', msg, *args, '\033[0m')

if __name__ == '__main__':
    # print_sum(1, 2)
    # print_formatted(3, 4)
    # print(positive_int_list)
    print('123')
    print_to_server(123)
    print_to_server('abc')
    print_to_server('123', 123123, 'dsfkldslkfn')
    print('123dfsd')
    print(("123",))
