from enum import Enum


class PizzaType(Enum):
    MARGARITA = 0,
    MEXICO = 1,
    STELLA = 2


class Pizza:
    def __init__(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price


class PizzaMargarita(Pizza):
    def __init__(self):
        super().__init__(3.5)


class PizzaMexico(Pizza):
    def __init__(self):
        super().__init__(17.5)


class PizzaStella(Pizza):
    def __init__(self):
        super().__init__(5.5)


def create_pizza(pizza_type: PizzaType) -> Pizza:
    factory_dict = {
        PizzaType.MARGARITA: PizzaMargarita,
        PizzaType.MEXICO: PizzaMexico,
        PizzaType.STELLA: PizzaStella
    }
    return factory_dict[pizza_type]()


for pizza in PizzaType:
    my_pizza = create_pizza(pizza)
    print(f'Pizza type: {pizza}, price: {my_pizza.get_price()}')
