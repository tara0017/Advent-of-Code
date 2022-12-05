"""
            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
 1   2   3   4   5   6   7   8   9
 """

"""
#test code
A = ['Z','N']
B = ['M','C','D']
C = ['P']
stacks = [blank,A,B,C]
"""


def move_crates(x):
    global stacks

    for i in range(x[0]):
        crate = stacks[x[1]].pop()
        stacks[x[2]].append(crate)


def move_crates2(x):
    global stacks
    
    moved_stack = []
    
    for i in range(x[0]):
        crate = stacks[x[1]].pop()
        moved_stack.append(crate)

    for i in range(x[0]):
        crate = moved_stack.pop()
        stacks[x[2]].append(crate)
        
        
def get_top_crates():
    global stacks
    s = ''
    for i in range(1, len(stacks)):
        c = stacks[i].pop()
        s += c
    return s

    
blank = []
A = ['W','B','D','N','C','F','J']
B = ['P','Z','V','Q','L','S','T']
C = ['P','Z','B','G','J','T']
D = ['D','T','L','J','Z','B','H','C']
E = ['G','V','B','J','S']
F = ['P','S','Q']
G = ['B','V','D','F','L','M','P','N']
H = ['P','S','M','F','B','D','L','R']
I = ['V','D','T','R']
stacks = [blank,A,B,C,D,E,F,G,H,I]


f = open('day5.txt','r')

for x in f:
    x = x.split()
    y = [int(x[1]), int(x[3]), int(x[5])]
    #move_crates(y)
    move_crates2(y)


print(get_top_crates())


