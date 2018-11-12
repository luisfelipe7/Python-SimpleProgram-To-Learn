# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

from sys import argv
import itertools


# +++++++++++++++++++++++++ Working with Strings +++++++++++++++++++++++++

# ********** Python String Methods ***********

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
    print(letter + "\n")
