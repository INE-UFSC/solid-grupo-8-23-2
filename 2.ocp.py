from abc import ABC, abstractmethod


"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""
class Animal(ABC):
    def __init__(self, name: str, sound=None):
        self.name = name
        self.sound = sound
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        return self.sound

"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        pass
    
class FavDiscount(Discount):
    def __init__(self, customer, price):
        super().__init__(customer, price)

    def give_discount(self):
        return self.price * 0.2
            
class VIPDiscount(Discount):
    def __init__(self, customer, price):
        super().__init__(customer, price)

    def give_discount(self):
        return self.price * 0.4
    