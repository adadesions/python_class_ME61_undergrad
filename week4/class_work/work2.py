data = [3, 5, 2, 8, 12, 6, 7]
num_even = 0
num_odd = 0

for d in data:
    if d%2 == 0:
        num_even += 1
        print('Even number:', d)
    else:
        num_odd += 1
        print('Odd number:', d)
else:
    print('Ther are', num_even, 'even numbers')
    print('Ther are', num_odd, 'odd numbers')
    print('End of loop')
