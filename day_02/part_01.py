# open file
f = open('values.txt', 'r')
f=f.read()

x = f.split(",")

answer = 0

for x in x:
    start_value = int(x.split('-')[0])
    end_value = int(x.split('-')[1])+1
    # print(x, start_value, end_value)

    for y in range(start_value, end_value):
        length = len(str(y))
        if length%2 == 0:
            half = int(length / 2)

            first_part = int(str(y)[0:half])
            second_part = int(str(y)[half:])
        
            if first_part == second_part:
                print(f"Invalid ID: {y}")
                answer += y

print(f"The answer is: {answer}")



