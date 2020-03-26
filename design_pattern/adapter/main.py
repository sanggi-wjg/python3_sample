from design_pattern.adapter.mallard_duck_impl import MallardDuckImpl
from design_pattern.adapter.turkey_to_duck_adpter import TurkeyToDuckAdapter
from design_pattern.adapter.wild_turkey_impl import WildTurkeyImpl

if __name__ == '__main__':
    m = MallardDuckImpl()
    m.quack()
    m.fly()

    t = WildTurkeyImpl()
    t.gobble()
    t.fly()

    a = TurkeyToDuckAdapter(WildTurkeyImpl())
    a.quack()
    a.fly()
