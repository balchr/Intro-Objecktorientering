class Car():
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        print(self.brand)

    def set_brand(self, new_brand):
        self.brand = new_brand

    def get_color(self):
        print(self.color)

    def set_color(self, new_color):
        self.color = new_color

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, new_mileage):
        self.mileage = new_mileage


a_car = Car('Volvo', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand('Renault')
a_car.get_brand()

b_car = Car("Ford", "Röd", 8)
b_car.set_color("Blå")
b_car.get_color()
mileage = b_car.get_mileage()
print(mileage)

c_car = Car("Audi", "Gul", 18888882)

d_car = Car("WV", "Grön", 1221)

lista  = [a_car, b_car, c_car, d_car]

for i in lista:
    i.get_brand()
