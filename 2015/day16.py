# day16

def is_matching_aunt(a):
    global info

    for i in range(3):
        if a[i][0] in info:
            # part 2
            if a[i][0] == 'cats':
                if a[i][1] <= 7:
                    return False
            elif a[i][0] == 'trees':
                if a[i][1] <= 3:
                    return False
            elif a[i][0] == 'pomeranians':
                if a[i][1] >= 3:
                    return False
            elif a[i][0] == 'goldfish':
                if a[i][1] >= 5:
                    return False
            elif info[a[i][0]] != a[i][1]:
                return False

    return True


info = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
    }

aunts = dict()

f = open('day16.txt', 'r')
for x in f:
    x = x.replace(':', '').replace(',', '')
    x = x.split()
    a = [(x[2], int(x[3])), (x[4], int(x[5])), (x[6], int(x[7]))]
    aunts[x[1]] = a
    if is_matching_aunt(a):
        print(x[1], a)
    #break



        





