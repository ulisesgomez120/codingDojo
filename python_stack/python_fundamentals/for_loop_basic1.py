#Basic - Print all the numbers/integers from 0 to 150.
for int in range(0,151):
    print(int)
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for int in range(5,1000001):
    if int % 5 == 0:
        print(int)
#Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for int in range(1,101):
    if int % 5 == 0:
        print("Coding")
        if int % 10 == 0:
            print(" Dojo")
    else: 
        print(int)
    
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for int in range(0,10):
    if int % 2 != 0:
        sum += int
print(sum)
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
for int in range(2018,0,-4):
    print(int)
#Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def mulitples(LowNum, highNum, mult):
    for int in range(LowNum, highNum +1):
        if int % mult == 0:
            print(int)
mulitples(2,9,3)

list = [3,5,1,2]
for i in list:
    print(i)
# print everything in list

list = [3,5,1,2]
for i in range(list):
    print(i)
# Thought it would either be an error or prints eveything but i see now it was an error

list = [3,5,1,2]
for i in range(len(list)):
    print(i)
# Thought it would print everything in list since it len is 4 but i see now that the only connection it had to list was the length