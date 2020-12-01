# day22

class player:    
    def __init__(self, hit_points, armor, damage, mana_left, mana_spent):
        self.hit_points = hit_points
        self.armor      = armor
        self.damage     = damage
        self.mana_left  = mana_left
        self.mana_spent = mana_spent
    """
    def __call__(self, a, d, hp, ml, ms):
        self.hit_points = hp
        self.armor = a
        self.damage = d
        self.mana_left = ml
        self.mana_spent = ms
    """   
    def get_hp(self):
        return self.hit_points
    def get_ml(self):
        return self.mana_left
    def get_ms(self):
        return self.mana_spent
    def get_a(self):
        return self.armor
    def get_d(self):
        return self.damage
    
    def set_hp(self, v):
        self.hit_points = v
    def set_ml(self, v):
        self.mana_left = v
    def set_ms(self, v):
        self.mana_spent = v
    def set_a(self, v):
        self.armor = v
    def set_d(self, v):
        self.damage = v
    

class boss:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage     = damage
        
    def __call__(self, hp, d):
        self.hit_points = hp
        self.damage = d
    def get_hp(self):
        return self.hit_points
    def get_d(self):
        return self.damage
               


class snapshot:
    def __init__(self, p, b, a):
        self.player  = p
        self.boss    = b
        self.actions = a

    def get_player(self):
        return self.player
    def get_boss(self):
        return self.boss

import copy

# returns a list of game snapshots after each possible player action
def player_turn(s):
    next_snapshots = []
    p = s.get_player()
    b = s.get_boss()

    #print_snapshot(s)

    
    # create a copy of player and boss
    np = player(p.hit_points, p.armor, p.damage, p.mana_left, p.mana_spent)
    nb = boss(b.hit_points, b.damage)

    # update effects that last multiple turns
    if shield_active(s):        # shield   
        np.set_a(7)     #np.set_a(np.armor + 7)  # shield INCREASED BY 7
    else:
        np.set_a(0)
    if poison_active(s):        # poison
        nb.hit_points -= 3
    if recharge_active(s):      # recharge
        np.mana_left += 101

    # select each of the possible actions as the next action
    # select magic missile
    if np.mana_left >= 53:
        npm = player(np.hit_points, np.armor, np.damage, np.mana_left - 53, np.mana_spent + 53)     # next player after missile
        nbm = boss(nb.hit_points - 4, nb.damage)    # next boss after missile
        nam = s.actions + 'M'                       # next actions after missile
        ns  = snapshot(npm, nbm, nam)               # next snapshot after missile
        next_snapshots.append(ns)
    # select drain
    if np.mana_left >= 73:
        npd = player(np.hit_points + 2, np.armor, np.damage, np.mana_left - 73, np.mana_spent + 73)     # next player after drain
        nbd = boss(nb.hit_points - 2, nb.damage)    # next boss after drain
        nad = s.actions + 'D'                       # next actions after drain
        ns  = snapshot(npd, nbd, nad)               # next snapshot after drain
        next_snapshots.append(ns)
    # select shield
    if (not shield_active(s)) and np.mana_left >= 113:
        nps = player(np.hit_points, np.armor, np.damage, np.mana_left - 113, np.mana_spent + 113)     # next player after shield
        # next boss is unaffected after shield
        nas = s.actions + 'S'                       # next actions after missile
        ns  = snapshot(nps, nb, nas)                # next snapshot after missile
        next_snapshots.append(ns)
    # select poison  
    if (not poison_active(s)) and np.mana_left >= 173:
        npp = player(np.hit_points, np.armor, np.damage, np.mana_left - 173, np.mana_spent + 173)     # next player after poison
        # next boss is unaffected after poison
        nap = s.actions + 'P'                       # next actions after poison
        ns  = snapshot(npp, nb, nap)                # next snapshot after poison
        next_snapshots.append(ns)
    # select recharge
    if (not recharge_active(s)) and np.mana_left >= 229:
        npr = player(np.hit_points, np.armor, np.damage, np.mana_left - 229, np.mana_spent + 229)     # next player after recharge
        # next boss is unaffected after recharge
        nar = s.actions + 'R'                       # next actions after recharge
        ns  = snapshot(npr, nb, nar)                # next snapshot after recharge
        next_snapshots.append(ns)        
    
    return next_snapshots


