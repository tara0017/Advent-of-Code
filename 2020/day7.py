# day7
import tree, node

def add_to_dict(x):
    key = x[0]
    bag_dict[key] = []

    # no bags inside
    if 'no other' in x[1]:
        return

    # bags inside
    for i in range(1, len(x)):
        s = x[i]
        
        # get number of bags
        index_of_first_space = s.find(' ')
        num = int(s[:index_of_first_space])
            
        # name of bag
        bag_name = s[index_of_first_space + 1:]

        # add info to dict
        # bag_dict[key].append(bag_name)        # part 1
        bag_dict[key].append((num, bag_name))   # part 2
                  

# returns array of bags which 'bag' can be inside
def what_bags_can_it_be_inside(bag):
    global bag_dict

    lst = []
    
    for k,v in bag_dict.items():
        if bag in v:
            lst.append(k)

    return lst


def num_bags_inside(bag_info, groups_above):
    global bag_dict, total

    num = bag_info[0]
    bag_name = bag_info[1]

    # get children (bags inside)
    bags_inside = bag_dict[bag_name]

    # update total
    total += (groups_above * num)
    
    #base case (no children/bags inside)
    if len(bags_inside) == 0:
        return 

    # recursive step
    else:
        for b in bags_inside:
            num_bags_inside(b, groups_above * num)


# collect and clean data
bag_dict = dict()
f = open('day7.txt', 'r')
for x in f:
    x = x.replace(' contain', ',')
    x = x.replace('.', '')
    x = x.replace('\n', '')
    x = x.replace(' bags', '')
    x = x.replace(' bag', '')
    x = x.split(', ')
    add_to_dict(x)

    
# part 2
total = 0          
num_bags_inside((1, 'shiny gold'), 1)
print(total - 1)




"""
# part 1
bags_that_can_contain = set()
bag_queue = ['shiny gold']
newly_added_bags = set()

while len(bag_queue) > 0:    
    for bag in bag_queue:
        new_bags = what_bags_can_it_be_inside(bag)

        for b in new_bags:
            newly_added_bags.add(b)
            bags_that_can_contain.add(b)

    # reset bag queue with new seeds
    bag_queue.clear()
    for b in newly_added_bags:
        bag_queue.append(b)
    newly_added_bags.clear()
    

print(len(bags_that_can_contain)) 
"""


