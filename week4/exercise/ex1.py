n = input('Enter some number: ')
try:
    n = int(n)
    for mul in range(1, 13):
        print('{0}x{1} = {2}'.format(n, mul, n*mul))
except ValueError:
    print('Please only enter interger.')