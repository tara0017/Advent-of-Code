# day25

def find_loop_size(n):
    val  = 1
    loop = 0
    while val != n:
        val *= 7
        val %= 20201227
        loop += 1

    return loop

def transform_value(subj_num, loop_size):
    val = 1
    for i in range(loop_size):
        val *= subj_num
        val %= 20201227

    return val


door_pub_key = 11562782   
card_pub_key = 18108497  

# get loop sizes for each
door_loop_size = find_loop_size(door_pub_key)
card_loop_size = find_loop_size(card_pub_key)

# get encryption key
encr_key = transform_value(door_pub_key, card_loop_size)

print(encr_key)


