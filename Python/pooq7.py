class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
    
    def __repr__(self):
        return f'Person: {self.__name},{self.__age}'
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__age
    
    def set_age(self, age):
        if age <= 0:
            raise Exception(f'Invalid age {age}')
        self.__age = age
    
    def get_age(self):
        return self.__age


person_1 = Person("Maria Julia", 18)
person_2 = Person("Alan Turing", 120)
person_3 = Person("Bebe", 1)

print(person_1)


     