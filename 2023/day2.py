#day 2

def get_records(s):
    records = []
    rgb = [0,0,0]

    i = 0
    while i < len(s):
        if s[i] == ';':
            records.append(rgb)
            rgb = [0,0,0]
        else:
            if s[i+1] == 'red':
                rgb[0] = int(s[i])
                i += 1
            elif s[i+1] == 'green':
                rgb[1] = int(s[i])
                i += 1
            elif s[i+1] == 'blue':
                rgb[2] = int(s[i])
                i += 1
        i += 1
        
    records.append(rgb)
    return records
            

games = dict()
max_red = 12
max_green = 13
max_blue = 14


f = open('day2.txt','r')
for x in f:
    x = x.replace(',', '')
    x = x.replace(':', '')
    x = x.replace(';', ' ;')
    x = x.split()

    record = get_records(x[2:])
    games[int(x[1])] = record


#part 1
def part1():
    global games, max_red, max_blue, max_green
    id_sum = 0
    
    for k,v in games.items():

        is_possible_game = True
        for record in v:
            if record[0] > max_red or record[1] > max_green or record[2] > max_blue:
                is_possible_game = False
                break
        if is_possible_game:
            id_sum += k

    print(id_sum)    

#part 2
def part2():
    global games
    power_sum = 0

    for k,v in games.items():
        p = [0,0,0]
        for record in v:
            p[0] = max(p[0], record[0])
            p[1] = max(p[1], record[1])
            p[2] = max(p[2], record[2])

        power = p[0] * p[1] * p[2]
        power_sum += power

    print(power_sum) 

part1()
part2()



