# Solution 1
for n in range(7):
    if n > 0 and n%3 == 0:
        continue
    print(n, end=' ')

print()

# Solution 2
for n in range(7):
    if n == 3 or n == 6:
        continue
    print(n, end=' ')
