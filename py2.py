from datetime import datetime
startTime = datetime.now()

input = [-2, -3, 4, -1, -2, 1, 5, -3]

i = 0
max = input[0]
for item in input: 
    # print(input[i], i)
    a = len(input)-i
    b = 0
    d = 0
    while a > b:
        c = b + i
        b+=1
        d+=input[c]
        if d > max:
            max = d
    i += 1
print(max)

print(datetime.now() - startTime)