#day10
def reverse_sublist(l):
    global index, my_list
    copy_list = my_list[:]
    #print('before', len(copy_list))
    for i in range(256):
        copy_list.append(my_list[i])
    #print('after', len(copy_list))
    #print("l = ", l, 'index = ', index)
    sub_list = copy_list[index: index + l]
    #print('sub_list length ', len(sub_list))
    #print()
    sub_list.reverse()

    for i in range(l):
        y = sub_list[i]
        copy_list[(index + i) % 256] = y
    my_list = copy_list[:256]

    
lengths = [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]
skip_size = 0
my_list = []
index = 0

for i in range(256):
    my_list.append(i)

for l in lengths:
    reverse_sublist(l)
    #adjust index
    index += (l + skip_size)
    index %= 256
    skip_size += 1


print(my_list[0], my_list[1], my_list[0] * my_list[1])



