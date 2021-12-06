# day 6


def build_freq_dict():
    global ages
    # buid age frequency dictionary
    f = open('day6.txt','r')
    for i in range(9):
        ages[i] = 0


    for x in f:
        x = x.strip()
        x = x.split(',')

        for fish in x:
            ages[int(fish)] += 1


def increment_one_day():
    global ages
    next_day = dict()
    reset_parents = 0
    
    for k,v in ages.items():
        if k == 0:
            next_day[8] = v
            reset_parents = v
        else:
            next_day[k-1] = v
    next_day[6] += reset_parents
    return next_day
            

def get_total_count():
    global ages
    total = 0
    
    for k,v in ages.items():
        total += v
    return total


ages = dict()
num_days = 256

build_freq_dict()
for day in range(num_days):
    ages = increment_one_day()
    #print(day,':',ages)

print('Number pf lanternfish:', get_total_count())








