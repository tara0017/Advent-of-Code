# day 18
class tree_node:
    def __init__(self, value, level, parent, l_child = None, r_child = None):
        global tree_nodes
        
        self.value = value
        self.level = level
        self.parent  = parent
        self.l_child = l_child
        self.r_child = r_child

        tree_nodes.add(self)
        
    def print_node(self):
        if self.parent == None:
            print('None')
        else:
            print(self.parent.value)
        print('Value:', self.value)
        print('Level:', self.level)
        if self.l_child == None:
            print('None')
        else:
            print('left:', self.l_child.value)
        if self.r_child == None:
            print('None')
        else:
            print('right:', self.r_child.value)
        print('--------------------------------------------------')



def reduce_first_unreduced_node_old():
    global root

    visited = set()
    n = root.l_child
    
    visited.add(n)

    while True:
        if (n.level == 5):   # nested inside four pairs #(n != None) and 
            explode(n)
            return 1
        elif (n.l_child == None) and (n.value > 9):     # double digit leaf #(n != None) and 
            split(n)
            return 2
        else:               # check next node
            visited.add(n)
                
            if (n.l_child != None) and (n.l_child not in visited):      # check left child (if exists)  
                n = n.l_child
            elif (n.r_child != None) and (n.r_child not in visited):   # check right child (if exists)
                n = n.r_child
            else:
                while (n in visited) and ((n.r_child == None) or (n.r_child in visited)): 
                    n = n.parent
                    
                    if (root in visited) and (n.level == 0):   # (this is the root again) all nodes have been checked
                        return None
       

    
"""
update snailfish number tree (running total)

parameters:
    s = string of snailfish number to add to tree (right child of current root node)    
"""
def addition(s):
    global root

    new_root = get_tree_node(s, None)
    value = '[' + root.value + ',' + new_root.value + ']'
    
    # increment levels by 1 for all nodes in both trees
    for n in tree_nodes:
        n.level += 1

    #create new temp root with original tree as left child and new tree as right child        
    n = tree_node(value, 0, None, root, new_root)

    # update old root's parent
    root.parent = n

    # update root node
    root = n

    new_root.parent = root 
    


"""
parameter:
    s = string of snailfish number
"""
def get_tree_node(s, parent):

    if parent == None:  #root
        level = 0
    else:
        level = parent.level + 1

    n = tree_node(s, level, parent)
    
    n.l_child = get_left_child(s, level, n)
    n.r_child = get_right_child(s, level, n)

    return n
    
    

def get_left_child(s, parent_level, parent):
    # remove outside braces
    s = s[1:-1]
    
    num_string = '0123456789'

    level = parent_level + 1
    
    if s[0] in num_string:  # no nested snailfish
        # make sure it is not a double digit value
        if s[1] in num_string:
            v = int(s[0:2])
        else:
            v = int(s[0])
        n = tree_node(v, level, parent)
        return n
    else:                   # nested snailfish
        # get left string up to ','
        num_open_brace = 0
        num_close_brace = 0
        for i in range(len(s)):
            if s[i] == '[':
                num_open_brace += 1
            elif s[i] == ']':
                num_close_brace += 1

            if num_open_brace == num_close_brace:
                n = get_tree_node(s[:i + 1], parent)
                return n

                
                   
def get_right_child(s, parent_level, parent):
    # remove outside braces
    s = s[1:-1]
    
    num_string = '0123456789'

    level = parent_level + 1
    
    if s[-1] in num_string:  # no nested snailfish on right side
        # make sure it is not a double digit value
        if s[-2] in num_string:
            v = int(s[-2:])
        else:
            v = int(s[-1])
        n = tree_node(v, level, parent)
        return n
    else:                   # nested snailfish
        # get right string after ','
        num_open_brace = 0
        num_close_brace = 0
        for i in range(len(s)):
            if s[i] == '[':
                num_open_brace += 1
            elif s[i] == ']':
                num_close_brace += 1

            if num_open_brace == num_close_brace:
                n = get_tree_node(s[i+2:], parent)
                return n


# ensures there are no explosions left before doing splits                        
def any_explosions_left():
    global tree_nodes
    for n in tree_nodes:
        if n.level == 5:
            return True
    return False



"""
search left to right to find 1st instance of a value that must be "reduced"
numbers that must be reduced:  (level = 5)  or (no children and value > 9)
reduces number if there is something to reduce and returns a value (1 = explode, 2 = split)
returns 'None' if there is nothing to reduce
"""
def reduce_first_unreduced_node():
    global root

    visited = set()
    n = root.l_child
    
    visited.add(n)

    while True:
        if (n.level == 5):   # nested inside four pairs
            explode(n)
            return 1
        elif (n.l_child == None) and (n.value > 9) and (any_explosions_left() == False):     # double digit leaf #(n != None) and 
            split(n)
            return 2
        else:               # check next node
            visited.add(n)
                
            if (n.l_child != None) and (n.l_child not in visited):      # check left child (if exists)  
                n = n.l_child
            elif (n.r_child != None) and (n.r_child not in visited):   # check right child (if exists)
                n = n.r_child
            else:
                while (n in visited) and ((n.r_child == None) or (n.r_child in visited)): 
                    n = n.parent
                    
                    if (root in visited) and (n.level == 0):   # (this is the root again) all nodes have been checked
                        return None
            


