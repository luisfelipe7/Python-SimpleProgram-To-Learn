# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

# Execute Python : /usr/bin/python3
# Execute File: /usr/bin/python3  pathOfTheFile

from sys import argv
import itertools


# *********************** Working with Strings **************************

# Declaring an String
string1 = "abcdefgghijkzzlmnopqrstuvawxyz"

# Printing the String
print("This is my string:", string1)

# Count of the elements of the String
print("Elements of the string", len(string1))

# Count how many times a letter is on the string
print("Count how many time the a is on the string", string1.count('a'))

# Substring of the string
print("Print from leeter in the position 0 to the letter on the position 5",
      string1[0:6])

# Sort the letters of an string and return a list
print("Sort the letters in the right way", sorted(string1))

# Eliminate the equal letters and return a string
print("Eliminate the equal letters", ''.join(
    ch for ch, _ in itertools.groupby(string1)))

# Loop on the string
print("Loop on the string")
for letter in string1:
    print(letter)
    letter = "O"

# String before loop
print("String before loop "+string1)

# Reverse a string
print("String reverse "+string1[::-1])

# Return the index where the w is
print("String index where is the w  "+str(string1.find('w')))

# Return True or False depending if the value is on the string
print("String find the y on the array  " + str('y' in string1))

# Check if the string is a palindrome (WAY 1)
string2 = "aibohphobia"

if(string1[::-1] == string1):
    print("String1 is a palindrome")

if(string2[::-1] == string2):
    print("String2 is a palindrome")


# Checj if the string is a palindrome (WAY 2)
string2 = "aibohphobia"
reversedString2 = reversed(string2)
reversedString1 = reversed(string1)
if(list(reversedString1) == list(string1)):
    print("String1 is a palindrome")
if(list(reversedString2) == list(string2)):
    print("String2 is a palindrome")


# ***************** This is WRONG **************************
# print("String first element "+string1[0])
# string1[0] = "b"
# print("String with the first element modified "+string1[0])
