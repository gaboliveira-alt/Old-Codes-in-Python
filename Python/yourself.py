class introduce_yourself:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def hello(self):
        print(f'{self.name} {self.age} {self.height}')
        
        
hello = introduce_yourself("Gabriel", 18, 1.79)
hello.hello()
