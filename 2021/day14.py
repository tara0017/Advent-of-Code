# day 14

def get_count(s):
    global rules, count, pair_count    

    for i in range(len(s) - 1):
        count[s[i]] += 1

        pair = s[i:i+2]
        pair_count[pair] += 1

    # last char in string was not counted in loop
    count[s[-1]] += 1


def update_template():
    global template, rules, count, pair_count
    
    temp_pair_count = dict()
    
    for k,v in pair_count.items(): 
        if v == 0:
            continue
        else:
            new_pairs  = rules[k]
            new_letter = new_pairs[0][1]
            
            #add new letter to count
            count[new_letter] += v
            
            #add 2 new pairs to temp_pair_count
            for p in new_pairs:
                if p not in temp_pair_count:
                    temp_pair_count[p] = v
                else:
                    temp_pair_count[p] += v

    pair_count = temp_pair_count

            
    
def update_template_old():
    global template
    
    temp = ''
    for i in range(len(template) - 1):
        c = get_new_char(template[i : i+2])
                         
        temp += (template[i] + c)

    temp += template[-1]
    template = temp

    
count      = dict()   # number of times each letter appears
pair_count = dict()   # number of times each pair appears
rules      = dict()   # i.e. 'CH -> B'     =>      ['CB', 'BH']
is_rules   = False

f = open('day14.txt', 'r')

for x in f:
    if is_rules:
        x = x.strip()
        x = x.split(' -> ')

        # 'CH -> B'       =>      ['CB', 'BH']
        s1 = x[0][0] + x[1]
        s2 = x[1] + x[0][1]
        
        outcomes = [s1, s2]
        
        rules[x[0]] = outcomes
        
        pair_count[x[0]] = 0
        count[x[1]]      = 0
              
    elif x == '\n':
        is_rules = True

    else:
        template = x.strip()


# get initial count of letters and pairs
get_count(template)


for step in range(40):
    update_template()


max_count = count[template[0]]
min_count = count[template[0]]


for k,v in count.items():
    if v > max_count:
        max_count = v
    elif v < min_count:
        min_count = v
        
    
print(max_count - min_count)


        
    

