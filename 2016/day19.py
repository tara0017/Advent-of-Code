#day19
def opposite(i):
    global elves

    index = int(len(elves) / 2) + i
    return (index % len(elves))


elves = []

for i in range(3004953):
    elves.append(i)


index = 0
while len(elves) > 1:
    #print(elves, int(len(elves)/2))
    opp_index = opposite(index)
    #print(opp_index)
    elves.pop(opp_index)
    if opp_index < index:
        adjust = -1
    else:
        adjust = 0
    index = (index + 1 + adjust) % len(elves)
    if len(elves) % 500000 == 0:
        print(len(elves))
    

#print(elves)
print(elves[0] + 1)


    

    
    



