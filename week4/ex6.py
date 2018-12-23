'''
    digits = 2
    letters = 9
'''

word = 'w3resource9'
digits = 0
letters = 0

for w in word:
    if w in '0123456789':
        digits += 1
    else:
        letters += 1

print('digits =', digits, 'letters =', letters)