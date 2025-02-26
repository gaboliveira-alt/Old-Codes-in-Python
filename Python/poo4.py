class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        print('Moving')
    

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        
        self.breed = breed
        self.age = age
        
    def bark(self):
        print('Woof')
        

my_dog = Dog('Jax', 'Bulldog', 5)

print(my_dog.name)
print(my_dog.breed)
print(my_dog.age)

        