def get_adjacent_left_number(n):
    global root
    
    while n == n.parent.l_child:
        n = n.parent
        if n == root:   # no number to the left
            return None
        
    n = n.parent.l_child
    while n.r_child != None:
        n = n.r_child
    return n

    
def get_adjacent_right_number(n):
    global root
    
    while n == n.parent.r_child:
        n = n.parent
        if n.parent == None:    # no number to the right
            return None
        
    n = n.parent.r_child
    while n.l_child != None:
        n = n.l_child
    return n


def explode(n):
    global root
    
    p = n.parent
    lcv = p.l_child.value
    rcv = p.r_child.value

    old_value = p.value
    new_value = '0'
    
    # add left side
    temp = get_adjacent_left_number(n)
    if temp != None:
        temp.value += lcv
        # update values of parent nodes after lcv and rcv added 
        while temp.parent != None:
            temp = temp.parent
            left  = str(temp.l_child.value)
            right = str(temp.r_child.value)
            temp.value = '[' + left + ',' + right + ']'
        root.value = '[' + root.l_child.value + ',' + root.r_child.value + ']'   
            
    # add right side
    temp = get_adjacent_right_number(n.parent)
    if temp != None:

        temp.value += rcv
        
        # update values of parent nodes after lcv and rcv 
        while temp.parent != None:
            temp = temp.parent
            left  = str(temp.l_child.value)
            right = str(temp.r_child.value)
            temp.value = '[' + left + ',' + right + ']'
        root.value = '[' + root.l_child.value + ',' + root.r_child.value + ']'  

        
    # delete left child node and right child node
    tree_nodes.remove(p.l_child)
    tree_nodes.remove(p.r_child)
    # set parent node children to 'None'
    p.l_child = None
    p.r_child = None


    # replace node's (and every node above i.e. parent) value with new_value
    # set parent node value to 0
    p.value = 0
    while p.parent != None:
        p = p.parent
        p.value = p.value.replace(old_value, new_value, 1)
 
    

def split(n):
    # get 2 values from double digit value
    lv = int(n.value / 2)
    rv = n.value - lv
    new_value = '[' + str(lv) + ',' + str(rv) + ']'
    old_value = str(n.value)
    
    # create l_child node
    l_chld = tree_node(lv, n.level + 1, n)
    # create r_child node
    r_chld = tree_node(rv, n.level + 1, n)
    
    # assign l_child and r_child as children of n
    n.l_child = l_chld
    n.r_child = r_chld
    n.value = new_value
    
    # replace node's (and every node above i.e. parent) value with new_value
    while n.parent != None:
        n = n.parent
        n.value = n.value.replace(old_value, new_value, 1)
    root.value = '[' + root.l_child.value + ',' + root.r_child.value + ']'      





"""
reduce the snailfish number according to explode/split rules

return:
    reduced snailfish number tree (running_total)
"""
def reduce_number():
    global tree_nodes
    
    is_num_reduced = False
    while is_num_reduced == False:
        is_num_reduced = True
        #look for 1st instance of a number > 9 or a number in 5th level of tree
        reduce_happened = reduce_first_unreduced_node()
        if reduce_happened != None:
            is_num_reduced = False



"""
recursively get magnitude of a node (root for magnitude of entire tree)
3 * left_child + 2 * r_child
"""
def get_magnitude(node):
    # base case: reached a leaf (numerical value) has no children
    if node.l_child == None:
        return int(node.value)

    else:
        left = get_magnitude(node.l_child)
        right = get_magnitude(node.r_child)
        return (3*left + 2*right)




tree_nodes = set()      
snailfish_numbers = []


f = open('day18.txt','r')
for x in f:
    x = x.strip()
    snailfish_numbers.append(x)



"""
# Part 1
root = get_tree_node(snailfish_numbers[0], None)
reduce_number() # in case initial expression is not reduced

for i in range(1, len(snailfish_numbers)):
    addition(snailfish_numbers[i])
    reduce_number()

root.print_node() # final sum
print(get_magnitude(root))
"""


# Part 2

max_mag = 0
print(len(snailfish_numbers))

for n1 in snailfish_numbers:
    
    for n2 in snailfish_numbers:
        if n2 == n1:
            continue
        
        # clear old values
        tree_nodes.clear()
        root = get_tree_node(n1, None)
        
        addition(n2)
        reduce_number()

        # check if magnitude is larger
        mag = get_magnitude(root)
        if mag > max_mag:
            max_mag = mag
            #print(mag, n1, n2)
            #root.print_node()
    

print(max_mag)















