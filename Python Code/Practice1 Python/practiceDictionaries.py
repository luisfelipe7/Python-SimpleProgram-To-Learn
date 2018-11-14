# Author: Luis Felipe Castro Sánchez
# Creation Date: 13/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

# Execute Python : /usr/bin/python3
# Execute File: /usr/bin/python3  pathOfTheFile

# To sort in a custom way
import functools
from sys import argv
import itertools


# *********************** Working with dictionaries **************************

# Creating a dictionary
myData = {"name": "Luis", "city": "Heredia", "country": "Costa Rica"}

# Printing a dictionary
print("This is the dictionary for my data : "+str(myData))

# Getting a value with the key
print("The value of the key "+("city")+" is: "+myData.get("city"))

# Looping on a dictionary
print("Printing the dictionary looping on each element")
for key, value in (list(myData.items())):
    print(" Key -> "+key+" / Value -> "+value)

# Inserting a element on the dictionary
myData.update(career="Systems Engineering")
print("This is the dictionary for my data updated : "+str(myData))
print("Getting the value added: "+str(myData.get("career")))

# Getting the keys
keysOfMyData = myData.keys()
for key in keysOfMyData:
    print("This is a key: "+str(key))

# Getting the values
valuesOfMyData = myData.values()
for value in valuesOfMyData:
    print("This is a value: "+str(value))

# Evaluate all elements from a dictionary
if all([(element.isnumeric() is True) for element in myData.values()]):
    print("All element are numbers")
else:
    print("All elements are not numbers")

# Evaluate all elements from a dictionary
myDataOfNumbers = {"number0": 0, "number1": 1, "number2": 2, "number3": 3}
if all([(str(element).isnumeric() is True) for element in myDataOfNumbers.values()]):
    print("All element are numbers")
else:
    print("All elements are not numbers")
