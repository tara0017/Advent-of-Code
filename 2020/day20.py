# day20
import copy

        
class tile():
    def __init__(self, number, grid):
        self.number      = number
        self.grid        = grid
        self.edges       = self.get_edges(self.grid)

    # returns a list with edges in order [N, E, S, W]
    def get_edges(self, g):
        N = g[0]
        S = g[-1]
        E = []
        W = []
        
        for i in range(len(g)):
            E.append(g[i][-1])
            W.append(g[i][0])
            
        return [N, E, S, W]
    

    def flip_horiz(self):
        #edges flip for N,S
        for r in self.grid:
            r.reverse()
        self.edges = self.get_edges(self.grid)


    def flip_vert(self):
        #edges flip for E,W
        self.grid.reverse()
        self.edges = self.get_edges(self.grid)


    def rotate_left(self):
        # edges flip for N, S
        new_grid = copy.deepcopy(self.grid)
        length = len(self.grid)
        for r in range(length):
            for c in range(length):
                row = c
                col = length - r - 1
                new_grid[r][c] = self.grid[row][col]
                
        self.grid = copy.deepcopy(new_grid)
        self.edges = self.get_edges(self.grid)
        
    
def create_tile(x, num):
    grid = []
    for row in x:
        r = []
        for c in row:
            if c == '#':
                r.append(1)
            else:
                r.append(0)
        grid.append(r)

    t = tile(num, grid)
    return t


def read_file():
    global image
    
    tile = []
    f = open('day20.txt', 'r')
    for x in f:
        if x == '\n':
            if len(tile) > 0:
                image.add(create_tile(tile, tile_num))
                tile.clear()

        elif 'Tile' in x:
            tile_num = int(x[4:x.index(':')])
            
        else:
            x = x.strip()
            tile.append(x)


"""
create a dictionary (needs to be updated after transformation)
{key = edge list [1,0,0,1...] : value =  list of matching tiles }
"""
def create_histogram():
    global edge_hist, image

    for t in image:
        # loop through each edge
        for i in range(len(t.edges)):
            e = t.edges[i]
            tuple_e = tuple(e)

            #if the edge is already in dictionary
            if tuple_e in edge_hist:
                #add tile to that key's values
                edge_hist[tuple_e].append(t)

            # that edge configuration is not already in keys
            else:
                # if reversed is in keys
                re = copy.deepcopy(e)
                re.reverse()
                tuple_e = tuple(re)
                if tuple_e in edge_hist:
                    edge_hist[tuple_e].append(t)
                
                # brand new edge configuration
                else:
                    # add this to dictionary as a new key
                    edge_hist[tuple_e] = [t]


def get_tile_by_number(n):
    global image

    for t in image:
        if t.number == n:
            return t


def print_border():
    for n in borders:
        t = get_tile_by_number(n)
        print(n)
        
        for e in t.edges:
            tup = tuple(e)
            re = copy.deepcopy(e)
            re.reverse()
            rev_tup = tuple(re)

            neighbors = []
            try:
                tiles     = edge_hist[tup]
                for t in tiles:
                    neighbors.append(t.number)
            except:
                tiles_rev = edge_hist[rev_tup]
                for t in tiles_rev:
                    neighbors.append(t.number)

            print(e, '\t', neighbors)
        print('---------------------------------')


    
# determine image border layout
def print_neighbors(n):
    print('================')
    print(n)
    t = get_tile_by_number(n)
    for e in t.edges:
        tup = tuple(e)
        re = copy.deepcopy(e)
        re.reverse()
        rev_tup = tuple(re)

        neighbors = []
        try:
            tiles     = edge_hist[tup]
            for t in tiles:
                neighbors.append(t.number)
        except:
            tiles_rev = edge_hist[rev_tup]
            for t in tiles_rev:
                neighbors.append(t.number)

        print(e, '\t', neighbors)
    print('================')


def get_neighbors(n):
    lst = []    # returns [N neighbors, E neighbors, S neighbors, w neighbors]
    t = get_tile_by_number(n)

    for e in t.edges:
        tup = tuple(e)
        re = copy.deepcopy(e)
        re.reverse()
        rev_tup = tuple(re)

        neighbors = []
        try:
            tiles     = edge_hist[tup]
            for t in tiles:
                if t.number != n:
                    neighbors.append(t.number)
        except:
            tiles_rev = edge_hist[rev_tup]
            for t in tiles_rev:
                if t.number != n:
                    neighbors.append(t.number)

        lst.append(neighbors)

    return lst


def orient_top_tile(pre_tile, tile_num):
    s = get_tile_by_number(pre_tile)
    t = get_tile_by_number(tile_num)

    # get t's northern edge to have no neighbors
    nbrs = get_neighbors(tile_num)
    for i in range(4):
        if len(nbrs[i]) == 0:
            side_wo_nbrs = i    # 0:N   1:E     2:S     3:W
    # if side w/o nbrs is facing N, do nothing. Otherwise...
    if side_wo_nbrs == 1:
        t.rotate_left()
    elif side_wo_nbrs == 2:
        t.flip_vert()
    elif side_wo_nbrs == 3:
        t.rotate_left()
        t.flip_vert()

    west = (t.edges)[3]
    east = (s.edges)[1]
    
    # if the edges do not match, flip horizontal
    if west != east:
        t.flip_horiz()


