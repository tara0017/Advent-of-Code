# day23 part 1

def play_round():
    global cups, current_cup

    # get 3 cups clockwise of current cup
    three_to_move = []
    for i in range(3):
        ind = (cups.index(current_cup) + 1) % len(cups)
        n = cups.pop(ind)
        three_to_move.append(n)

    # get destination cup
    destination_cup = current_cup - 1
    while destination_cup not in cups:
        destination_cup -= 1
        if destination_cup < min(cups):
            destination_cup = max(cups)

    # place 3 cups after destination cup
    dest_ind = cups.index(destination_cup)
    cups = cups[:dest_ind + 1] + three_to_move + cups[dest_ind + 1:]

    # update current cup
    curr_ind = (cups.index(current_cup) + 1) % len(cups)
    current_cup = cups[curr_ind]


def get_labels():
    global cups
    s = ''
    ind = cups.index(1)
    for i in range(ind + 1, ind + len(cups)):
        s += str(cups[i % len(cups)])

    return s
    
 

cups = [2,5,3,1,4,9,8,6,7]
current_cup = cups[0]
destination_cup = None

move = 1
while move <= 100:
    play_round()
    move += 1


print('Part 1:', get_labels())

