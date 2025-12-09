# Day 3

def get_largest(lst):
    
    mx = max(lst)
    mx_ind = lst.index(mx)
    #print(lst, mx, mx_ind)

    # max is last digit
    if mx_ind == len(lst) - 1:
        mx2 = max(lst[:-1])
        return (10 * mx2 + mx)
    else:
        mx2 = max(lst[mx_ind + 1:])
        return (10 * mx + mx2)


def get_next_digit(lst, num_digits_needed):
    for i in range(9,0,-1):
        if i in lst:
            if lst.index(i) <= len(lst) - num_digits_needed:
                return i
    
        
def get_largest2(lst):
    mx = ''

    while len(mx) < 12:
        d = get_next_digit(lst, 12 - len(mx))
        mx += str(d)
        lst = lst[lst.index(d) + 1:]

    return int(mx)


    
joltage = 0
joltage2 = 0

f = open('day3.txt','r')
for x in f:
    x = x.strip()
    #print(x)
    
    #convert to int list
    lst = list()
    for c in x:
        lst.append(int(c))
        
    joltage  += get_largest(lst)
    joltage2 += get_largest2(lst)

print(joltage)
print(joltage2)    

