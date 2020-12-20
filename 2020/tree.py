
class tree():
    def __init__(self):
        # set of nodes
        self.nodes = []

    # add a node to the tree
    def add_node(self, node):
        self.nodes.append(node)

    # print the nodes in the tree
    def print_tree(self):
        for node in self.nodes:
            print(node.value, ": ", end = "")
            for c in node.children:
                print(c, end = ",\t")
            print()

    # get a node by its value
    def get_node_by_value(self, v):
        for n in self.nodes:
            if n.value == v:
                return n
        return None

    # returns the parent node
    def get_parent(self, child):
        for n in self.nodes:
            if child.value in n.children:
                return n

    # return a list of children for given node
    def get_children(self, node):
        return node.children