def boss_turn(s):
    p = s.player
    
    # create a copy of player and boss
    np = player(p.hit_points, p.armor, p.damage, p.mana_left, p.mana_spent)
    nb = boss(s.boss.hit_points, s.boss.damage)
        
    # update effects that last multiple turns
    if shield_active(s):      # shield
        np.set_a(7)     #np.set_a(np.armor + 7)  # shield INCREASED BY??? 7
    else:
        np.armor = 0
    if poison_active(s):      # poison
        nb.hit_points -= 3
    if recharge_active(s):    # recharge
        np.mana_left += 101

    # if boss loses before attack, return prior to boss' attack
    if nb.hit_points <= 0:
        ns = snapshot(np, nb, s.actions + 'B')
        return ns

    # boss hasn't lost yet, attack player
    np.hit_points -= max(1, (nb.damage - np.armor))  ######IS SHIELD INCREASED BY 7 (+= 7
    # reduce armor
    np.armor = max(0, (np.armor - nb.damage))
    
    #return game snapshots after boss attack
    ns = snapshot(np, nb, s.actions + 'B')
    return ns


def shield_active(s):
    duration = 6
    if 'S' in s.actions[len(s.actions) - duration - 1:]:
        return True     
    return False

def poison_active(s):
    duration = 6
    if 'P' in s.actions[len(s.actions) - duration - 1:]:
        return True         
    return False

def recharge_active(s):
    duration = 5
    if 'R' in s.actions[len(s.actions) - duration - 1:]:
        return True     
    return False


def print_snapshot(s):
    p = s.player
    b = s.boss
    print("TURN", turn)
    print("PLAYER", p.hit_points, p.armor, p.mana_left, p.mana_spent)
    print("BOSS: ", b.hit_points, b.damage)
    print("ACTIONS", s.actions)
    print('---------------------------------------------')

    
# initial snapshot
initial_boss     = boss(58, 9)
initial_player   = player(50, 0, 0, 500, 0)
initial_snapshot = snapshot(initial_player, initial_boss, '')
turn = 0

# least amount of mana spent set to inifinity
least_spent  = 10**6
winning_actions = ''

# queue to track all possible game snapshots after n turns
game_snapshots = [initial_snapshot]


while len(game_snapshots) > 0:
    turn += 1
    next_turn_snapshots = []    #queue of all possible game outcomes for the next turn
    
    for s in game_snapshots:

        # player turn
        if turn % 2 == 1:
            #print('Player turn')
            
            # update snapshot with each possible action
            next_snapshot = player_turn(s)   ### update active effect

            # for each snapshot in next_snapshots
            for ns in next_snapshot:
                p = ns.player
                b = ns.boss
                
                # if mana spent is more than least_spent,
                if p.mana_spent > least_spent:
                    continue            #trash snapshot
                
                elif p.mana_left < 0:   # negative mana left
                    continue            #trash snapshot
                
                elif b.hit_points <= 0: # boss is defeated (new cheaper defeat)
                    least_spent     = p.mana_spent
                    winning_actions = ns.actions
                    
                else:
                    #append snapshot to next_turn_snapshots
                    next_turn_snapshots.append(ns)
                

        # boss' turn  
        else:
            #print('Boss turn')
            next_snapshot = boss_turn(s)     ### update active effect
            b = next_snapshot.boss
            p = next_snapshot.player
            
            # if boss losses
            if b.hit_points <= 0:
                
                # if mana spent is less than least_spent
                if p.mana_spent < least_spent:
                    least_spent     = p.mana_spent
                    winning_actions = next_snapshot.actions
                    
                else:   # mana spent exceeds least spent
                    continue        # trash next_snapshot

            # player loses  
            elif p.hit_points <= 0: 
                continue            # trash next_snapshot

            # both are still alive (append next_snapshot to next_turn_snapshots)
            else:
                next_turn_snapshots.append(next_snapshot)

    game_snapshots = next_turn_snapshots[:]
    """
    for s in game_snapshots:
        if s.actions in 'RBSBRBPBMBSBMBPBMBMBM'[:len(s.actions)]:
            if poison_active(s):
                print("poisen active", s.actions)
            print_snapshot(s)
    """

print(winning_actions)
print(least_spent)

# 1026 too low  ( D P R S M P M M M M )
# 1295 too high ( R S R P M S M P M M M )   RBSBRBPBMBSBMBPBMBMBM

