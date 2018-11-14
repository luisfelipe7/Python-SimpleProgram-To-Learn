# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

# Execute Python : /usr/bin/python3
# Execute File: /usr/bin/python3  pathOfTheFile


import functools
from sys import argv
import itertools


# *********************** Working with Sets **************************


# Variables
filterElement = ""

# Define a method to filter list


def filterByValue(element):
    if (((element.lower()).find(filterElement.lower())) != -1):
        return True
    else:
        return False


# Define a custom sort

def customSort(element1, element2):
    containsElement1 = False
    containsElement2 = False
    if((str(element1).lower()).find("d") != -1):
        containsElement1 = True
    if((str(element2).lower()).find("d") != -1):
        containsElement1 = True
    if((containsElement1 is True) and (containsElement2 is True)):
        if(element1 > element2):
            return -2
        else:
            return -1
    else:
        if(containsElement1 is True or containsElement2 is True):
            return -1
        else:
            if(containsElement1 is False and containsElement2 is False):
                if(element1 > element2):
                    return 0
                else:
                    return 1


# Creating a set
mySet = set(("animal1", "animal2", "animal3",
             "animal4", "dog1", "dog2", "dog3"))

# Looping on the set
for element in mySet:
    print("Element : "+str(element))

# Printing the set
print("This is my set "+str(mySet))

# Adding a element on the set, push on the first place
mySet.add("animal5")
print("This is my set with another element "+str(mySet))

# Removing an element from the set, pop the first element
mySet.pop()
print("This is my set without an element "+str(mySet))

# Filtering the set
print("Type the element to search on the set ")
filterElement = str(input())
filteredListOfAnimal = filter(filterByValue, mySet)
print("MySet with that match with the filterElement " +
      filterElement+" "+str(list(filteredListOfAnimal)))

# Sorting the set
print("Sorting the set of elements ")
sortedSet = sorted(mySet)
# sortedSet = sorted(mySet, reverse=True) DESC
print("Sorted set of elements "+str(sortedSet))
