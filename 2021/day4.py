# day4


class bingo_board():
    
    def __init__(self, board):
        self.board = board
    
    def get_sum_of_uncrossed_values(self):
        total = 0
        for row in self.board:
            for value in row:
                if int(value) > 0:
                    total += int(value)
        return total

    def print_board(self):
        for row in self.board:
            print(row)
        print('-----------------------')

    def is_row_complete(self, row):
        for n in self.board[row]:
            if n != -1:
                return False
        return True

    def is_col_complete(self, col):
        for i in range(5):
            if self.board[i][col] != -1:
                return False
        return True

    def remove_value(self, value):
        for i in range(5):
            for j in range(5):
                if int(self.board[i][j]) == value:
                    self.board[i][j] = -1
                    return (i,j)
        return False


def play_game():
    for n in called_numbers:
        for b in bingo_grids:
            result = b.remove_value(n)
            if result != False:
                if b.is_row_complete(result[0]) or b.is_col_complete(result[1]):
                    b.print_board()
                    total = b.get_sum_of_uncrossed_values()
                    print('n=',n, 'total=',total, 'score=',n*total)
                    return
            
        
def play_game2():
    grids_to_remove = set()
    
    for n in called_numbers:
        grids_to_remove.clear()
        
        for b in bingo_grids:
            result = b.remove_value(n)
            if result != False:
                if b.is_row_complete(result[0]) or b.is_col_complete(result[1]):
                    if len(bingo_grids) == 1:
                        b.print_board()
                        total = b.get_sum_of_uncrossed_values()
                        print('n=',n, 'total=',total, 'score=',n*total)
                        return
                    else:
                        grids_to_remove.add(b)
        for grid in grids_to_remove:
            bingo_grids.remove(grid)
                


#called_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
called_numbers = [30,35,8,2,39,37,72,7,81,41,25,46,56,18,89,70,0,15,84,75,88,67,42,44,94,71,79,65,58,52,96,83,54,29,14,95,66,61,97,68,57,90,55,32,17,47,20,98,1,69,63,62,31,86,77,85,87,93,26,40,24,19,48,76,73,49,34,45,82,22,80,78,23,6,59,91,64,43,21,51,13,3,53,99,4,28,33,74,12,9,36,50,60,11,27,10,5,16,92,38]

#f = open('day4test.txt', 'r')
f = open('day4.txt', 'r')

bingo_grids = set()
board = []

for x in f:
    x = x.strip()
    if x == '':
        bingo_grids.add(bingo_board(board))
        board = []
        continue
    else:
        
        x = x.split()
        board.append(x)

# part 1
#play_game()


# part 2
play_game2()


    




