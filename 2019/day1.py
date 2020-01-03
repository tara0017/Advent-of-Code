#day1
f = open("day1_input.txt", "r")

#part 1
"""
total_fuel = 0
for i in f:
    total_fuel += int(int(i)/3 - 2)
print(total_fuel)
"""


#part 2
def find_module_fuel(w):
    module_fuel = 0
    while w > 0:
        next_fuel_amount = int(w/3 - 2)
        if next_fuel_amount > 0:
            module_fuel += next_fuel_amount
            w = next_fuel_amount
        else:
            return module_fuel

"""
#practice
print(find_module_fuel(100756))
"""
total_fuel = 0

for i in f:
    weight = int(i)
    total_fuel += find_module_fuel(weight)


print(total_fuel)
