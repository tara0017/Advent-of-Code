# day4

import hashlib


def get_md5_hash(key):
    hasher = hashlib.md5()
    hasher.update(key.encode('utf-8'))
    return format(hasher.hexdigest())

number = 0
while(True):
    number += 1

    key = 'bgvyzdsv' + str(number)
    ans = get_md5_hash(key)

    if ans[:6] == '000000':
        print(number, key)
        print(ans)
        break

