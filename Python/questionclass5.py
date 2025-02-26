class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        if age <= 0:
            raise Exception(f'Invalid Age: {age}')
        self.__age = age