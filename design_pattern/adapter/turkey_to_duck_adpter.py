from design_pattern.adapter.duck_interface import DuckInterface
from design_pattern.adapter.turkey_interface import TurkeyInterface


class TurkeyToDuckAdapter(DuckInterface):

    def __init__(self, _Turkey: TurkeyInterface):
        self._Turkey = _Turkey

    def quack(self):
        self._Turkey.gobble()

    def fly(self):
        self._Turkey.fly()
