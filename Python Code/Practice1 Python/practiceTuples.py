# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

# To sort in a custom way
import functools
from sys import argv
import itertools


# *********************** Working with Tuples **************************

#  Creating a tuple
myTuple = ("Costa Rica", "Peru", "Nicaragua", "Jamaica")

#  Printing a tuple
print("This my tuple "+str(myTuple))

# Count how many times an element is on the tuple
print("Costa Rica is on the tuple "+str(myTuple.count("Costa Rica"))+" times")

# Obtain the index from a element
print("Costa Rica is on the index " +
      str(myTuple.index("Costa Rica"))+" from the tuple")

# Obtain an specific element from the tuple
print("Obtaining the element on the second index "+myTuple[2])
