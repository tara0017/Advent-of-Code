#day3
def is_triangle(s):
    sides = []
    for i in s:
        sides.append(int(i))
    m = max(sides)
    sides.remove(m)
    if m < sum(sides):
        return True
    return False


count = 0

c = 0
f = open('day3_input.txt', 'r')
for x in f:
    x = x.split()
    if c%3 == 0:
        r = x[:]
    elif c%3 == 1:
        s = x[:]
    elif c%3 == 2:
        t = x[:]
        #print(r, s, t)
        for i in range(3):
            if is_triangle([r[i], s[i], t[i]]):
                count += 1
    c += 1
    #if is_triangle(x):
    #    count += 1

print(count)        




