# day11

def increment_password():
    global password, letters

    i = len(password) - 1

    # find right most non-z letter
    while password[i] == 'z':
        #change password[i]  to 'a'
        password = password[:i] + 'a' + password[i+1:]
        i -= 1
        
    current_letter = password[i]
    ind_of_next_letter = letters.index(current_letter) + 1
    next_letter = letters[ind_of_next_letter]
    # update password
    password = password[:i] + next_letter + password[i+1:]

def double_pair():
    global password
    for i in range(len(password) - 3):
        if password[i] == password[i+1]:
            for j in range(i+1, len(password) - 1):
                if password[j] == password[j+1] and password[j] != password[i]:
                    return True
    return False

def increasing_straight():
    for i in range(len(password) - 2):
        if (ord(password[i]) == ord(password[i+1]) - 1) and (ord(password[i]) == ord(password[i+2]) - 2):
            return True
    return False


# part 1
password = 'cqjxjnds'
# part 2
password = 'cqjxxyzz'

letters  = 'abcdefghjkmnpqrstuvwxyz'     # i, l, o not allowed


while True:
    increment_password()
    if increasing_straight():
        if double_pair():
            print(password)
            break
        
        
        






    
