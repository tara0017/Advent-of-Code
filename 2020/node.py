class node():
    def __init__(self, parent, children, value):
        self.parent = parent
        self.children = children
        self.value = value

    def add_child(self, child):
        self.children.append(child)
