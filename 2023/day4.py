# day 4

def read_card(x):
    global cards

    x = x.split()
    divider = x.index('|')
    
    winning_numbers = set() 
    for i in range(2, divider):
        winning_numbers.add(int(x[i]))

    num_matches = 0
    for i in range(divider + 1, len(x)):
        if int(x[i]) in winning_numbers:
            num_matches += 1

    cards[x[1]] = [1, num_matches]


def count_copies():
    global cards

    total = 0
    for k,v in cards.items():
        copies = v[0]
        matching_nums = v[1]
        
        total += copies
        
        for i in range(1, matching_nums + 1):
            cards[str(int(k) + i)][0] += copies
         
    return total     
    

def get_card_value():
    global cards
    
    total = 0
    for k,v in cards.items():
        if v[1] == 0:
            continue
        else:
            total += 2**(v[1] - 1)

    return total


#global variables
cards = dict() #{card number: [num_copies, matches]}
total_cards = 0

f = open('day4.txt','r')

for x in f:
    x = x.replace(':', '')
    read_card(x)

print('Part 1: ', get_card_value())    
print('Part 2: ', count_copies())

