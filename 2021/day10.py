# day 10

def check_validity(x):
    global incomplete_chunks
    
    open_chunks = []
    open_chars  = '<({['
    close_chars = '>)}]'

    for char in x:
        if char in open_chars:
            open_chunks.append(char)
        elif char in close_chars:
            if is_correct_close(open_chunks[-1], char):
                del open_chunks[-1]
            else:
                return char

    # chunk is legal look to see if it has parts still open
    if len(open_chunks) > 0:
        incomplete_chunks.append(open_chunks)
    return 1


def is_correct_close(open_char, char):
    if open_char == '(' and char == ')':
        return True
    elif open_char == '[' and char == ']':
        return True
    elif open_char == '<' and char == '>':
        return True
    elif open_char == '{' and char == '}':
        return True
    else:
        return False


    
def get_score(seq):
    score = 0
    for i in range(len(seq))[::-1]:
        if seq[i] == '(':
            score = 5*score + 1
        elif seq[i] == '[':
            score = 5*score + 2
        elif seq[i] == '{':
            score = 5*score + 3
        elif seq[i] == '<':
            score = 5*score + 4
    return score


syntax_error_score = 0
incomplete_chunks = []

f = open('day10.txt','r')
for x in f:
    illegal_char = check_validity(x)
    if illegal_char == 1:
        continue
    elif illegal_char == ')':
        syntax_error_score += 3
    elif illegal_char == ']':
        syntax_error_score += 57
    elif illegal_char == '}':
        syntax_error_score += 1197
    elif illegal_char == '>':
        syntax_error_score += 25137
        

print('Part 1:', syntax_error_score)


scores = []
for seq in incomplete_chunks:     
    scores.append(get_score(seq))
    
scores.sort()
median_score = scores[int((len(scores) - 1)/2)]
print('Part 2:', median_score)




    





