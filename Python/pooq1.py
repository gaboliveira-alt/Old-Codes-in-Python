import pooqutils

class BankAccount:
    __last_account_number = 0
    def __init__(self, holder):
        BankAccount.__last_account_number += 1
        self.number = BankAccount.__last_account_number
        self.holder = holder
        self.balance = 0.0
    
    def deposit(self, ammount):
        if ammount < 0:
            return False
        self.balance += ammount
        return True
    
    def withdraw(self, ammount):
        if (ammount < 0) or (self.balance < ammount):
            return False
        self.balance -= ammount
        return True
    
    def print_balance(self):
        print("BANCO EXEMPLO S/A")
        print("SALDO DA CONTA")
        print("Conta: ",self.number)
        print("Titular: ",self.holder)
        print("Saldo: ", pooqutils.float_to_currency(self.balance))
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        currency = pooqutils.float_to_currency(self.balance)
        return f'BankAccount({self.holder}, {currency})'
    

for k in range(10):
    account = BankAccount(f'Titular: {k}')
    account.print_balance()
    print()

        