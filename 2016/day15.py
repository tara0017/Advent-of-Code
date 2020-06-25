#day15
discs = []  #(positions, starting_location)

f = open('day15_input.txt', 'r')
for x in f:
    x = x.replace('.', '')
    x = x.split()
    #print(x[3], x[-1])
    discs.append((int(x[3]), int(x[-1])))

discs.append((11, 0))
for d in discs:
    print(d)

time = 6

while True:
    answer_found = True
    #loop through the discs
    for i in range(len(discs)):
        #if ball doesn't fall through
        if (1 + i + time + discs[i][1]) % discs[i][0] != 0:
            answer_found  = False
            #print(time, discs[i])
            break
    if answer_found:
        print(time)
        break
    else:
        time += 19


    










