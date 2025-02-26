from random import randint

class BloodType:
    def __init__(self, data):
        if isinstance(data, BloodType):
            self.type = data.type
            self.rh_factor = data.rh_factor
        elif isinstance(data, str):
            self.type, self.rh_factor = self.__validate_str(data)
        else:
            raise TypeError("Invalid data type")

    def __validate_str(self, data):
        if (len(data) < 2) or (len(data) < 3):
            raise ValueError(f'Invalid string format: {data}')
        
        rh_factor = ('+', '-')
        blood_types = ('A', 'B', 'AB', 'O')
        type, rh = data[0:-1], data[-1]
        
        if rh not in rh_factor:
            raise ValueError(f'Invalid rh factor: {rh}')
        if type not in blood_types:
            raise ValueError(f'Invalid Blood Type: {type}')
        return (type, rh)
    
    def __str__(self):
        return f'{self.type}{self.rh_factor}'
    
    def __repr__(self):
        return f'BloodType({self.type}{self.rh_factor})'
    
    def can_donate_to(self, other):
        if not isinstance(other, BloodType):
            raise ValueError(f'not istance of Bloodtype: {other}')
        
        if (self.rh_factor == '+') and (other.rh_factor == '-'):
            return False
        
        if self.type == 'O':
            return True
        elif self.type in other.type:
            return True
        
        return False


class Donor:
    def __init__(self, name, age, blood_type):
        self.name = name
        self.age = age
        self.blood_type = BloodType(blood_type)
    
    def __str__(self):
        return f'{self.name},{self.age},{self.blood_type}'
    
    def __repr__(self):
        return f'Donor({self.name},{self.age},{self.blood_type})'
    
    def can_donate_to(self, other):
        return self.blood_type.can_donate_to(other.blood_type)


def main():
    blood_types = ('A', 'B', 'AB', 'O')
    rh_factor = ('+', '-')
    donors = []
    
    for type in blood_types:
        for rh in rh_factor:
            blood_type = f'{type}{rh}'
            name = f'Donor {blood_type}'
            age = randint(16, 60)
            donors.append(Donor(name, age, blood_type))
            
    
    for donor in donors:
        for other in donors:
            can_donate = donor.can_donate_to(other)
            print(f'{str(donor):<18} ==> {str(other):<18}: {can_donate}')

if __name__ == '__main__':
    main()
        