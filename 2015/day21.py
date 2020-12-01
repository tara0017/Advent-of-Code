# day21
def will_defeat_boss(damage, shield):
    """
    boss info
    Hit Points: 100
    Damage: 8
    Armor: 2
    """
    
    # since we both have the same amount of "hit points" (100)
    if (damage - 2) >= (8 - shield):
        return True
    return False
    """
    boss_hit_points = 100
    boss_damage     = 8
    boss_shield     = 2
    my_hit_points   = 100
    
    while True:
        # I attack
        d = max(1, damage - boss_shield)
        boss_hit_points -= d
        if boss_hit_points <= 0:
            return True
        
        # boss attacks
        d = max(1, boss_damage - shield)
        my_hit_points -= d
        if my_hit_points <= 0:
            return False
    """
    

# shop items (buy 1 weapon, 1 or 0 armors, 0-2 rings)
#Weapons:    Cost  Damage  Armor
weapons = [
['Dagger',      8,     4,   0],
['Shortsword', 10,     5,   0],
['Warhammer',  25,     6,   0],
['Longsword',  40,     7,   0],
['Greataxe',   74,     8,   0]
]

#Armor:      Cost  Damage  Armor
armor = [
['Leather',    13,     0,   1],
['Chainmail',  31,     0,   2],
['Splintmail', 53,     0,   3],
['Bandedmail', 75,     0,   4],
['Platemail', 102,     0,   5]
]

#Rings:         Cost  Damage  Armor
rings = [
['Damage', +1,   25,     1,   0],
['Damage', +2,   50,     2,   0],
['Damage', +3,  100,     3,   0],
['Defense', +1,  20,     0,   1],
['Defense', +2,  40,     0,   2],
['Defense', +3,  80,     0,   3]
]


# add option of no armor
armor.append(['None', 0, 0, 0])

# add no rings as one of the option
# (will not account for no rings w either selection) 
rings.append(['None', 0, 0, 0, 0])


# set default highest cost to 0
highest_cost = 0

# select 1 weapon, 1 armor and up to 2 rings
for w in weapons:
    for a in armor:
        # option of no rings selected
        damage = w[2]
        shield = a[3]
        cost   = w[1] + a[1]
        if cost > highest_cost and not will_defeat_boss(damage, shield):
            print(w, a, cost)
            highest_cost = cost

            
        # option of at least 1 ring selected
        for r_index1 in range(len(rings)):  # select 1st ring
            for r_index2 in range(r_index1 + 1, len(rings)): # select 2nd ring
                new_damage  = damage + (rings[r_index1][3] + rings[r_index2][3])
                new_shield  = shield + (rings[r_index1][4] + rings[r_index2][4])
                new_cost    = cost   + (rings[r_index1][2] + rings[r_index2][2])
                if new_cost > highest_cost and not will_defeat_boss(new_damage, new_shield):
                    print(w, a, rings[r_index1], rings[r_index2], new_cost)
                    highest_cost = new_cost

"""
# part 1

# set default lowest cost to infinity
lowest_cost = 10**3

# select 1 weapon, 1 armor and up to 2 rings
for w in weapons:
    for a in armor:
        # option of no rings selected
        damage = w[2]
        shield = a[3]
        cost   = w[1] + a[1]
        if cost < lowest_cost and will_defeat_boss(damage, shield):
            print(w, a, cost)
            lowest_cost = cost

            
        # option of at least 1 ring selected
        for r_index1 in range(len(rings)):  # select 1st ring
            for r_index2 in range(r_index1 + 1, len(rings)): # select 2nd ring
                new_damage  = damage + (rings[r_index1][3] + rings[r_index2][3])
                new_shield  = shield + (rings[r_index1][4] + rings[r_index2][4])
                new_cost    = cost   + (rings[r_index1][2] + rings[r_index2][2])
                if new_cost < lowest_cost and will_defeat_boss(new_damage, new_shield):
                    print(w, a, rings[r_index1], rings[r_index2], new_cost)
                    lowest_cost = new_cost

"""
