
f = open('values.txt', 'r')

password = 0
position = 50
max_range = 100

for line in f:

    operator = line[0]
    value = int(line[1:])
    x = range(value)
    for n in x:
        if operator == 'L':
            position -= 1
        else:
            position +=1
        
        position = position%100
        
        if position == 0:
            password +=1
            
print(f"The password is: {password}")
