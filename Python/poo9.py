class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        self._odometer = odometer
    
    def describe_car(self):
        print(self.year, self.model)
    
    def read_odometer(self):
         print("Odometer:", self._odometer, "miles")

my_car = Car("Audi", 2020, 15000)

print(my_car._odometer)

        