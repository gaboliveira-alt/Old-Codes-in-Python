class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        self._odometero = odometer
    
    def describe_car(self):
        print(self.year, self.model)
    
    def read_odometer(self):
        print("Odometer: ", self._odometero, "miles")

my_car = Car("Audi", 2020, 15000)

my_car.describe_car()
my_car.read_odometer()


        