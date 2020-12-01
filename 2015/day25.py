# day25

# Enter the code at row 3010, column 3019.
row    = 3010
column = 3019

def f(a):
    x = a*252533 % 33554393
    return x


code = 20151125
code_number = int(column*(column+1)/2 + (column+row - 1)*(column+row - 2)/2 - column*(column-1)/2)
print(code_number)

for i in range(code_number - 1):
    code = f(code)

print(code)


