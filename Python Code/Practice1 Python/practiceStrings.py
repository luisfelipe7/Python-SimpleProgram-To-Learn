# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

from sys import argv
import itertools


# +++++++++++++++++++++++++ Working with Strings +++++++++++++++++++++++++

# ******************* Python String Methods ************************************

string1 = "abcdefgghijkzzlmnopqrstuvawxyz"

print("This is my string:", string1)
print("Elements of the string", len(string1))
print("Count how many time the a is on the string", string1.count('a'))
print("Print from leeter in the position 0 to the letter on the position 5",
      string1[0:6])
print("Sort the letters in the right way", sorted(string1))
print("Eliminate the equal letters", ''.join(
    ch for ch, _ in itertools.groupby(string1)))
print("Loop on the string")
for letter in string1:
    print(letter)
    letter = "O"
print("String before loop "+string1)
print("String reverse "+string1[::-1])
print("String index where is the w  "+str(string1.find('w')))
print("String find the y on the array  " + str('y' in string1))

# ***************** Palindrome or not Palindrome WAY 1 **************************
string2 = "aibohphobia"

if(string1[::-1] == string1):
    print("String1 is a palindrome")

if(string2[::-1] == string2):
    print("String2 is a palindrome")


# ***************** Palindrome or not Palindrome WAY 2 **************************

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
