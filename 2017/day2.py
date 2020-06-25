#day2
def get_difference(s):
    biggest = 0
    smallest = 10**6
    for n in s:
        n = int(n)
        if n > biggest:
            biggest = n
        if n < smallest:
            smallest = n
    return biggest - smallest

def find_divisors(x):
    values = []
    for n in x:
        values.append(int(n))
    for i in values:
        for j in values:
            if j != i and i % j == 0:
                return i/j


    
total = 0
f = open("day2_input.txt", "r")
for x in f:
    x = x.split()
    div = find_divisors(x)
    total += div

print(total)

"""
#part 1
for x in f:
    x = x.split()
    diff = get_difference(x)
    total += diff

print(total)
"""