def orinent_tile(pre_tile, tile_num, row, i):
    global g
    
    try:
        west_tile = get_tile_by_number(pre_tile)
        pre_east_edge = (west_tile.edges)[1]
    except:     # this is the left most tile (no tile to the west
        west_tile = None
    north_tile_num = g[row - 1][i]
    north_tile     = get_tile_by_number(north_tile_num)
    current_tile   = get_tile_by_number(tile_num)
    current_tile_edges = current_tile.edges
    
    # get current_tile's northern edge to match north_tile's southern edge
    south_edge = (north_tile.edges)[2]
    if south_edge in current_tile_edges:
        if south_edge == current_tile_edges[1]:     # matches east side
            current_tile.rotate_left()
        elif south_edge == current_tile_edges[0]:   # matches northern side
            pass
        elif south_edge == current_tile_edges[2]:   # matches southern side
            current_tile.flip_vert()
        elif south_edge == current_tile_edges[3]:   # matches western side
            current_tile.rotate_left()
            current_tile.flip_vert()


    else:   # edge does not match... tile must be flipped
        current_tile.flip_horiz()
        current_tile.flip_vert()
        current_tile_edges = current_tile.edges
        
        if south_edge in current_tile_edges:
            if south_edge == current_tile_edges[1]:     # matches east side
                current_tile.rotate_left()
            elif south_edge == current_tile_edges[0]:   # matches northern side
                pass
            elif south_edge == current_tile_edges[2]:   # matches southern side
                current_tile.flip_vert()
            elif south_edge == current_tile_edges[3]:   # matches western side
                current_tile.rotate_left()
                current_tile.flip_vert()

    # get current_tile's western edge to match previous_tile's eastern edge
    nbrs = get_neighbors(tile_num)
    if west_tile == None:   # 1st tile in row (no edge to match)
        if len(nbrs[1]) == 0:   # side with no neighbors is on the wrong side (east)
            current_tile.flip_horiz()
        
    else:                   # not 1st tile in row (match edges to previous tile)
        if nbrs[1] == pre_east_edge:
            current_tile.flip_horiz()


def read_tile_grid(t, i, j):
    global complete_image, hashtag_count

    g = t.grid
    for m in range(len(g) - 2):
        for n in range(len(g) - 2):
            val = g[m+1][n+1]
            if val == 1:
                hashtag_count += 1
            
            image_y = 8 * i + m
            image_x = 8 * j + n
            
            complete_image[(image_y, image_x)] = val
 

def is_monster(start_point):
    global complete_image, monster

    for p in monster:
        point = (start_point[0] + p[1], 95 - (start_point[1] + p[0]))

        if complete_image[point] == 0:
            return False
    print('monster at starting point:', point)
    return True



# global variables
image = set()       # set of tiles
edge_hist = dict()  # {key = edge : value = [(tile1, N), (tile2, W)]}
borders = []
hashtag_count = 0


read_file()
create_histogram()

###############
# look for tiles along the border (only 1 item in value list) for that particular key
# corners:  2 adjacent sides with key configurations that do not appear elsewhere
for e in edge_hist:
    if len(edge_hist[e]) == 1:
        t = edge_hist[e][0]
        borders.append(t.number)
################          
#print_border()



g = []
g.append([1093,	2203,	1223,	1871,	2917,	2741,	1129,	3251,	1619,	1997,	2131,	3217])
g.append([3187,	2011,	1931,	2281,	1409,	1721,	1889,	1237,	3911,	1747,	3323,	2297])
g.append([1013,	3889,	3359,	1987,	3989,	2029,	2383,	1531,	2909,	2851,	1609,	1753])
g.append([1523,	3947,	1451,	2251,	1433,	2677,	3739,	3803,	3923,	2027,	3457,	3863])
g.append([1663,	1559,	1637,	1759,	1097,	2423,	2207,	2731,	3701,	3347,	3677,	2467])
g.append([2411,	2711,	3847,	2269,	3571,	3533,	1879,	2503,	1229,	1499,	2803,	3659])
g.append([2143,	3061,	3331,	2789,	3391,	2243,	3491,	2857,	3037,	2687,	2551,	3019])
g.append([1291,	2341,	1657,	2441,	2003,	1579,	1571,	1459,	1249,	1181,	1279,	2153])
g.append([1877,	2539,	2777,	2659,	2719,	3449,	1217,	1999,	3049,	2017,	2521,	2593])
g.append([1009,	2137,	3257,	2843,	1213,	1289,	1277,	1399,	3109,	3559,	1823,	3371])
g.append([1069,	3709,	3343,	3119,	2293,	1481,	1979,	3319,	1483,	1063,	2381,	1361])
g.append([1321,	3373,	2213,	1061,	3851,	1117,	2081,	2087,	1811,	3011,	3769,	1613])

          
#=========== ORIENT TOP ROW ======================    
previous_tile = g[0][0]
for i in range(1, len(g[0])):    
    orient_top_tile(previous_tile, g[0][i])
    previous_tile = g[0][i]

# fix end of row
n = g[0][-1]    # last tile
t  = get_tile_by_number(n)
nb = get_neighbors(n)

while (len(nb[0]) > 0) or (len(nb[1]) > 0):
    t.rotate_left()
    nb = get_neighbors(n)
#===============================================

       
#********** ORIENT REMAINING TILES ***************    
for row in range(1, len(g)):
    previous_tile = None
    for i in range(len(g[row])):
        orinent_tile(previous_tile, g[row][i], row, i)
        previous_tile = g[row][i]
#***********************************************

              
#^^^^^^^^^^^ complete entire image ^^^^^^^^^^^^^^^^^^
complete_image = dict()
for i in range(len(g)):
    line = g[i]
    for j in range(len(line)):
        tile_num = line[j]
        t = get_tile_by_number(tile_num)
        read_tile_grid(t, i, j)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



#points that make up a monster (from top left corner)
monster = [(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]

for y in range(76):
    for x in range(93):
        start_point = (y,x)
        if is_monster(start_point):
            hashtag_count -= len(monster)
print(hashtag_count)


