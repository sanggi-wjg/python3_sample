from design_pattern.adapter.turkey_interface import TurkeyInterface


class WildTurkeyImpl(TurkeyInterface):

    def gobble(self):
        print('Gobble')

    def fly(self):
        print('Turkey Flying')
