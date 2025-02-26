class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print('Moving')

class Dog(Animal):
    def bark(self):
        print('Woof')
        
my_dog = Dog('bob')

print(my_dog.name)
my_dog.move()

my_dog.bark()

        