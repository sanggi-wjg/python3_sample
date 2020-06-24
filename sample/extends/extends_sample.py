class Parents(object):

    def show(self):
        raise NotImplementedError()


class Child(Parents):

    def show(self):
        print('This is child')


child = Child()
child.show()
