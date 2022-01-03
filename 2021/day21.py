# day 21

class player:
    def __init__(self, position, score = 0):
        self.position = position
        self.score    = score


def play_turn():
    global dice_value, p1, p2, turn, game_over
    turn += 1

    if turn % 2 == 1:
        p = p1
    else:
        p = p2

    # update position
    steps_to_move = 3 * dice_value + 3
    p.position += steps_to_move
    p.position %= 10
    if p.position == 0:
        p.position = 10

    # update score
    p.score += p.position
    if p.score >= 1000:
        game_over = True
    
    # update dice
    dice_value += 3
    if dice_value > 100:
        dice_value -= 100


def part1():    
    while game_over == False:
        play_turn()
        
    print('P1:', p1.position, p1.score)
    print('P2:', p2.position, p2.score)
    print('Die rolls:', 3 * turn)     # 3 rolls per turn

    print('Part 1:', 3 * turn * min(p1.score, p2.score))        

start = []
f = open('day21.txt')
for x in f:
    x = x.strip()
    x = x.split()
    start.append(int(x[-1]))
    

p1 = player(start[0])
p2 = player(start[1])
dice_value = 1
turn = 0
game_over = False


# part1()


class game_snapshot:
    def __init__(self, p1, p2, turns_played = 0, is_game_over = False):
        self.p1 = p1
        self.p2 = p2
        self.turns_played = turns_played
        self.is_game_over = is_game_over
#g = game_snapshot(p1, p2)


# s= snapshot (list), n = number of steps (for 3 rolls)
def update_pos_score(s, n):
    s[0] = (s[0] + 1) % 2
    if s[0] == 1:   #player 1's turn
        s[1] = s[1] + n
        if s[1] > 10:
            s[1] -= 10
        s[2] += s[1]
        return s
    else:
        s[3] = s[3] + n
        if s[3] > 10:
            s[3] -= 10
        s[4] += s[3]
        return s
    
def play_dirac_turn(snapshot, occurances):
    global updated_games_in_progress, p1_wins, p2_wins
    
    #1,1,1
    s = list(snapshot)
    s = update_pos_score(s, 3)
    
    # if someone wins
    if s[2] >= 21:      # player 1 won
        p1_wins += occurances
    elif s[4] >= 21:    # player 2 won
        p2_wins += occurances
    # no winner yet
    else:
        s = tuple(s)
        if s in updated_games_in_progress:  # if already in updated_games_in_progress
            # update num occurances
            updated_games_in_progress[s] += occurances
        else:                               # not already in updated_games_in_progress
            # add it to updated games_in_progress
            updated_games_in_progress[s] = occurances
            
    #1,1,2  1,2,1   2,1,1
    s = list(snapshot)
    s = update_pos_score(s, 4)
    
    # if someone wins
    if s[2] >= 21:      # player 1 won
        p1_wins += (3*occurances)
    elif s[4] >= 21:    # player 2 won
        p2_wins += (3*occurances)
    # no winner yet
    else:
        s = tuple(s)
        if s in updated_games_in_progress:  # if already in updated_games_in_progress
            # update num occurances
            updated_games_in_progress[s] += (3*occurances)
        else:                               # not already in updated_games_in_progress
            # add it to updated games_in_progress
            updated_games_in_progress[s] = (3*occurances)
            
    #1,1,3  1,3,1   3,1,1   2,2,1   2,1,2   1,2,2
    s = list(snapshot)
    s = update_pos_score(s, 5)
    
    # if someone wins
    if s[2] >= 21:      # player 1 won
        p1_wins += (6*occurances)
    elif s[4] >= 21:    # player 2 won
        p2_wins += (6*occurances)
    # no winner yet
    else:
        s = tuple(s)
        if s in updated_games_in_progress:  # if already in updated_games_in_progress
            # update num occurances
            updated_games_in_progress[s] += (6*occurances)
        else:                               # not already in updated_games_in_progress
            # add it to updated games_in_progress
            updated_games_in_progress[s] = (6*occurances)
            
    #1,2,3  1,3,2   2,3,1   2,1,3   3,1,2   3,2,1   2,2,2
    s = list(snapshot)
    s = update_pos_score(s, 6)
    
    # if someone wins
    if s[2] >= 21:      # player 1 won
        p1_wins += (7*occurances)
    elif s[4] >= 21:    # player 2 won
        p2_wins += (7*occurances)
    # no winner yet
    else:
        s = tuple(s)
        if s in updated_games_in_progress:  # if already in updated_games_in_progress
            # update num occurances
            updated_games_in_progress[s] += (7*occurances)
        else:                               # not already in updated_games_in_progress
            # add it to updated games_in_progress
            updated_games_in_progress[s] = (7*occurances)
            
    #1,3,3  3,1,3   3,3,1   2,2,3   2,3,2   3,2,2
    s = list(snapshot)
    s = update_pos_score(s, 7)
    
    # if someone wins
    if s[2] >= 21:      # player 1 won
        p1_wins += (6*occurances)
    elif s[4] >= 21:    # player 2 won
        p2_wins += (6*occurances)
    # no winner yet
    else:
        s = tuple(s)
        if s in updated_games_in_progress:  # if already in updated_games_in_progress
            # update num occurances
            updated_games_in_progress[s] += (6*occurances)
        else:                               # not already in updated_games_in_progress
            # add it to updated games_in_progress
            updated_games_in_progress[s] = (6*occurances)
            
    #2,3,3  3,2,3   3,3,2
    s = list(snapshot)
    s = update_pos_score(s, 8)
    
    # if someone wins
    if s[2] >= 21:      # player 1 won
        p1_wins += (3*occurances)
    elif s[4] >= 21:    # player 2 won
        p2_wins += (3*occurances)
    # no winner yet
    else:
        s = tuple(s)
        if s in updated_games_in_progress:  # if already in updated_games_in_progress
            # update num occurances
            updated_games_in_progress[s] += (3*occurances)
        else:                               # not already in updated_games_in_progress
            # add it to updated games_in_progress
            updated_games_in_progress[s] = (3*occurances)
            
    #3,3,3
    s = list(snapshot)
    s = update_pos_score(s, 9)
    
    # if someone wins
    if s[2] >= 21:      # player 1 won
        p1_wins += occurances
    elif s[4] >= 21:    # player 2 won
        p2_wins += occurances
    # no winner yet
    else:
        s = tuple(s)
        if s in updated_games_in_progress:  # if already in updated_games_in_progress
            # update num occurances
            updated_games_in_progress[s] += occurances
        else:                               # not already in updated_games_in_progress
            # add it to updated games_in_progress
            updated_games_in_progress[s] = occurances    
    

import copy


p1_wins = 0
p2_wins = 0


"""
dictionary:
key:                                                         value:
(turn(1or0), p1.position, p1.score, p2.position, p2.score)   num_occurances
"""
games_in_progress = dict()
g = (0, p1.position, p1.score, p2.position, p2.score)
games_in_progress[g] = 1
updated_games_in_progress = dict()

while len(games_in_progress) > 0:
    for k,v in games_in_progress.items():
        updated_game_snapshot = play_dirac_turn(k, v)
    games_in_progress = copy.deepcopy(updated_games_in_progress)
    updated_games_in_progress.clear()


print(p1_wins, p2_wins)
        






