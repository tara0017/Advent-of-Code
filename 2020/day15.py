# day15

data = [1,0,15,2,10,13]

numbers = dict()
turn = 0
last_value = None

# add initial input data
for v in data:
    turn += 1
    numbers[v] = [turn]
    last_value = v

# play game
while True:
    turn += 1

    if len(numbers[last_value]) == 1:   # first time it was spoken
        # update last value
        last_value = 0

    else:   #number has appeared before
        # update last value
        indices = numbers[last_value]
        last_value = indices[-1] - indices[-2]  # age
        
    # add turn to index of new spoken value
    if last_value not in numbers:
        numbers[last_value] = [turn]
    else:
        numbers[last_value].append(turn)

    if turn == 2020:     # part 1
        print('part 1')
        print(turn, last_value) 
    
    if turn == 30000000: # part 2
        print('part 2')
        print(turn, last_value)  
        break



