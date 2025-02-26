import sys

def calculate_min_multiple(n):
    multiple = int('1' * len(str(n)))
    while True:
        if multiple % n == 0:
            break
        multiple = multiple * 10 + 1
    return multiple


for line in sys.stdin:
    multiple = calculate_min_multiple(int(line))    
    print(len(str(multiple)))