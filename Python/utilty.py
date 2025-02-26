def float_to_currency(value):
    man, dec = map(int, f'{value:0.2f}'.split('.'))
    
    thousands = []
    while man != 0:
        thousands.insert(0, str(m % 1000))
        man = man // 1000
        if man == 0:
            break
        
    m = ','.join(thousands)
    return f'R${man}.{dec}'