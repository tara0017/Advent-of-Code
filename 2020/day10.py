# day10

def get_values_at_most_three_away(v):
    values = []
    
    for d in data:
        if d > v and d <= 3+v:
            values.append(d)
    return values



# read file
data = []
f = open('day10.txt','r')
for x in f:
    data.append(int(x))

# add starting point
data.append(0)

# add ending point
m = max(data)
data.append(3 + m)
data.sort()


# part 1
diff_one = 0
diff_three = 0
for i in range(len(data)-1):
    if data[i+1] == 1 + data[i]:
        diff_one += 1
    elif data[i+1] == 3 + data[i]:
        diff_three += 1

print('Part 1:', diff_one, diff_three, diff_one*diff_three)


# part 2
# tree_size[ consecutive numbers] = branches (sum of previous 3 entries)
tree_size = dict()
tree_size[1] = 1
tree_size[2] = 1
tree_size[3] = 2
tree_size[4] = 4
tree_size[5] = 7
tree_size[6] = 13       # tree_size[5] + tree_size[4] + tree_size[3] 

# track number of branches
total_branches = 1

# consecutive numbers with a difference of 1
consec_numbers = 1

# set v to starting value (0)
v = data.pop(0)

for n in data:
    #next value is 1 away (consecutive number)
    if n == v+1:
        consec_numbers += 1
    else:   #difference of 3
        #update the total number of branches
        total_branches *= tree_size[consec_numbers]

        # reset the consecutive number count
        consec_numbers = 1

    # update v to new value
    v = n


print('Part 2:', total_branches)



