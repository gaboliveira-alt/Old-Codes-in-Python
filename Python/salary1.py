seller_name = input()
fixed_salary = float(input())
total_sale = float(input())

percentual = total_sale * 0.15
total_salary = fixed_salary + percentual

print(f'TOTAL = R$ {total_salary:.2f}')