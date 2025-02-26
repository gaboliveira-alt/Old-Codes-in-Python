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
        print('Woof!')

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        
        self.breed = breed
        self.age = age
    
    def sound(self):
        print('Meow')
        
my_dog = Dog('Jax', 'Bulldog', 5)
my_cat = Cat('Lily', 'Ragdoll', 5)

my_dog.sound()
my_cat.sound()

        
        