# day2

def get_area(x):
    l = int(x[0])
    w = int(x[1])
    h = int(x[2])

    a = l * w
    b = l * h
    c = w * h

    return 2 * (a + b + c) + min(a, b, c)


def calc_ribbon(x):
    l = int(x[0])
    w = int(x[1])
    h = int(x[2])

    wrap = 2 * (l + w + h - max(l,w,h))
    bow  = l * w * h
    return wrap + bow


total_area = 0
total_ribbon  = 0

f = open("day2.txt", "r")
for x in f:
    x = x.replace("\n", "")
    x = x.split("x")
    total_area += get_area(x)

    total_ribbon += calc_ribbon(x)

print(total_area)
print(total_ribbon)

