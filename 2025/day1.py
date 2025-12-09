# Day 1

f = open('day1.txt','r')

dial = 50
count = 0
count2 = 0

for x in f:
    x = x.strip()

    turn = int(x[1:])
    if turn >= 100:
        count2 += turn // 100
        turn %= 100
        
    if x[0] == 'L':
        if dial != 0 and dial - turn < 0:
            count2 += 1
            
        dial = (dial + 100 - turn) % 100

    elif x[0] == 'R':
        if dial != 0 and dial + turn > 100:
            count2 += 1
            
        dial = (dial + turn) % 100

    if dial == 0:
        count += 1
        
print(count)
print(count2 + count)
