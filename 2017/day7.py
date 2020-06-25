#day7
class node:
    def __init__(self, name, value, children, parent):
        self.name     = name
        self.value    = value
        self.children = children
        self.parent = parent

    def print_info(self):
        print("Name: ", self.name)
        print("Value: ", self.value)
        print("Children: ", self.children)
        print("Parent: ", self.parent)

    def set_parent(self, p):
        self.parent = p

    def get_value(self):
        return int(self.value)
    

def remove_node(c):
    global nodes_copy
    for n in nodes_copy:
        if n.name == c:
            nodes_copy.remove(n)
            break
        
nodes = []

f = open("day7_input.txt", "r")
for x in f:
    x = x.replace("(", "")
    x = x.replace(")", "")
    x = x.replace("->", "")
    x = x.replace(",", "")
    x = x.split()
    children = x[2:]
    n = node(x[0], x[1], children, "")
    nodes.append(n)

nodes_copy = nodes[:]
#print(nodes_copy)

for n in nodes:
    for c in n.children:
        #print("C = ", c)
        remove_node(c)


def get_node(n):
    global nodes
    for node in nodes:
        if node.name == n:
            return node
    
def get_total_weight(node):
    global weight
    if len(node.children) > 0:
        for c in node.children:
            n = get_node(c)
            weight += get_total_weight(n)
        #weight += node.get_value()
    else:
        return node.get_value()
    weight += node.get_value()
    return weight



def get_total_weight2(node):
    weight = 0
    if len(node.children) == 0:
        return node.get_value()
    else:
        weight = node.get_value()
        for c in node.children:
            n = get_node(c)
            weight += get_total_weight2(n)
        return weight



weight = 0
for n in nodes_copy:
    n.print_info()
print(nodes_copy)

s = "rfkvap" #"nzeqmqi"
print("=====================================")
get_node(s).print_info()
print("=====================================")
print(s, "W:", get_total_weight2(get_node(s)))


