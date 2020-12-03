# day3
def check_slope(x_change,y_change):
    global tree_map
    
    tree_count = 0
    x = 0
    y = 0
    for i in range(len(tree_map) // y_change):
        if tree_map[y][x] == 1:
            tree_count += 1
        x = (x + x_change) % len(tree_map[0])
        y += y_change
    return tree_count


tree_map = []

f = open('day3.txt','r')
for x in f:
    row = []
    for c in x:
        if c == '.':
            row.append(0)
        elif c == '#':
            row.append(1)
    tree_map.append(row)


print(check_slope(1,1))
print(check_slope(3,1))
print(check_slope(5,1))
print(check_slope(7,1))
print(check_slope(1,2))


