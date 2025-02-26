number_employer = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

month_end = worked_hours * amount_per_hour

print(f'NUMBER = {number_employer}\nSALARY = U$ {month_end:.2f}')