# day1
floor = 0
position = 0

f = open("day1.txt", "r")
for x in f:
    for i in x:
        position += 1
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        if floor == -1:
            print(position)
            break

print(floor)

