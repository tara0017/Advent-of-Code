# day21
import copy

def read_file():
    f = open('day21.txt','r')
    for x in f:
        x = x.strip()
        x = x.replace('(contains ', '=')
        x = x.replace(')', '')
        x = x.split('=')
        labels.append(x)


def process_item(food):
    global allergens
    
    alrgns      = food[1].split(', ')
    ingrediants = set(food[0].split())
    
    for a in alrgns:
        #is it already in dictionary
        if a in allergens:
            
            # allergan already has a match
            if len(allergens[a]) == 1:
                continue

            # allergen has multiple potential matches
            else:
                ing_to_remove = []
                
                # check each ingrediant against potential matches
                for ingrd in allergens[a]:
                    if ingrd not in ingrediants:
                        ing_to_remove.append(ingrd)

                for i in ing_to_remove:
                    allergens[a].remove(i)   
            
        #not already in dictionary
        else:
            #a is a new key
            #put all ingrediants in a set and set as potential matches for a
            allergens[a] = copy.deepcopy(ingrediants)


def trim_ingrediants():
    global allergens

    newly_matched_allergens = set()
    
    for a in allergens:
        if len(allergens[a]) == 1:
            for item in allergens[a]:
                newly_matched_allergens.add(item)

    while len(newly_matched_allergens) > 0:
        next_matched_allergens = []
        
        for match in newly_matched_allergens:
            for a in allergens:
                
                #if it hasn't been matched yet
                if len(allergens[a]) > 1:
                    try:
                        allergens[a].remove(match)
                        
                        #now that match was removed is there only 1 option left?
                        if len(allergens[a]) == 1:
                            for al in allergens[a]:
                                next_matched_allergens.append(al)
                    except:
                        continue

        # update newly matched allergens
        newly_matched_allergens.clear()
        for n in next_matched_allergens:
            newly_matched_allergens.add(n)
            



def get_num_non_allerg():
    global allergens, labels
    count = 0
    
    allerg = set()
    for a in allergens:
        allerg = allerg.union(allergens[a])

    for lbl in labels:
        lbl = lbl[0]
        lbl = lbl.split()

        for item in lbl:
            if item not in allerg:
                count += 1

    return count




            
# global variables 
labels    = []
allergens = dict()  #key = allergen : value = set(potential matches)

# read input file and populate global variables
read_file()
for food in labels:
    process_item(food)


trim_ingrediants()

# part 2
# print each ingrediant and matching allergen
print('Part 2:')
keys = allergens.keys()
for a in sorted(keys):
    print(a, '\t', allergens[a])

# part 1
count = get_num_non_allerg()
print('\nPart 1:', count)


