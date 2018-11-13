# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

from sys import argv

# ++++++++++++ Defining functions to work with ints +++++++++++++++++++

# Function to define if a number is multiple of 2


def parNumber(number1):
    if (number1 % 2 == 0):
        return True
    else:
        return False


# Function to define if a number is prime (Recursive)


def primeNumberRecursive(number1, value):
    if(number1 == value):
        return True
    elif (number1 % value == 0):
        return False
    else:
        return primeNumberRecursive(number1, value+1)


# Function to define if a number is an armstrong number


def armstrongNumber(number1):
    value = 0
    for element in str(number1):
        value += int(element)*int(element)*int(element)
    if (value == number1):
        return True
    else:
        return False


# Recursive Factorial Function


def recursiveFactorialFunction(number):
    if((number == 0) or (number == 1)):
        return number
    else:
        return number * recursiveFactorialFunction(number-1)


# Iterative Factorial Function


def iterativeFactorialFunction(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


# Recursive Fibonacci Function

def recursiveFibonacciFunction(number):
    if((number == 0) or (number == 1)):
        return number
    elif(number == 2):
        return 1
    else:
        return recursiveFibonacciFunction(number-1) + recursiveFibonacciFunction(number-2)


# Iterative Fibonacci Function

def iterativeFibonacciFunction(number):
    x = 0
    y = 0
    for i in range(0, number+1):
        if(i == 0):
            pass
        elif(i == 1):
            y = 1
        elif(i > 1):
            valueY = y
            y = x + y
            x = valueY
    return y

# ++++++++++++++++++++++ Working with Ints ++++++++++++++++++++++++++++


myInt = 100
print("The number "+str(myInt)+" is multiple of 2: "+str(parNumber(myInt)))
print("The number "+str(myInt)+" is a prime number : " +
      str(primeNumberRecursive(myInt, 2)))
print("The number "+str(127)+" is a prime number : " +
      str(primeNumberRecursive(127, 2)))
print("The number "+str(2)+" is a prime number : " +
      str(primeNumberRecursive(2, 2)))
print("The number "+str(3)+" is a prime number : " +
      str(primeNumberRecursive(3, 2)))
print("The number "+str(997)+" is a prime number : " +
      str(primeNumberRecursive(997, 2)))
print("The number "+str(myInt)+" is an armstrong number : " +
      str(armstrongNumber(myInt)))
print("The number "+str(663)+" is an armstrong number : " +
      str(armstrongNumber(663)))
print("The number "+str(407)+" is an armstrong number : " +
      str(armstrongNumber(407)))
print("The fact number with an iterative method of " +
      str(7)+" is : "+str(iterativeFactorialFunction(7)))
print("The fact number with a recursive method of " +
      str(7)+" is : "+str(recursiveFactorialFunction(7)))
print("Recursive Fibonnaci result of "+str(0) +
      " is : "+str(recursiveFibonacciFunction(0)))
print("Recursive Fibonnaci result of "+str(7) +
      " is : "+str(recursiveFibonacciFunction(7)))
print("Iterative Fibonnaci result of "+str(0) +
      " is : "+str(iterativeFibonacciFunction(0)))
print("Iterative Fibonnaci result of "+str(7) +
      " is : "+str(iterativeFibonacciFunction(7)))      
print("Iterative Fibonnaci result of "+str(10) +
      " is : "+str(iterativeFibonacciFunction(10)))          