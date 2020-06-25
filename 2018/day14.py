#day 14
def create_new_recipe():
    global recipes, elf1_index, elf2_index
    sum_of_recipes = recipes[elf1_index] + recipes[elf2_index]
    if sum_of_recipes < 10:
        recipes.append(sum_of_recipes)
    else:
        digit_1 = sum_of_recipes % 10
        digit_2 = int(sum_of_recipes / 10)
        recipes.append(digit_2)
        recipes.append(digit_1)
        
def update_elf_location():
    global recipes, elf1_index, elf2_index
    length = len(recipes)
    elf1_move = recipes[elf1_index] + 1
    elf2_move = recipes[elf2_index] + 1
    elf1_index = (elf1_index + elf1_move) % length
    elf2_index = (elf2_index + elf2_move) % length


def get_string():
    global recipes, after_how_many_recipes
    s = ""
    for i in recipes:
        s += str(i)
    return s[after_how_many_recipes: after_how_many_recipes + 10]


def get_recipe_seq():
    global recipes, recipe_number, seq
    s = ''
    for i in range(recipe_number, recipe_number + len(seq)):
        s += str(recipes[i])
    #print(s)
    return s

        

    

recipes = [3, 7]
elf1_index = 0
elf2_index = 1

#part 2
answer_found = False
recipe_number = 0
seq = '633601'
                   
while not answer_found:
    create_new_recipe()
    update_elf_location()
    while len(recipes) > recipe_number + len(seq):
        if get_recipe_seq() == seq:
            answer_found = True
            print(recipe_number)
            break
        else:
            recipe_number += 1
    


    
"""
#part 1
after_how_many_recipes = 633601
while len(recipes) < 10 + after_how_many_recipes:
    #print(recipes)
    create_new_recipe()
    #print(recipes)
    update_elf_location()
    #print(elf1_index, elf2_index)
    #print("--------------------------------")

print(get_string())
"""


