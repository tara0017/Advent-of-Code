# day 7
class hand:
    def __init__(self, hand, bid, level = 0):
        self.hand = hand
        self.bid = bid
        self.level = level

    """
    levels:
    High card        0
    One pair         1
    Two pair         2
    Three of a kind  3
    Full house       4
    Four of a kind   5
    Five of a kind   6
    """
    def update_level(self): 
        card_distribution = dict()

        max_occurance = 1
        for c in self.hand:
            if c in card_distribution:
                card_distribution[c] += 1
                max_occurance = max(max_occurance, card_distribution[c])
            else:
                card_distribution[c] = 1

        match max_occurance:
            case 1:
                self.level = 0
            case 2:
                num_pairs = 0
                
                for k,v in card_distribution.items():
                    if v == 2:
                        num_pairs += 1

                if num_pairs == 1:   #pair
                    self.level = 1
                elif num_pairs == 2: #2 pair
                    self.level = 2
            case 3:
                for k,v in card_distribution.items():
                    if v == 2:      # full house
                        self.level = 4
                        break
                    elif v == 1:    #three of a kind
                        self.level = 3
                        break
            case 4:
                self.level = 5
            case 5:
                self.level = 6
        


"""
returns positive value if h1 > h2 
"""
def compare(h1, h2):
    strength = '23456789TJQKA'
    for i in range(len(h1)):
        ind1 = strength.index(h1[i])
        ind2 = strength.index(h2[i])
        if ind1 != ind2:
            return ind1 - ind2
        

"""
sort hands from small to large (all hands are the same level)
param list of hands 
return sorted list 
"""  
def sort_hands(hands):
    if len(hands) == 0:
        return hands
    
    sorted_list = [hands[0]]

    for j in range(1, len(hands)):
        for i in range(len(sorted_list)):
            if compare(hands[j].hand, sorted_list[i].hand) < 0: #current hand is smaller
                #insert hand here
                sorted_list.insert(i, hands[j])
                break
            elif i == len(sorted_list) - 1:     #smaller than all of sorted list
                sorted_list.append(hands[j])
                break

    return sorted_list
                


#global variables
hands_by_level = dict()     #{int level : list [] of all hands with that level}
for i in range(7):
    hands_by_level[i] = []
    
#read file
f= open('day7.txt', 'r')
for x in f:
    x = x.split()
    h = hand(x[0], int(x[1]))
    h.update_level()
    hands_by_level[h.level].append(h)






#Part 1
    
#sort each level in hands_by_level
sorted_hands = []
for i in range(7):
    sorted_hands += sort_hands(hands_by_level[i])


total_winning = 0
for i in range(len(sorted_hands)):
    total_winning += (i+1) * sorted_hands[i].bid
print('Part 1: ', total_winning)




#Part 2
"""
returns 1 if h1 > h2 
"""
def compare2(h1, h2):
    strength = 'J23456789TQKA'
    for i in range(len(h1)):
        ind1 = strength.index(h1[i])
        ind2 = strength.index(h2[i])
        if ind1 != ind2:
            return ind1 - ind2
        

"""
sort hands from small to large (all hands are the same level)
input list of hands 
return sorted list 
"""  
def sort_hands2(hands):
    if len(hands) == 0:
        return hands
    
    sorted_list = [hands[0]]

    for j in range(1, len(hands)):
        for i in range(len(sorted_list)):
            if compare2(hands[j].hand, sorted_list[i].hand) < 0: #current hand is smaller
                #insert hand here
                sorted_list.insert(i, hands[j])
                break
            elif i == len(sorted_list) - 1:     #smaller than all of sorted list
                sorted_list.append(hands[j])
                break
            
    return sorted_list


"""
at least 1 joker exists    
"""
def get_new_level(h):
    c = h.hand.count('J')  #get number of jokers
    
    match c:
        case 1: # 1 joker
            if h.level == 1: #one pair to 3 of a kind
                return hand(h.hand, h.bid, 3)
            elif h.level == 2: #two pair to full house
                return hand(h.hand, h.bid, 4)
            elif h.level == 3: #three of a kind to four of a kind
                return hand(h.hand, h.bid, 5)
            else: #all other cases level +1
                return hand(h.hand, h.bid, h.level + 1)
        case 2: # 2 jokers
            if h.level == 1: #one pair to 3 of a kind
                return hand(h.hand, h.bid, 3)
            elif h.level == 2: #two pair to four of a kind
                return hand(h.hand, h.bid, 5)
            elif h.level == 4: #full house to five of a kind
                return hand(h.hand, h.bid, 6)
            # no other options
        case 3: # 3 jokers
            if h.level == 3: #three of a kind to 4 of a kind
                return hand(h.hand, h.bid, 5)
            elif h.level == 4: #full house to five of a kind
                return hand(h.hand, h.bid, 6)
            # no other options
        case 4: # 4 jokers
            if h.level == 5: #four of a kind to 5 of a kind
                return hand(h.hand, h.bid, 6)
            # no other options
        case 5: # 5 jokers
            return hand(h.hand, h.bid, 6)

            

"""
param a dictionary {level : list of hands}
"""
def adjust_hands_level(hands_by_level):
    new_dict = dict()
    for i in range(7):
        new_dict[i] = []

    for k,v in hands_by_level.items():
        for h in v:
            if not 'J' in h.hand:       # no jokers
                new_dict[k].append(h)
            else:
                updated_hand = get_new_level(h)
                new_dict[updated_hand.level].append(updated_hand)
                
    return new_dict



#adjust hands by level
hands_by_level2 = adjust_hands_level(hands_by_level)

#sort each level in hands_by_level
sorted_hands2 = []
for i in range(7):
    sorted_hands2 += sort_hands2(hands_by_level2[i])

total_winning2 = 0
for i in range(len(sorted_hands2)):
    total_winning2 += (i+1) * sorted_hands2[i].bid
print('Part 2: ', total_winning2)


