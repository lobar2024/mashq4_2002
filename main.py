
#3
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        if quantity > 0:
            self.status = "mavjud"
        else:
            self.status = "mavjud emas"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print("Miqdor manfiy bo‘lishi mumkin emas!")
        else:
            self.__quantity = value
            if value > 0:
                self.status = "mavjud"
            else:
                self.status = "mavjud emas"

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


# Tekshiruv
p = Product("Olma", 5)
print(p.name)
print(p.quantity)
print(p.status)

p.quantity = 0
print(p.status)
