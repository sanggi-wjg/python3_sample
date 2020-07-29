def test(*fields, **expression):
    field_name = list(fields)
    print(type(fields), fields)
    print(type(field_name), field_name)

    for name in field_name:
        print(type(name), name)

    print()


test('idx', 'productCd', 'packageCd')

sample = 'idx', 'productCd', 'packageCd'
sample2 = 'regDate',
test(*sample, *sample2)

# sample = 'idx', 'productCd', 'packageCd'
# test(sample)
