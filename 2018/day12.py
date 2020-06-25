#day12

initial_state = "##.#.####..#####..#.....##....#.#######..#.#...........#......##...##.#...####..##.#..##.....#..####"
#practice data
#initial_state = "#..#.#..##......###...###"

def get_start(s):
    i = 0
    for j in state:
        if j == "#":
            return i - 5
        i += 1

def get_end(s):
    for j in range(len(state)-1, 0, -1):
        if state[j] == "#":
            return j + 5

        
key = set()

f = open("day12_input.txt", "r")
for x in f:
    x = x.replace("=>", "")
    x = x.split()
    if x[1] == "#":
        key.add(x[0])

for k in key:
    print(k)


#starting number of plants
num_plants = 0
for i in initial_state:
    if i == "#":
        num_plants += 1
print("0", num_plants)


#add 60 "." on front and end of text (at most 3 dots before/after plant produce a plant)
state = "."*10 + initial_state + "."*100
gen = 0


#print(state)

while gen < 20:
    gen += 1
    #find starting index (location of 1st # -3)
    start = get_start(state)
    #find ending index (location of last # +3)
    end = get_end(state)

    new_state = "." * (len(initial_state)+40)
    for i in range(start, end):
        s = state[i:i+5]
        if s in key:
            new_state = new_state[:i+2] + "#" + new_state[i+3:]
            num_plants += 1
    state = new_state[:]

    print(gen, num_plants)
    print(state)
        

pot_sum = 0
for i in range(len(state)):
    if state[i] == "#":
        print(i-10)
        pot_sum += (i-10)


print(pot_sum)











