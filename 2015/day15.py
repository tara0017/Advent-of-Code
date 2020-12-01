# day15
def find_highest_score():
    global ingredients, highest_score, winner

    # create all combinations of ingrediants totaling 100 tspns
    for sp in range(100):
        for pe in range(100):#(100 - sp):
            if sp + pe > 100:
                break
            for fr in range(100): #100 - (sp + pe)):
                if fr + sp + pe > 100:
                    break
                for su in range(100): #100 - (sp + pe + fr)):
                    if su + fr + sp + pe > 100:
                        break
                    
                    totals = []     # [cap, dur, fla, tex, cal]
                    for i in range(1, 6):
                        totals.append(sp * ingredients[0][i] + pe * ingredients[1][i] + fr * ingredients[2][i] + su * ingredients[3][i])

                    # part 2
                    # recipe must have exactlt 500 calories
                    if totals[-1] != 500:
                        continue

                    #if there are any 0's or negative values score is automatically 0
                    if min(totals) <= 0:
                        score = 0
                    else:
                        #calculate total score
                        score = 1
                        for t in totals[:-1]:
                            score *= t

                    # update highest score
                    if score > highest_score:
                        highest_score = score
                        winner = (score, sp, pe, fr, su)

# global variables
ingredients = []
highest_score = 0
winner = ()

f = open('day15.txt', 'r')
for x in f:
    x = x.replace(':', '').replace(',', '')
    x = x.split()

    # [name, capacity, durability, flavor, texture, calories]
    ingredients.append([x[0], int(x[2]), int(x[4]), int(x[6]), int(x[8]), int(x[10])])

for i in ingredients:
    print(i)

find_highest_score()
print(winner)   
