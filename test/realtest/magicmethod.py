class MagicClass:

    def __new__(cls, *args, **kwargs):

        print('args len :', args.__len__(), args)

        if len(args) < 1:
            return 'Args Is None'
        else:
            return 'Singular Strike'

    def __init__(self, num, txt):
        self.num = num
        self.txt = txt

    def __repr__(self):
        return self.num, self.txt


_MagicClass = MagicClass(0, '123')

print(_MagicClass)
