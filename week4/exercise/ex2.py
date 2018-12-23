# Solved by For-loop
result = 0
for n in range(10):
    # Equivalent to result = result + n
    result += n
print('result from For:', result)


# Solved by While-loop
k = 1
result = 0
while k <= 9:
    result += k
    k += 1
print('Result from While:', result)


# Solved by series formula
n = 9
formula = n*(n+1)//2
print('result from formula =', formula)
