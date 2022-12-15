#day13
import numbers, copy

def in_right_order(s1,s2):
    #cases:
    #    1 of them is an empty list
    #    2 integers
    #    2 lists
    #    number and a list
    
    
    #empty list
    if s1 == []:
        return True
    elif s2 == []:
        return False

    #two integers
    if isinstance(s1[0], numbers.Number) and isinstance(s2[0], numbers.Number):
        #different values
        if s1[0] < s2[0]:
            return True
        elif s1[0] > s2[0]:
            return False

        else:   #equal values
            s1.pop(0)
            s2.pop(0)
            return in_right_order(s1, s2)

    #two lists
    elif isinstance(s1[0], list) and isinstance(s2[0], list):
        #lists are the same
        if s1[0] == s2[0]:
            s1.pop(0)
            s2.pop(0)

            return in_right_order(s1, s2)

        else: #lists are different
            return in_right_order(s1[0], s2[0])

    #number and list
    else:
        #s1 starts with a number
        if isinstance(s1[0], numbers.Number) and isinstance(s2[0], list):
            new_s1 = [s1[0]]

            #check if this new list matched s2 list
            if new_s1 == s2[0]:
                s1.pop(0)
                s2.pop(0)
                return in_right_order(s1, s2)
            else:
                return in_right_order(new_s1, s2[0])
                
            
        #s2 starts with a number
        if isinstance(s1[0], list) and isinstance(s2[0], numbers.Number):
            new_s2 = [s2[0]]

            #check if this new list matched s2 list
            if new_s2 == s1[0]:
                s1.pop(0)
                s2.pop(0)
                return in_right_order(s1, s2)
            else:
                return in_right_order(s1[0], new_s2)


    

#global variables                
pair_num = 1
pairs_in_right_order = set()
s1 = None
s2 = None
packets = []

#read data
f = open('day13.txt', 'r')
for x in f:
    if x == '\n':
        
        if in_right_order(s1, s2):
            pairs_in_right_order.add(pair_num)
        
        #reset the values
        s1 = None
        s2 = None

        #increment pair number
        pair_num += 1

    else: #assign values
        x = x.strip()
        if s1 == None:
            s1 = eval(x)
            packets.append(copy.deepcopy(s1))
        else:
            s2 = eval(x)
            packets.append(copy.deepcopy(s2))
    

#part 1
print('Part 1:', sum(pairs_in_right_order))


#part 2
ind_1 = 1
ind_2 = 2

for p in packets:
    if in_right_order(copy.deepcopy(p),[[6]]):
        ind_2 += 1

        if in_right_order(copy.deepcopy(p), [[2]]):
            ind_1 += 1
       


ind_2 -= 1 #[[6]] vs. [[[[6]], [1, [1, 8, 4], 1], [[3, 2, 8, 5, 0], 10], 3, [[10], 1, [10, 8, 5, 0], 7, [2, 10, 5]]], [9], [[1, 2, [7, 4, 7, 4, 5], 7, [1, 8, 1, 6, 5]], [[4, 10, 1], [1, 1, 0], [6], 4]], [6], [8, [10], 5]]

print('Part 2:', ind_1, ind_2, ind_1 * ind_2)








