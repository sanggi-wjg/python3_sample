from design_pattern.factory.abstract_factory.menu.pizza import CheesePizza_Seoul, CheesePizza_Busan


class PizzaFactory:

    def create_pizza(self, pizza_type: str):
        pass


class SeoulPizzaFactory(PizzaFactory):

    def create_pizza(self, pizza_type: str):
        if pizza_type == 'cheese':
            return CheesePizza_Seoul()


class BusanPizzaFactory(PizzaFactory):

    def create_pizza(self, pizza_type: str):
        if pizza_type == 'cheese':
            return CheesePizza_Busan()
