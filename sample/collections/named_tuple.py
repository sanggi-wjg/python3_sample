import collections

if __name__ == '__main__':
    Person = collections.namedtuple(typename = 'Person', field_names = 'name age gender')
    print(type(Person), Person, Person.__doc__)

    bob = Person(name = 'bob', age = 30, gender = 'male')
    print(type(bob), bob, bob.__doc__)
    print(bob.name, bob.age, bob.gender)

    jane = Person(name = 'jane', age = 20, gender = 'female')
    print(type(jane), jane)
    print(jane.name, jane.age, jane.gender)

    for p in [bob, jane]:
        print(p)


    def check(obj: Person):
        if isinstance(obj, Person):
            print(obj, 'is Person instance')
        else:
            print(obj, 'is not Person instance')


    check(jane)

    print('#############################################')
    Point = collections.namedtuple('Point', ['x', 'y'])
    p1 = Point(11, 22)
    print(p1, p1._asdict())

    print('#############################################')
    with_class = collections.namedtuple('WithClass', 'name class age gender', rename = True)
    print(with_class._fields)

    two_ages = collections.namedtuple('TwoAge', 'name age gender age', rename = True)
    print(two_ages._fields)
