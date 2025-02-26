def profitable(d1, d2):
    area = d1 * d2
    invest = area > 700
    return invest


buy = profitable(90, 120)
print(buy)
