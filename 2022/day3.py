#day3

def get_priority(s1, s2):
    letters = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in s1:
        if c in s2:
            common = c
            break
    return letters.index(common)

def get_priority2(group):
    letters = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in group[0]:
        if c in group[1] and c in group[2]:
            common = c
            break
    return letters.index(common)

"""
p_sum = 0

f = open("day3.txt", "r")
for x in f:
    x = x.strip()
    #print(x, len(x))
    half = int(len(x) /2)
    first_half = x[:half]
    second_half = x[half:]
    p_sum += get_priority(first_half, second_half)
    

print(p_sum)
"""


p_sum2 = 0
group = []

f = open("day3.txt", "r")
for x in f:
    x = x.strip()
    
    group.append(x)
    if len(group) == 3:
           
        p_sum2 += get_priority2(group)
        group.clear()
           
    

print(p_sum2)









