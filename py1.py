from datetime import datetime
startTime = datetime.now()

input = [42, 3, -6, 24, -10, -8, 2, 20, 40]
i = 0
max = input[0]
while i < len(input): 
    a = len(input)-i #length of input minus what number your number you are on
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