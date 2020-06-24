class Pizza:
    name = ''
    style = ''

    def prepare(self):
        print('({}) {} preparing'.format(self.style, self.name))

    def bake(self):
        raise NotImplementedError('Not implemented bake()')

    def cut(self):
        print('({}) {} cutting'.format(self.style, self.name))

    def box(self):
        print('({}) {} boxing'.format(self.style, self.name))


class CheesePizza(Pizza):
    name = 'Cheese Pizza'

    def bake(self):
        print('({}) {} cheese topping'.format(self.style, self.name))


class CheesePizza_Seoul(CheesePizza):
    style = 'Seoul'

    def bake(self):
        super().bake()
        print('It\'s {} Style! add something'.format(self.style))


class CheesePizza_Busan(CheesePizza):
    style = 'Busan'

    def bake(self):
        super().bake()
        print('It\'s {} Style! add shrimp'.format(self.style))
