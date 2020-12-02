# day2
def is_valid_password(x):
    least = int(x[0])
    most  = int(x[1])
    char  = x[2]
    pwd   = x[3]

    num = 0
    for c in pwd:
        if c == char:
            num += 1
    if num >= least and num <= most:
        return True
    return False


def is_valid_password2(x):
    i = int(x[0]) - 1
    j = int(x[1]) - 1
    char  = x[2]
    pwd   = x[3]

    if pwd[i] != pwd[j]:
        if pwd[i] == char or pwd[j] == char:
            return True
    return False


count  = 0
count2 = 0

f = open('day2.txt', 'r')
for x in f:
    x = x.replace('-', ' ')
    x = x.replace(':', '')
    x = x.split()
    if is_valid_password(x):
        count += 1
    if is_valid_password2(x):
        count2 += 1
        
print('valid passwords part 1:', count)
print('valid passwords part 2:', count2)
