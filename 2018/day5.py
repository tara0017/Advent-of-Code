#day5
def process_reactions(x):
    reaction_happened = True
    while reaction_happened:
        reaction_happened = False
        for i in range(len(x)-1):
            #print(i)
            if x[i] == x[i+1].upper() or x[i] == x[i+1].lower():
                if x[i] != x[i+1]:
                    #print(x[i], x[i+1])
                    x = x[:i] + x[i+2:]
                    reaction_happened = True
                    break

    #print(x)
    return len(x)
    

"""
#part1
f = open("day5_input.txt", "r")
for x in f:
    x = x.strip()
    process_reactions(x)
"""


#part2
f = open("day5_input2.txt", "r")
for x in f:
    x = x.strip()


smallest = len(x)
#ASCII:     a = 97         z = 122
for i in range(97, 123):
    #print(i)
    letter = chr(i)
    print(letter, letter.upper())
    y = x.replace(letter, "")
    y = y.replace(letter.upper(), "")
    l = process_reactions(y)
    if l < smallest:
        print(l)
        smallest = l
    



