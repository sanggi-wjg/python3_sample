from design_pattern.adapter.duck_interface import DuckInterface


class MallardDuckImpl(DuckInterface):

    def quack(self):
        print('Quack')

    def fly(self):
        print('DuckDuck Fly')
