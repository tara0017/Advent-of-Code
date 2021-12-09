# day8

def part1():
    num_1478 = 0

    f = open('day8.txt','r')
    for x in f:
        x = x.strip()
        x = x.split()

        for v in x[11:]:
            if len(v) == 2 or len(v) == 3 or len(v) == 4 or len(v) == 7:
                num_1478 +=1
                
    print('Part 1:',num_1478)


# part 2
def get_key(x):
    key = dict()
    
    seq_length = dict()
    for i in range(2, 8):
        seq_length[i] = []  #multiple entries

    for seq in x[:10]:
        seq_length[len(seq)].append(seq)

    key['A'] = get_missing_chars(seq_length[3], seq_length[2])[0]
    DB       = get_missing_chars(seq_length[4], seq_length[2])
    AEG      = get_missing_chars(seq_length[7], seq_length[4])
    CDE      = get_missing_chars(seq_length[7], seq_length[6])
    CF       = seq_length[2][0]
    
    #'d' should appear in both DB and CDE
    for char in DB:
        if char in CDE:
            key['D'] = char
        else:
            key['B'] = char

    #'e' should appear in both AEG and CDE
    for char in AEG:
        if char in CDE:
            key['E'] = char
        elif char == key['A']:
            continue
        else:
            key['G'] = char

    #'c' is only unassigned letter in CDE
    for char in CDE:
        if char == key['D'] or char == key['E']:
            continue
        else:
            key['C'] = char

    #'f' is only unassigned letter in CF
    for char in CF:
        if char != key['C']:
            key['F'] = char
            
    return key
            

def get_missing_chars(s1, s2):
    missing_letters = []
    
    if len(s2) == 1:
        for char in s1[0]:
            if char not in s2[0]:
                missing_letters.append(char)       
    else: #multiple sequances of that length
        for seq in s2:
            for char in s1[0]:
                if char not in seq:
                    missing_letters.append(char)

    return missing_letters


# return a set of letters after conversion
def convert_letters(seq, key):
    letters = set()
    for k,v in key.items():
        if v in seq:
            letters.add(k)
    return letters
            
    
def get_output_value(x, key):
    num_letter_key = dict()
    num_letter_key[0] = {'A','B','C','E','F','G'}
    num_letter_key[1] = {'C','F'}
    num_letter_key[2] = {'A','C','D','E','G'}
    num_letter_key[3] = {'A','C','D','F','G'}
    num_letter_key[4] = {'B','C','D','F'}
    num_letter_key[5] = {'A','B','D','F','G'}
    num_letter_key[6] = {'A','B','D','E','F','G'}
    num_letter_key[7] = {'A','C','F'}
    num_letter_key[8] = {'A','B','C','D','E','F','G'}
    num_letter_key[9] = {'A','B','C','D','F','G'}

    num = ''
    for seq in x[11:]:
        s = convert_letters(seq, key)
        for k,v in num_letter_key.items():
            if s == v:
                num += str(k)
                break

    return int(num)


def part2():
    total = 0
    
    f = open('day8.txt','r')
    for x in f:
        x = x.strip()
        x = x.split()
    
        key = get_key(x)
        v = get_output_value(x, key)
        total += v
    
    print('Part 2:', total)



part1()
part2()







