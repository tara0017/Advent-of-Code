# day5

class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.start = [self.x1, self.y1]
        self.end   = [self.x2, self.y2]

    def print_line(self):
        print(self.start, '->', self.end)




def get_data():
    global lines
    
    f = open('day5.txt', 'r')
    for x in f:
        x = x.strip()
        x = x.split(' -> ')
        start = x[0].split(',')
        end   = x[1].split(',')
        ln = line(int(start[0]), int(start[1]), int(end[0]), int(end[1]))
        lines.add(ln)


def process_lines():
    global lines, point_matrix
    
    for ln in lines:
        point = ln.start
        # ensure line is either vertical or horizontal
        if ln.x1 != ln.x2 and ln.y1 != ln.y2:
            continue

        ### VERTICAL AND HORIZONTAL LINES ###
        # determine if vertical or horizontal
        horizontal = False
        change     = 1  # assume increasing values
        
        if ln.x1 != ln.x2:  # horizontal
            horizontal = True
            # increasing or decreasing
            if ln.x1 > ln.x2:
                change = -1
        else:               #vertical
            if ln.y1 > ln.y2:
                change = -1
            
        p = tuple(point)
        while True:
            # update point freq
            if p not in point_matrix:
                point_matrix[p] = 1
            else:
                point_matrix[p] += 1

            # move point closer to end
            if horizontal:
                point[0] += change
            else:
                point[1] += change
                
            p = tuple(point)

            if p == tuple(ln.end):
                # update ending point
                if p not in point_matrix:
                    point_matrix[p] = 1
                else:
                    point_matrix[p] += 1
                break
        
def process_lines2():
    global lines, point_matrix
    
    for ln in lines:
        point = ln.start
        
        ### DIAGONAL LINES ###
        if ln.x1 != ln.x2 and ln.y1 != ln.y2:
            if ln.x1 > ln.x2:
                x_change = -1
            else:
                x_change = 1
                
            if ln.y1 > ln.y2:
                y_change = -1
            else:
                y_change = 1

            p = tuple(point)            
            while True:
                # update point freq
                if p not in point_matrix:
                    point_matrix[p] = 1
                else:
                    point_matrix[p] += 1

                # move point closer to end
                point[0] += x_change
                point[1] += y_change
                    
                p = tuple(point)

                if p == tuple(ln.end):
                    # update ending point
                    if p not in point_matrix:
                        point_matrix[p] = 1
                    else:
                        point_matrix[p] += 1
                    break

        ### VERTICAL AND HORIZONTAL LINES ###
        else:
            # determine if vertical or horizontal
            horizontal = False
            change     = 1  # assume increasing values
            
            if ln.x1 != ln.x2:  # horizontal
                horizontal = True
                # increasing or decreasing
                if ln.x1 > ln.x2:
                    change = -1
            else:               #vertical
                if ln.y1 > ln.y2:
                    change = -1
                
            p = tuple(point)            
            while True:
                # update point freq
                if p not in point_matrix:
                    point_matrix[p] = 1
                else:
                    point_matrix[p] += 1

                # move point closer to end
                if horizontal:
                    point[0] += change
                else:
                    point[1] += change
                    
                p = tuple(point)

                if p == tuple(ln.end):
                    # update ending point
                    if p not in point_matrix:
                        point_matrix[p] = 1
                    else:
                        point_matrix[p] += 1
                    break


def count_multiple_hits():
    global point_matrix
    count = 0

    for p in point_matrix:
        if point_matrix[p] > 1:
            count += 1
    print('count =', count)
                
            
# global variables
lines = set()
point_matrix = dict()

        
get_data()
process_lines2()
count_multiple_hits()



