# day19
import tree, node, copy

def add_inst(x):
    global instructions

    x = x.split(':')
    instructions[int(x[0])] = x[1]



def read_file():
    global instructions, messages
    inst = True
    msg  = False
    f = open('day19.txt', 'r')
    for x in f:
        if msg == True:     # messages
            x = x.strip()
            messages.append(x)

        elif x == '\n':     # seperation of instructions and messages
            inst = False
            msg  = True
            
        else:               # instructions
            x = x.replace('"', '')
            x = x.strip()
            add_inst(x)



# returna a list of strings w/ each value sperated by a comma
def get_children(parent):
    global instructions
    
    v = instructions[parent.value]
    v = v.split()

    # multiple children
    if '|' in v:    
        if len(v) > 3:  # of the form "num1 num2 | num3 num4
            s1 = v[0] + ',' + v[1]
            s2 = v[3] + ',' + v[4]
            lst = [s1,s2]
        else:           # of the form "num1 | num2
            s = v[0] + ',' + v[2]
            lst = [s]

    # one child      
    else:           
        s = ''
        for i in v:
            s += i + ','
            
        # remove final comma
        s = s[:-1]
        lst = [s]
    
    return lst


#1 input:    77 | 91             returns: ['77', '91']
#2 input:    91 87 | 77 58       returns:  ['91,87', '77,58']
#3 input:    91 91               returns: ['91,91']
#4 input:    42                  returns: ['42']
def read_chldrn_from_dict(v):
    if v =='a' or v == 'b':
        return []
    
    s = instructions[v]
    s = s.split()

    if '|' in s:
        # if length is 3    (case 1)
        if len(s) == 3:
            return [s[0], s[2]]
        
        # length is 5       (case 2)
        else:
            s1 = s[0] + ',' + s[1]
            s2 = s[3] + ',' + s[4]
            return [s1, s2]
        
    else:
        # if length is 2    (case 3)
        if len(s) == 2:
            s = s[0] + ',' + s[1]
            return [s]

        # length is 1       (case 4)
        else:
            return s
            
    
    

# param s:  string of values seperated by comma
# return:   a list of strings (integer values)
def get_val(s):
    s = s.split(',')
    return s



# build tree
def build_tree():
    global t
    
    # root
    n  = node.node(None, ['8,11'], 0)
    n1 = node.node(n, [], 8)
    n2 = node.node(n, [], 11)
    
    t.add_node(n)
    t.add_node(n1)
    t.add_node(n2)

    new_nodes = [n1, n2]


    while len(new_nodes) > 0:
        temp = []
        for nd in new_nodes:
            
            if nd.value != 'a' and nd.value != 'b':
                
                # update children
                chldrn = get_children(nd)
                nd.children = chldrn
                
                # for each child
                for child in chldrn:
                    
                    # get all children values
                    v_lst = get_val(child)

                    
                    # for each child's values
                    for v in v_lst:
                        try:
                            v = int(v)
                        except:
                            v = v

                        # check if node already exist
                        c = t.get_node_by_value(v)
                        
                        if c != None:
                            #update parent
                            c.parent = nd.value

                        # create a new node 
                        else:
                            cn = read_chldrn_from_dict(v)
                            
                            n = node.node(nd, cn, v)
                            t.add_node(n)
                            temp.append(n)

        new_nodes = copy.deepcopy(temp)



def get_index(msg, i, nums):
    n = nums[i]

    length = 0
    for j in range(i):
        length += len(nums[j])
        length += 1     # comma

    return msg.index(n, length)
        

def all_as_and_bs(item):
    for c in item:
        if c != 'a' and c != 'b' and c != ',':
            return False
    return True


def simplify(msg):
    global final_msgs
    smpl = [('50', 'b,b'), ('39', 'b,b,a'), ('100', 'a,b'), ('97', 'a,a'), ('118', '84,a'), ('96', 'a,a,a'), (',0,', ',42,42,31,'), ('87', '14,b'), ('77', 'a'), ('91', 'b')]

    for s in smpl:
        msg = msg.replace(s[0], s[1])

    if all_as_and_bs(msg):
        # add it to final set of msgs
        item = msg.replace(',', '')
        final_msgs.add(item)

        return (True, msg)
    return (False, msg)


def get_matching_msg():
    global t, final_msgs

    
    lst = ['0']
    nxt_lst = set()

    # continue until lst is blank (replaced all values by 'a's and 'b's
    while len(lst) > 0:
        print('lst length:', len(lst))
        
        nxt_lst.clear()
        
        for msg in lst:
            
            simpler = simplify(msg)
            if simpler[0] == True:
                continue
            else:
                msg = simpler[1]
            
            nums = msg.split(',')

            # cycle through each number (or 'a', or 'b') in the msg
            for i in range(len(nums)):
                n = nums[i]
                
                if n == 'a' or n == 'b':
                    continue
                else:
                    value = int(n)

                    # get value's children
                    node = t.get_node_by_value(value)
                    cld  = t.get_children(node)


                    # if there is only 1 child
                    if len(cld) == 1:
                        ind = get_index(msg, i, nums)
                        
                        new_msg = msg[:ind] + cld[0] + msg[ind + len(n):]
                        nxt_lst.add(new_msg)


                    # if it has 2 children
                    else:
                        # create 2 new msgs by replacing current value (@ this index) by each child
                        ind = get_index(msg, i, nums)
                        msg1 = msg[:ind] + cld[0] + msg[ind + len(n):]
                        msg2 = msg[:ind] + cld[1] + msg[ind + len(n):]
                        if msg1 not in nxt_lst:
                            nxt_lst.add(msg1)
                        if msg2 not in nxt_lst:
                            nxt_lst.add(msg2)

        # update lst
        lst.clear()
        lst= list(nxt_lst)

    return final_msgs



# global variables
instructions = dict()
messages     = []
t = tree.tree()
final_msgs = set()


read_file()
build_tree()


# get all matching rules
matching_msg = get_matching_msg()

# count solutions
count = 0
for m in messages:
    if m in matching_msg:
        count += 1
        
print(count)

    













