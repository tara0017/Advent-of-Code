#day7

class dirc:
    def __init__(self, dir_name, parent_dir, dir_lst = [], file_lst = [], dir_size = 0):
        self.dir_name = dir_name
        self.parent_dir = parent_dir
        self.dir_lst = dir_lst
        self.file_lst = file_lst
        self.dir_size = dir_size

    def add_dir(self, d):
        self.dir_lst.append(d)

    def add_file(self, f):
        self.file_lst.append(f)

    def get_files_size(self):
        size = 0
        for f in self.file_lst:
            size += int(f[0])
        return size
        
    def print_contents(self):
        print("Directory name:", self.dir_name)
        print("Parent directory:", self.parent_dir.dir_name)

        print("Nested directories: ", end = "")
        for d in self.dir_lst:
            print(d.dir_name, end = " ")
        print()

        print("Nested files: ", end = "")
        for f in self.file_lst:
            print(f, end = " ")
        print("\n")
        

def get_dir(name, parent):
    global directories

    for d in directories:
        if d.dir_name == name and d.parent_dir == parent:
            return d
        
    #if directory not found (not yet created) create a new directory
    return -1

    
#Read the items (files and directories) inside the current directory
def get_contents(cmnds):
    global current_dir

    for c in cmnds:
        #current item is a directory
        if c[0] == 'dir':
            d = get_dir(c[1], current_dir)
            if d == -1: #no such directory exists
                d = dirc(c[1], current_dir,[],[],0)
                directories.append(d)
                current_dir.add_dir(d)

            else:
                current_dir.add_dir(d)

        #current item is a file 
        else: 
            current_dir.add_file(c)
            
            
#global variables
commands = []
directories = []
root = dirc('/', None)
directories.append(root)
current_dir = None


#read file
f = open('day7.txt','r')
for x in f:
    x = x.split()
    commands.append(x)

#process commands
i = 0
while i < len(commands):
    if commands[i][0] == '$':
        if commands[i][1] == 'cd':
            if commands[i][2] == '..':
                current_dir = current_dir.parent_dir     
            else:            
                current_dir = get_dir(commands[i][2], current_dir)
            i += 1
            
        elif commands[i][1] == 'ls':
            #get all the commands up to the next '$' (ie files/dir inside cd)
            cmnds = [] #list of contents
            i += 1
            while i < len(commands) and commands[i][0] != '$':
                cmnds.append(commands[i])
                i +=1
            get_contents(cmnds)
    else:
        print("PROBLEM", commands[i])
        break




def get_dir_size(d):
    if d.dir_size != 0:
        return d.dir_size

    #size of nested directories
    nd_sizes = 0
    for nd in d.dir_lst:
        nd_sizes += get_dir_size(nd)

    #size of files
    f_sizes = d.get_files_size()

    return nd_sizes + f_sizes

#PART 1
total = 0
for d in directories:
    s = get_dir_size(d)
    if s <= 100000:
        total += s
print("Part 1:", total)


#PART 2
s = get_dir_size(root)
space_required = 30000000 - (70000000 - s)

candidate = 30000000
for d in directories:
    s = get_dir_size(d)
    if s >= space_required and s < candidate:
        candidate = s
print("Part 2:", candidate)

