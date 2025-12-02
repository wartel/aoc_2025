
f = open('values.txt', 'r')

password = 0
position = 50
max_range = 100

for line in f:

    operator = line[0]
    value = int(line[1:])
    if operator == 'L':
        position -= value
    else:
        position += value
    
    position = position%100
    if position == 0:
        password += 1
    
    #print(f"line is {line}")
    #print(f"operator: {operator}, value: {value}, position: {position}, password: {password}")
    
print(f"The password is: {password}")
