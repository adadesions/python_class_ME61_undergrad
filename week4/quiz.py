width = int(input('Width: '))
length = int(input('Length: '))

print('o'*length)

for w in range(width-2):
    print('o'+'#'*(length-2)+'o')

print('o'*length)
