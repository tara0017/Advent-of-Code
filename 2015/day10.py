# day10

seq = '1113222113'
turns = 50

for j in range(turns):
    next_seq = ''
    i = 0
    while i < len(seq):
        consec_values = 1
        if i < len(seq) - 1:
            while seq[i+1] == seq[i]:
                consec_values += 1
                i += 1
                if i == len(seq) - 1:
                    break
        next_seq += (str(consec_values) + seq[i])
        i += 1
    seq = next_seq

print(len(seq))

