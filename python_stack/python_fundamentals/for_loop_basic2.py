# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def biggie(list):
    for i in range(len(list)):
        if list[i] > 0:
           list[i] = "big"
    return list
print(biggie([1,2,-3,-3,1]))

# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def countPositives(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
    list[-1] = count
    return list
print(countPositives([1,2,3,4,4,4]))

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(list):
    sum = 0
    for i in list:
        sum += i
    return sum
print(sumTotal([1,2,3,4]))

# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def avg(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)
print(avg([1,2,3,4]))

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def length(list):
    return len(list)
print(length([1,1,1]))

# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def min(list):
    if len(list) <= 0:
        return False
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
print(min([1,2,3,-3,3,1]))

# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def max(list):
    if len(list) <= 0:
        return False
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print(max([1,2,3,-3,4,1]))

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ulti(list):
    dic = {
        "sumTotal": sumTotal(list),
        "average": avg(list),
        "maximum": max(list),
        "minimum": min(list),
        "length": length(list)
    }
    return dic
print(ulti([1,2,3]))

# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverse(list):
    # alt would be
    # return list[::-1]
    listLength = len(list)
    for i in range(listLength - 1,-1,-1):
        list.append(list[i])
    return list[listLength:]
print(reverse([1,2,3,4]))