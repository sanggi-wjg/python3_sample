from design_pattern.factory.abstract_factory.pizza_factory import PizzaFactory, SeoulPizzaFactory, BusanPizzaFactory


class PizzaStore:

    def order_pizza(self, pizza_factory: PizzaFactory, pizza_type: str):
        pizza = pizza_factory.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

    def create_pizza(self, pizza_type: str):
        raise NotImplementedError('Not implemented create_pizza()')


if __name__ == '__main__':
    pizza_store = PizzaStore()
    pizza_store.order_pizza(SeoulPizzaFactory(), 'cheese')

    pizza_store = PizzaStore()
    pizza_store.order_pizza(BusanPizzaFactory(), 'cheese')
