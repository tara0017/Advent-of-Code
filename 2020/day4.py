# day4
def process_line(x):
    info = []
    x = x.split()
    for item in x:
        field = (item[:3], item[4:])
        info.append(field)
    #print(field)
    return info

def is_valid_passport(p):
    # part 1
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # ignore 'cid'
    for f in fields:
        if f not in p:
            return False

    # part 2
    #byr 1920 - 2002
    if not is_byr_valid(p['byr']):
        return False
    
    #iyr 2010 - 2020
    if not is_iyr_valid(p['iyr']):
        return False
    
    #eyr 2020 - 2030
    if not is_eyr_valid(p['eyr']):
        return False
    
    #hgt 150 - 193 cm OR 59 - 76
    if not is_hgt_valid(p['hgt']):
        return False
    
    #hcl # followed by 6 chars 0-9 or a-f
    if not is_hcl_valid(p['hcl']):
        return False
    
    #ecl 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    if not is_ecl_valid(p['ecl']):
        return False
    
    #pid 9 digit number
    if not is_pid_valid(p['pid']):
        return False
    
    return True

#pid 9 digit number
def is_pid_valid(pid):
    allowed_chars = ['0','1','2','3','4','5','6','7','8','9']
    if len(pid) == 9:
        for c in pid:
            if c not in allowed_chars:
                return False
        return True
    return False
        
#ecl 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
def is_ecl_valid(ecl):
    allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in allowed_ecl:
        return True
    return False
        
#hcl # followed by 6 chars 0-9 or a-f
def is_hcl_valid(hcl):
    allowed_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    if hcl[0] == '#':
        for c in hcl[1:]:
            if c not in allowed_chars:
                return False
        return True
    return False

#hgt 150 - 193 cm OR 59 - 76 in
def is_hgt_valid(hgt):
    h = int(hgt[:-2])
    if hgt[-2:] == 'cm':
        if h >= 150 and h <= 193:
            return True
    if hgt[-2:] == 'in':
        if h >= 59 and h <= 76:
            return True
    return False
        
#eyr 2020 - 2030
def is_eyr_valid(yr):
    yr = int(yr)
    if yr >= 2020 and yr <= 2030:
        return True
    return False

#iyr 2010 - 2020
def is_iyr_valid(yr):
    yr = int(yr)
    if yr >= 2010 and yr <= 2020:
        return True
    return False

#byr 1920 - 2002
def is_byr_valid(yr):
    yr = int(yr)
    if yr >= 1920 and yr <= 2002:
        return True
    return False



passports = []
string = ''

f = open('day4.txt','r')
for x in f:
    if x == '\n':
        data = process_line(string)
        p = dict()

        
        for d in data:
            p[d[0]] = d[1]
        passports.append(p)
        string = ''
    else:
        string += x.replace('\n', ' ')


count = 0
for p in passports:
    if is_valid_passport(p):
        count += 1

print("Valid passports:", count)    
