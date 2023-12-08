#day 1

"""
returns 2 digit number
first # in tens place, last number in ones place
"""
def get_num(s):
    map_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num = 0

    for i in range(len(s)):
        if s[i].isnumeric():
            num += 10*int(s[i])
            break
        elif (i >= 2) and s[i-2:i+1] in map_dict:
            num += 10 * map_dict[s[i-2:i+1]]
            break
        
        elif (i >= 3) and s[i-3:i+1] in map_dict:
            num += 10 * map_dict[s[i-3:i+1]]
            break
        elif (i >= 4) and s[i-4:i+1] in map_dict:
            num += 10 * map_dict[s[i-4:i+1]]
            break

    
    for i in range(len(s) - 1, -1, -1):
        if (s[i]).isnumeric():
            num += int(s[i])
            break
        elif i <= len(s) - 3 and s[i:i+3] in map_dict:
            num += map_dict[s[i:i+3]]
            break
        elif i <= len(s) - 4 and s[i:i+4] in map_dict:
            num += map_dict[s[i:i+4]]
            break
        elif i <= len(s) - 5 and s[i:i+5] in map_dict:
            num += map_dict[s[i:i+5]]
            break

    return num
    
def part1(s):
    num = 0

    for i in range(len(s)):
        if s[i].isnumeric():
            num += 10*int(s[i])
            break
        
    for i in range(len(s) - 1, -1, -1):
        if (s[i]).isnumeric():
            num += int(s[i])
            break

    return num

    
total1 = 0
total2 = 0

f = open('day1.txt','r')
for x in f:
    n = part1(x)
    total1 += n
    
    #print(x, '\t')
    n = get_num(x)
    total2 += n

print('Part 1: ', total1)
print('Part 2: ', total2)
