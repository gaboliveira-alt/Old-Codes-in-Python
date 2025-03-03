def greeting(name, greet = 'Oi', sufix = '!'):
    return f'{greet}, {name}{sufix}'

def sum(*args):
    values_sum = 0
    for value in args:
        values_sum += value
    return values_sum

def print_sum(prompt, *numbers):
    print(prompt, sum(numbers))
    
def sample(a, b, *pargs, **kwargs):
    print('a\t', a)
    print('b\t', b)
    print('pargs\t', pargs)
    print('kwargs\t', kwargs)

