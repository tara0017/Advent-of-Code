#day7
def passes_abba_test(s):
    for i in range(len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2]:
            if s[i] != s[i+1]:
                return True
    return False

def passes_aba_test(s):
    result = []
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            result.append(s[i:i+3])
    #print(result)
    return result
            
    
count = 0

f = open('day7_input.txt','r')
"""
for x in f:
    x = x.replace('[', ' [')
    x = x.replace(']', '] ')
    x = x.split()
    is_abba = False
    dq      = False
    
    for s in x:
        if '[' in s:
            if passes_abba_test(s):
                dq = True
                break
        else:
            if is_abba == False:
                is_abba = passes_abba_test(s)

    if is_abba and not dq:
        #print(x)

        in_brackets = set()
        outside_brackets = set()
        
        for s in x:
            if '[' in s:
                aba = passes_aba_test(s)
                for a in aba:
                    in_brackets.add(a)                
            else:
                aba = passes_aba_test(s)
                for a in aba:
                    outside_brackets.add(a)
                    
        for a in in_brackets:
            b = a[1] + a[0] + a[1]
            if b in outside_brackets:
                #print(a, b, x)
                count += 1


        
    #break
        
"""
g = []

for x in f:
    x = x.replace('[', ' [')
    x = x.replace(']', '] ')
    x = x.split()
    is_abba = False
    dq      = False
    
    for s in x:
        if '[' in s:
            if passes_abba_test(s):
                dq = True
                break
        else:
            if is_abba == False:
                is_abba = passes_abba_test(s)

    if is_abba and not dq:
        print(x)
        count += 1
        g.append(x)
        
    #break
print(count)

count = 0

for x in g:
    in_brackets = set()
    outside_brackets = set()
    
    for s in x:
        if '[' in s:
            aba = passes_aba_test(s)
            for a in aba:
                in_brackets.add(a)                
        else:
            aba = passes_aba_test(s)
            for b in aba:
                outside_brackets.add(b)
                
    for d in in_brackets:
        c = d[1] + d[0] + d[1]
        if c in outside_brackets:
            #g.append(x)
            #print(a, b, x)
            count += 1
    #break

print(count)
            

"""
for x in f:
    x = x.replace('[', ' [')
    x = x.replace(']', '] ')
    x = x.split()
    is_abba = False
    dq      = False
    
    for s in x:
        if '[' in s:
            if passes_abba_test(s):
                dq = True
                break
        else:
            if is_abba == False:
                is_abba = passes_abba_test(s)

    if is_abba and not dq:
        print(x)
        count += 1
    #break


for x in f:
    x = x.replace('[', ' [')
    x = x.replace(']', '] ')
    x = x.split()
    in_brackets = set()
    outside_brackets = set()
    
    for s in x:
        if '[' in s:
            aba = passes_aba_test(s)
            for a in aba:
                in_brackets.add(a)                
        else:
            aba = passes_aba_test(s)
            for b in aba:
                outside_brackets.add(b)
                
    for d in in_brackets:
        c = d[1] + d[0] + d[1]
        if c in outside_brackets:
            #g.append(x)
            #print(a, b, x)
            count += 1
    #break
"""
    
