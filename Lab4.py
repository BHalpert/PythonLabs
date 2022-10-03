import random

# part 1
arr = [random.randint(1, 20) for x in range(10)]
print(arr)

mean = 0
for x in range(10):  # adds together the 10 numbers
    mean = arr[x] + mean
print("mean is: ", mean/10)

smallest = arr[0]
index = 0
for x in range(10):
    if arr[index] > arr[x-1]: # determines if next value in array is smaller
        smallest = arr[x - 1]
        index = x - 1
print("smallest value: ", smallest, " index: ", index)

# part 2
print('Enter a number:')
num = int(input())
if num < 0:  # determines if valid number
    print("must be positive")
    quit()
else:
    arr2 = []
    while int(num) >= 1:  #
        arr2.insert(0, int(num) % 10)
        num = num/10
print(arr2)

# part 3
arrA = [random.randint(1,20) for x in range(10)]
arrA.sort()
print(arrA)
arrB = [random.randint(1, 20) for x in range(10)]
arrB.sort()
print(arrB)

arrC = []
inda = 0
indb = 0
for x in range(len(arrA + arrB)):  # goes through the entire loop
    if inda >= len(arrA):  # checks if it has reached the end of one of the arrays
        arrC.insert(0, arrB[indb])
        indb += 1
    elif indb >= len(arrB):
        arrC.insert(0, arrA[inda])
        inda += 1
    else:
        if arrA[inda] < arrB[indb]:  # checks which array has a smaller number in the array
            arrC.insert(0, arrA[inda])
            inda += 1
        else:
            arrC.insert(0, arrB[indb])
            indb += 1

arrC.reverse()

print(arrC)
