# day23 part 2

class cup:
    def __init__(self, value, next_cup):
        self.value = value
        self.next_cup = next_cup



def create_cups():
    global cup_dict, cups

    c = cup(cups[0], None)
    cup_dict[cups[0]] = c

    # create a cup for the initial input values
    for i in range(1, len(cups)):
        nxt_cup = cup(cups[i], None)
        c.next_cup = nxt_cup
        
        cup_dict[cups[i]] = nxt_cup
        c = nxt_cup

    
    # add remaining cups for values up to 10**6
    for v in range(10, 10**6 + 1):
        nxt_cup = cup(v, None)
        c.next_cup = nxt_cup
        
        cup_dict[v] = nxt_cup
        c = nxt_cup
    
    
    # link last cup back to the starting cup
    nxt_cup.next_cup = cup_dict[cups[0]]


def print_values(n):
    global cups

    product = 1
    val = n
    for i in range(3):
        print(val, end = ', ')
        product *= val
        current_cup = cup_dict[val]
        nxt_cup = current_cup.next_cup
        val = nxt_cup.value
        
    print('\t', product)



def play_round():
    global cup_dict, current_cup, destination_cup, MAX
    
    nxt_cup = current_cup.next_cup
    next_three_values_to_move = []
    for i in range(3):
        next_three_values_to_move.append(nxt_cup.value)
        nxt_cup = nxt_cup.next_cup

    #print('3tomove', next_three_values_to_move)
    
    ### get the destination value ###
    dest_value = current_cup.value - 1
    while dest_value in next_three_values_to_move:
        dest_value -= 1
    # ensure value is not smaller than minimum
    if dest_value == 0:
        dest_value = MAX
        # ensure MAX is not in number to remove
        while dest_value in next_three_values_to_move:
            dest_value -= 1

    # get destination cup
    destination_cup = cup_dict[dest_value]

    ### adjust pointers ###
    last_cup_to_remove = cup_dict[next_three_values_to_move[-1]]
    # current_cup should now point to whatever the 3rd item to remove was pointing to
    current_cup.next_cup = last_cup_to_remove.next_cup
    
    # destination_cup should now point to 1st item from 3 to remove
    temp_cup_pointer = destination_cup.next_cup     # save the destination pointer
    first_cup_to_remove = cup_dict[next_three_values_to_move[0]]
    destination_cup.next_cup = first_cup_to_remove
    
    # last item from 3 to remove should now point to what destination cup was pointing to 
    last_cup_to_remove.next_cup = temp_cup_pointer         

    # update current cup
    current_cup = current_cup.next_cup



    

# global variables
cups = [2,5,3,1,4,9,8,6,7]
cup_dict = dict()   # value : cup

create_cups()

current_cup     = cup_dict[cups[0]]
destination_cup = None
MAX             = 10**6

move = 1
while move <= 10**7:
    play_round()
    move += 1

print_values(1)




