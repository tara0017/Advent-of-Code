# day6

def group_yes(g):
    answered_yes = set()
    
    # loop through each person
    for person in g:

        # loop through each question and add that question to set
        for question in person:
            answered_yes.add(question)
            
    return len(answered_yes)


def consensus_yes(g):
    answered_yes = set()

    # add all of 1st person's answers
    for q in g[0]:
        answered_yes.add(q)

    # check the rest of the people in the group
    for i in range(1, len(g)):
        items_to_remove = []

        # check each existing answer against next person's answers
        for a in answered_yes:
            if a not in g[i]:
                items_to_remove.append(a)

        # remove answers that do not appear for this individual
        for item in items_to_remove:
            answered_yes.remove(item)

    return len(answered_yes)


total_1 = 0
total_2 = 0
group = []

f = open('day6.txt','r')
for x in f:
    if x == '\n':
        # part 1
        total_1 += group_yes(group)

        # part 2
        total_2 += consensus_yes(group)
        
        group = []
    else:
        x = x.replace('\n', '')
        group.append(x)


print(total_1)
print(total_2)



        
