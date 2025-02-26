class Employee:
    total_employee = 0
    def __init__(self, name, salary):
        Employee.total_employee += 1
        self.name = name
        self.salary = salary
    
    def show_total_employees():
        print(f'Total employees: {Employee.total_employee}')
    
    def show(self):
        print(f'{self.name}: R${self.salary}')
    
    def __str__(self):
        return self.name
    
employee_1 = Employee("Kebler Eulalio", 2000)
employee_2 = Employee("João Nogueira", 1000)

Employee.show_total_employees()

print("-" * 50)
employee_1.show()
employee_2.show()

print("-" * 50)
Employee.show(employee_1)
Employee.show(employee_2)

print("-" * 50)
print(employee_1)
print(employee_2)





        