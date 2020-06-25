#day7
class step:
    def __init__(self, name):
        self.name       = name
        self.prereq     = ["ROOT"]
        self.children   = []

    def add_prereq(self, p):
        self.prereq.append(p)

    def add_children(self, c):
        self.children.append(c)

    def print_info(self):
        print(self.name, end = '\t')
        for i in range(1, len(self.prereq)):
            print(self.prereq[i], end='')
        print()
        #print(self.children)
        #print("-----------------------")


def get_step(n):
    global graph
    for g in graph:
        if g.name == n:
            return g


def select_step():
    global available_steps, steps_used
    available_steps.sort()
    s = available_steps.pop(0)
    if s not in steps_used:
        steps_used.append(s)
    #print(s)
    return s
    
def update_steps(s):
    global graph
    s = s.upper()
    for g in graph:
        if s in g.prereq:
            g.prereq.remove(s)

def update_avail_steps():
    global graph, available_steps, steps_used
    for g in graph:
        #g.print_info()
        if g.name not in steps_used:
            if len(g.prereq) == 0:
                available_steps.append(g.name)




i = 0            
graph = []      #list of steps   
steps = []      #list of lower case letters matching step name
f = open("day7_input.txt", "r")
for x in f:
    #print(i, graph)
    i += 1
    x = x.split()
    s = x[1]        #step
    c = x[7]        #child
    if s.lower() not in steps:      #new step
        steps.append(s.lower())
        st = step(s)
        graph.append(st)
    else:                   #step has already been created
        st = get_step(s)
    if c.lower() not in steps:      #new step
        steps.append(c.lower())
        ch = step(c)
        graph.append(ch)
    else:                   #step has already been created
        ch = get_step(c)
    st.add_children(c)
    ch.add_prereq(s)



for g in graph:
    g.print_info()

steps_used = []    
available_steps = ["root"]       #add "root" to available steps
#while length of available steps > 0
while len(available_steps) > 0:
    #select alpha first step and remove step from available steps
    s = select_step()
    if s in available_steps:
        available_steps.remove(s)
            
    #update prereqs
    update_steps(s)
    
    #add additional availble steps
    update_avail_steps()


steps_used.remove("root")
answer = ""
for i in steps_used:
    answer += i

print(answer)


