# day22
import copy

def read_file():
    global player1, player2
    p1 = False
    p2 = False

    f = open('day22.txt','r')
    for x in f:
        x = x.strip()
        if len(x) == 0:
            continue
        elif 'Player 1' in x:
            p1 = True
        elif 'Player 2' in x:
            p2 = True
            p1 = False
        elif p1:
            player1.append(int(x))
        elif p2:
            player2.append(int(x))


def play_a_round():
    global player1, player2

    p1 = player1.pop(0)
    p2 = player2.pop(0)

    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    elif p2 > p1:
        player2.append(p2)
        player2.append(p1)
        


def calc_score():
    global player1, player2
    score = 0
    
    # get winning player
    if len(player1) > 0:
        p = player1
    else:
        p = player2

    for i in range(len(p)):
        score += (p[i] * (len(p) - i))

    return score
                  
                   
        
    
def play_recursive_round(player1, player2):

    p1 = player1.pop(0)
    p2 = player2.pop(0)
    round_winner = None
    
    if len(player1) >= p1 and len(player2) >= p2:
        # get sub game hands
        p1_hand = copy.deepcopy(player1[:p1])
        p2_hand = copy.deepcopy(player2[:p2])

        # get round winner based off the sub game result
        round_winner = play_sub_game(p1_hand, p2_hand)
        
    elif p1 > p2:
        round_winner = 'p1w'
    elif p2 > p1:
        round_winner = 'p2w'

    # assign cards to winner
    if round_winner == 'p1w':
        player1.append(p1)
        player1.append(p2)
    elif round_winner == 'p2w':
        player2.append(p2)
        player2.append(p1)

    # return resulting hands
    return (player1, player2)
    


def play_sub_game(p1_hand, p2_hand):
    sub_game_hands = set()
    
    while len(p1_hand) > 0 and len(p2_hand) > 0:
        # if hands have occured before, player 1 automatically wins
        if tuple(p1_hand) in sub_game_hands or tuple(p2_hand) in sub_game_hands:
            return 'p1w'
        else:
            sub_game_hands.add(tuple(p1_hand))
            sub_game_hands.add(tuple(p2_hand))
            
        (p1_hand, p2_hand) = play_recursive_round(p1_hand, p2_hand)

    if len(p1_hand) == 0:
        return 'p2w'
    elif len(p2_hand) == 0:
        return 'p1w'

    

#global variables
player1 = []
player2 = []
rnd = 0

read_file()


"""
# part 1
while len(player1) > 0 and len(player2) > 0:
    play_a_round()
    rnd += 1

print('Part 1')
print(calc_score())
"""


# part 2
all_game_hands = set()
while len(player1) > 0 and len(player2) > 0:
    # if hands have occured before, player 1 automatically wins
    if tuple(player1) in all_game_hands or tuple(player2) in all_game_hands:
        print('PLAYER 1 WINS!')
        print(player1)
        print(player2)
        break
    else:
        all_game_hands.add(tuple(player1))
        all_game_hands.add(tuple(player2))
        
    (player1, player2) = play_recursive_round(player1, player2)
    rnd += 1

print('Part 2')
print(calc_score())








