dup_set = { 'apple', 'banana', 'banana', { 123 } }
print(type(dup_set), dup_set)

dup_set = set(list(set(dup_set)))
print(type(dup_set), dup_set)
