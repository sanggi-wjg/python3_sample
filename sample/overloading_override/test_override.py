class Override_Parents(object):

    def print(self, text: str):
        print(self)
        raise NotImplementedError


class Override_1(Override_Parents):
    def print(self, text: str):
        print(text)


class Override_2(Override_Parents):
    def print(self, text: str):
        print(len(text))


if __name__ == '__main__':
    override1 = Override_1()
    override2 = Override_2()

    sample = '123 abc'

    override1.print(sample)
    override2.print(sample)
