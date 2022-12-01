#Day 1

f = open("day1.txt", "r")
cal = 0
calories = []
largest = [0,0,0]

for x in f:
    if x == '\n':
        calories.append(cal)
        if cal >= min(largest):
            largest.remove(min(largest))
            largest.append(cal)
        cal = 0
    else:    
        cal += int(x)
    
print("Part 1:", max(largest))
print("Part 2:", sum(largest))

