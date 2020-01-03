#day4
def is_never_decreasing(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True


def has_same_adjacent_digits(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def has_two_adjacent_digits(n):
    s = str(n)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if (i+2) >= len(s):
                if s[i-1] != s[i]:
                    return True
            elif s[i+2] != s[i]:
                if i == 0:
                    return True
                elif s[i-1] != s[i]:
                    return True
    return False


data_range = [357253, 892942]
count = 0

#part2
for i in range(data_range[0], data_range[1] + 1):
    if is_never_decreasing(i):
        if has_two_adjacent_digits(i):
            count += 1
print (count)

"""
#part1
for i in range(data_range[0], data_range[1] + 1):
    if is_never_decreasing(i):
        if has_same_adjacent_digits(i):
            count += 1
print (count)
"""
