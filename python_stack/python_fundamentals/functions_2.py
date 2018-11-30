# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
def countDown(input):
    arr = []
    for num in range(input,-1,-1):
        arr.append(num)
    return arr
print(countDown(5))

# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
def printReturn(list):
    print(list[0])
    return list[1]
print(printReturn([1,2]))

# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
def firstPlus(list):
    return list[0] + len(list)
print(firstPlus([1,2,3]))

# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False
def greater(list):
    if len(list) <= 1:
        return False
    arr = []
    second = list[1]
    for i in list:
        if i > second:
            arr.append(i)
    print(len(arr))
    return arr
print(greater([3,2,3,3,1]))

# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthAndValue(size, value):
    return [value] * size
print(lengthAndValue(3,9))

