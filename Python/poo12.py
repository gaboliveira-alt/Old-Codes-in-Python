class Car:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        self.__odometer = odometer
    
    def _describe_car(self):
        print(self.year, self.model)
    
    def __read_odometer(self):
         print("Odometer:", self.__odometer, "miles")

my_car = Car("Audi", 2020, 15000)

my_car._describe_car()

my_car.__read_odometer()


        