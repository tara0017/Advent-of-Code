#day9
def process(s):
    new_string = ''
    ind = 0
    c = 0
    
    #while there are "(" beyone current index
    while '(' in s[ind:]:
        c+=1
        #find first "(" at or beyond current index
        t = '0'*ind + s[ind:]
        
        start = t.index('(')
        end   = t.index(')')
        new_string += s[ind:start]  #update new_string up to the "("
        #make copies
        copies = make_copies(t, start, end)
        new_string += copies[0]
        #update index
        ind = copies[1]

    print(len(new_string))

def make_copies(s, start, end):
    mid = s.index('x')
    num_chrs  = int(s[start+1:mid])
    num_times = int(s[mid+1 : end])
    new_index = end + num_chrs + 1
    string = s[end + 1 : end + 1 + num_chrs] * num_times
    return (string, new_index)



f = open('day9_input.txt', 'r')
for x in f:
    x = x.strip()
    process(x)



