# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica


# Execute Python : /usr/bin/python3
# Execute File: /usr/bin/python3  pathOfTheFile

# To sort in a custom way
import functools
from sys import argv
import itertools


# *********************** Working with List **************************


# ** Variables **

filterElement = ""


# Function to sum 5 each element of the list

def sumFive(x):
    return x+5


# Method to get the potency


def potencia(c):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

# Method to print in order way


def imprime_ordenado(c):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)

# Method to get the combinations from a list


def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]

# Method to insert on specific position


def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]

# Method to insert on multiple positions


def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]

# Method to permute on a list


def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s)
                for s in permuta(c[1:])],
               [])


# Define a method to filter list 

def filterByValue(element):
    if (((element.lower()).find(filterElement.lower())) != -1):
        return True
    else:
        return False


# Defining an specific way to sort the elements

def sortListBySecondElement(elem):
    return elem[1]

# Sorting with first even elements and then odd elements
# In custom compare the list sort according with the value of each element from the list
# Order in asc order so:
# -2 -> Bigger element and even
# -1 -> Smaller element and even (Even)
#  1 -> Not even (Not Even)
#  1.1 -> Not Even but Bigger
#  1.2 -> Not Even but smaller
# To sort in a custom way


def sortListByEvenElement(elem1, elem2):
    evenElem1 = False
    evenElem2 = False
    if(elem1 % 2 == 0):
        evenElem1 = True
    if(elem2 % 2 == 0):
        evenElem2 = True
    if((evenElem1 is True) and (evenElem2 is True)):
        if(elem1 > evenElem2):
            return -1
        else:
            return -2
    else:
        if((evenElem1 is False) and (evenElem2 is False)):
            if(elem1 > evenElem2):
                return 1.1
            else:
                return 1.2
        else:
            if(evenElem1 is True):
                return -1
            else:
                return 1


# Creating a list
myListOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The sum of the elements of the list
print("The sum of the elements of the list is : ", sum(myListOfNumbers))

# Appending a element on the list
myListOfNumbers.append(11)
print("This is myListOfNumbers with other element : "+str(myListOfNumbers))

# Looping on a list of elements with the index of each element
for index, number in enumerate(myListOfNumbers):
    print(str(index)+". "+str(number))

# Looping only with the value of the element in each field
for number in myListOfNumbers:
    print("I am a element from myListOfNumbers : "+str(number))

# Pop an element from the list of numbers, pop the last element
myListOfNumbers.pop()
print("This is myListOfNumbers with a drop element : "+str(myListOfNumbers))
print("Appending elements to the list to sorted")
myListOfNumbers.append(0)
myListOfNumbers.append(30)
myListOfNumbers.append(40)

# Ordering the elements from the list in asc order, the default way to order elements is on asc order
# Sort order the elements without set a key
myListOfNumbers.sort()
print("myListOfNumbers sorted in asc :"+str(myListOfNumbers))
myListOfNumbers.sort(reverse=True)
print("myListOfNumbers sorted in desc :"+str(myListOfNumbers))

# Creating a way to sort list with two elements, sort by second element
myListOfNumbersWithTwoElements = [
    (1, 4), (2, 5), (1, 1), (9, 9), (5, 3), (0, 2)]
myListOfNumbersWithTwoElements.sort(key=sortListBySecondElement)
print("Sorting myListOfNumbersWithTwoElements according with the second element " +
      str(myListOfNumbersWithTwoElements))

# Sorting List by even first and in asc order
# To sort in a custom way
myListOfNumbers.sort(key=functools.cmp_to_key(sortListByEvenElement))
print("myListOfNumbers sorted by desc and even first :"+str(myListOfNumbers))

# Evaluate all elements from a list
if all([element > 5 for element in myListOfNumbers]):
    print("All larger than 5")
else:
    print("All elements are not larger than 5")

# Evaluate if at least one element of the list satisfy the condition
if any([element > 5 for element in myListOfNumbers]):
    print("At least one element is largen than 5")
else:
    print("All are not larger than 5")

# List of String
# Filtering List of Strings
myListOfPeople = ["Luis", "Guillermo", "Yenifer", "Rosario"]
print("Write the value you want to search on the names")
filterElement = str(input())
filteredListOfPeople = filter(filterByValue, myListOfPeople)
print("MyListOfPeople with that match with the filterElement "+filterElement+" "+str(list(filteredListOfPeople)))


# Printing an specific element from the list
print("The first element from myListOfPeople is "+str(myListOfPeople[0]))

# Apply Map on a List
myListOfNumbers3 = [1, 2, 3, 4, 5]
result = list(map(sumFive, myListOfNumbers3))
print("MyListOfNumbers3 with five more on each element "+str(result))

# Lambda function 
square = lambda x: x**2
print(" Square of 3 is "+str(square(3)))

# Obtain combinations
# imprime_ordenado(combinaciones(myListOfNumbers, 3))
# Obtain permutations
# imprime_ordenado(permuta(myListOfNumbers))



















# Other Example of sort
# import functools
#
# lst = [list(range(i, i+5)) for i in range(5, 1, -1)]
#
# def fitness(item):
#    return item[0]+item[1]+item[2]+item[3]+item[4]
# def compare(item1, item2):
#    return fitness(item1) - fitness(item2)
#
# sorted(lst, key=functools.cmp_to_key(compare))
