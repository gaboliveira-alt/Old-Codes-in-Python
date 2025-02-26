class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
    
    def honk(self):
        print('Beep beep')

my_car = Car('Audi', 'Yellow', 'Toyota')

my_car.honk()

        