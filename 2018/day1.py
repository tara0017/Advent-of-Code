#day1
total = 0
freq = set()
is_solution_found = False
changes = []

f = open("day1_input.txt", "r")
for x in f:
    changes.append(int(x))



while is_solution_found == False:
    for x in changes:
        if total in freq:
            print(total)
            is_solution_found = True
            break
        else:
            freq.add(total)
            total += x
    #part1
    #print(total)
