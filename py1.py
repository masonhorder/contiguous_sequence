import time
input = [-2, -3, 4, -1, -2, 1, 5, -3]
print(input)

i = 0
max = input[0]
while i < len(input): 
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
