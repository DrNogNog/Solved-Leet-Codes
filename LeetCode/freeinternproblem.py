import numpy
import math
# Question One
def circle_sorter(list):
    for circle in list: # [x,y,z  x,y,z]
        x = circle[0]
        y = circle[1]
        r = circle[2]
        z = numpy.distanceformula(x,y)
        if list[circle+1] == NULL:
            print("error, no other circle")
        
        circle2 = list[circle+1]
        r2 = circle2[2]

        if (z > (r+r2)):
            print("intersection") 
# x^2 + y^2 = r^2   # x^2 + y^2 = r^2

#question 2
def multithreading(numbers):
    for i in numbers:
        math.sqrt(i)
def threads(numbers):
    number_of_threads = 10
    
#
#
#

#Question Three
def __init__(self, textfile):
    gastype = str
    number = int
    amount = int

    txt = open(textfile).read()
    array = txt.split(" ")
    for i in range(len(array)):
        if i == "gas":
        else if i == "diesel":
        else if i == "biodiesel":
        else if i ==
def checker(number):
    if number is in range(0,6):
        number = number
    else:
        print("error number is not a number labeled 1 to 5")
        return(False)
def checker2(gastype):
    if gastype is in ["gas", "diesel", "biodiesel", "hydrogen", "electricity"]
        gastype = gastype
    else:
        print("error, we do not serve that type of gas here")
        return(False)
def customer(gastype, number, amount):
    checker2(gastype)
    checker(number)
    gas_multiplier_amount = 2

    if gastype == "gas"
    


