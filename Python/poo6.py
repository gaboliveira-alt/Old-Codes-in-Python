class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print('Making a sound')

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        
        self.breed = breed
        self.age = age
    
    def sound(self):
        super().sound()
        print('Woof')
        
my_dog = Dog('Jax', 'Bulldog', 5)

my_dog.sound()
        