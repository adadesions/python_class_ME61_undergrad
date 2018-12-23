num_even, num_odd = 0, 0

for x in range(1, 10):
    if x%2 == 0:
        num_even += 1
    else:
        num_odd += 1

print('Number of even number:', num_even)
print('Number of odd number:', num_odd)
