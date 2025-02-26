sum_valid_scores = 0
count_valid_scores = 0

while True:
    scores = float(input())
    
    if (scores >= 0.0) and (scores <= 10.0):
        count_valid_scores += 1
        sum_valid_scores += scores
        
        if count_valid_scores == 2:
            avarege_scores = sum_valid_scores / count_valid_scores
            print(f'media = {avarege_scores:0.2f}')
            break
    else:
        print('nota invalida')
        
        
    