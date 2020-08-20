lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)  # item1
print(second_item)  # item2
print(third_item)  # item3
print(rest)  # ['item4', 'item5']
