# Contiguous Sequence By Mason Horder(For CAP Club)

input = [42, 3, -6, 24, -10, -8, 2, 20, 40]
def contiguousSequence(input):
    maxSequenceTotal = input[0]
    runningMaxTotal = input[0]
    for c in range(1, len(input)): 
        runningMaxTotal = max(input[c], runningMaxTotal + input[c]) 
        if maxSequenceTotal < runningMaxTotal:
            maxSequenceTotal = runningMaxTotal
    return maxSequenceTotal
    

print(contiguousSequence(input)) 
