# grades = ['A', 'B', 'C', 'D', 'F', 4, 3, 2, 1, 0]
# for grade in grades:
#     print('You have got:', grade)

'''
    Match Username with their job
'''
usernames = ['Sarah', 'John', 'Toon']
jobs = ['Engineer', 'Teacher', 'Singer']

# zip function
for i, (user, job) in enumerate(zip(usernames, jobs)):
    if i == 0:
        print(i, user, job, jobs[1])
    else:
        print(i, user, job)

# Range function
for n in range(10):
    print(n)

# range(start, end)
for n in range(10, 20):
    print(n)

# range(start, end, step)
for n in range(100, 111, 2):
    if n == 104:
        break
    print(n)

print('Continue keyword')
for n in range(100, 111, 2):
    if n == 104:
        continue
    print(n)
else:
    print('End of loop')