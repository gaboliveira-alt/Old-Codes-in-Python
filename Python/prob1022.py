def read_input():
    rat1_num, _, rat1_den, operator, rat2_num, _, rat2_den = input().split()
    return {
        'rational1': (int(rat1_num), int(rat1_den)),
        'rational2': (int(rat2_num), int(rat2_den)),
        'operator': operator,
    }
    

def rational_operation(operation_data):
    num = 0
    den = 1

    rat1 = operation_data['rational1']
    rat2 = operation_data['rational2']
    operator = operation_data['operator']
    
    if operator == '+':
        rat_num = (rat1[num] * rat2[den] + rat2[num] * rat1[den])
        rat_den = rat1[den] * rat2[den]
    elif operator == '-':
        rat_num = (rat1[num] * rat2[den] - rat2[num] * rat1[den])
        rat_den = rat1[den] * rat2[den]
    elif operator == '*':
        rat_num = rat1[num] * rat2[num]
        rat_den = rat1[den] * rat2[den]
    elif operator == '/':
        rat_num = rat1[num] * rat2[den]
        rat_den = rat1[den] * rat2[num]
        
    return (rat_num, rat_den)
    

def rational_simplify(rational):
    rat_num = rational[0]
    rat_den = rational[1]
    
    div = 2
    div_max = min(abs(rat_num), abs(rat_den))
    while div <= div_max:
        if (rat_num % div == 0) and (rat_den % div == 0):
            rat_num = rat_num // div
            rat_den = rat_den // div
        else:
            div = div + 1
        
    return (rat_num, rat_den)

def print_result(rational_result, rational_simplify):
    num = 0
    den = 1
    
    print(rational_result[num], '/', rational_simplify[den], '=', rational_simplify[num], '/', rational_simplify[den], sep='')


def main():
    rational_expression = int(input())
    
    while rational_expression > 0:
        rational_expression -= 1
        
        input_data = read_input()
        
        result_data = rational_operation(input_data)
        simplified_data = rational_simplify(result_data)
        
        print_result(result_data, simplified_data)
        

if __name__ == '__main__':
    main()    
    