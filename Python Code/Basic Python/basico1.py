# Imports Necesarios
from sys import argv
import basico2
import empleado
import persona
import familia
import animal
import datetime
# Sys is the name of the library, but in Python is called Module

# Iniciando con Python
# Run    -> Click derecho ejecutar Python en terminal.
# Debbug -> F5 Ejecutar Debugger.

# Exercise 1 (Print)
# Use of print
print("*********# Exercise 1 (Print)*********")
print("Hello World!")
print("Hello Again")
print("I like typing this")
print("This is fun")
print("Yay! Printing.")
print("I'd much rather you 'not'.")
# Importante, se puede usar "" pero usandolas dentro de ''
print('I "said" do not touch this.')
print(" # Octothorpe ")
print()  # Imprime una linea vacia

# Exercise 2 (Comments)
print("*********# Exercise 2 (Comments)*********")
# A comment, this is so you can read you program later.
# Anything after the # is ignored by python.
print("I could have code like this.")  # and the comment after is ignored

# You can also use a comment to "disable" or comment out code:
# print("This won't run.")

print("This will run.")
print()  # Imprime una linea vacia

# Exercise 3 (Numbers and Math)
print("*********# Exercise 3 Numbers and Math*********")
print("I will now count my dogs:")

print("Huskys", 25+30/6)  # 30.0
print("Chihuahas", 100-25*3 % 4)  # 97

print("Now I will count the puppies: ")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)  # 6.75, Modulo no devuelve float

print("Is it true that 3 + 2 < 5 - 7?")

print(3+2 < 5 - 7)  # False

print("What is 3 + 2?", 3 + 2)  # 5
print("What is 5 - 7", 5 - 7)  # -2

print("Oh, that's is why it's False.")

print("How about some more")

print("Is it greater?", 5 > -2)  # True
print("Is it greater or equal?", 5 >= -2)  # True
print("Is it less or equal", 5 <= -2)  # True

print("% no devuelve Float", 7 % 6)
print("Al relacionarse con un Float devuelve float siempre", 3.0+2)
print("Orden de operaciones", 3+3*2+5*2+3 % 3)  # 3+6+10+0 = 19

# For make the operations Python use PEMDAS:
# The order is the multiplication and division first, from left to right
# and then you do addition and subtraction from left to right too.
print()  # Imprime una linea vacia

# Exercise 4
print("*********# Exercise 4 Variables and Names*********")

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only ",  drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, " people today.")
print("We have ", passengers, " to carpool today.")
print()  # Imprime una linea vacia

# Exercise 5 (Only for Python >= 3.6)
print("*********# Exercise 5 More Variables and Printing*********")

# curso1 = 'Diseño de Gráficos por computadora'
# curso2 = 'Informática y Sociedad'
# curso3 = 'Propiedad Intelectual'
# curso4 = 'Aplicaciones Informáticas Globales'
# curso5 = 'Práctica Profesional Supervisada'
# print(f"Estoy llevando los siguientes cursos: {curso1}.")

# IMPORTANT : You can only create variables that start with a character not
# with a number
print()  # Imprime una linea vacia

# Exercise 6
print("*********# Exercise 6 Strings and Text*********")
presentacion = " Mi nombre es {}"
nombre = "Luis Felipe Castro Sanchez"
print(presentacion.format(nombre))

pablo = "Hola Soy Pablo y "
ana = "Hola Soy Ana"
print(pablo+ana)
print()  # Imprime una linea vacia

# Exercise 7
print("*********# Exercise 7 More Printing*********")
print(" El carro de Luis es {}".format("negro"))
ruta1 = "Home/"
ruta2 = "Users/"
ruta3 = "Felipe"
ruta4 = "Esa es mi "
ruta5 = "ruta"

print(ruta1+ruta2+ruta3, end=' ')
print(ruta4+ruta5)

numeroVeces = 2
print(("Se esta imprimiendo {} veces ".format(numeroVeces))*numeroVeces)
print()  # Imprime una linea vacia

# Exercise 8
print("*********# Exercise 8 Printing*********")
curso1 = 'a'
curso2 = 'b'
curso3 = 'c'
curso4 = 'd'
curso5 = 'e'

cursos = " Estas son las primeras cinco letras {} , {} , {} , {} y {}"
print(cursos.format(curso1, curso2, curso3, curso4, curso5))
print()  # Imprime una linea vacia

# Exercise 9
print("*********# Exercise 9 Printing, Printing and Printing*********")
# \n permite crear un espacio en blanco
# Dentro de """ Cada linea se va a separar automaticamente

numerosSeguidos = " 1 2 3 4 5 6...."
numerosSeparados = " 1 \n 2\n 3\n 4\n 5\n 6...."

print(" Hola voy a contar de forma seguida", numerosSeguidos)
print(" Hola voy a contar de forma separada", numerosSeparados)

print(""" Linea 1
 Linea 2
 Linea 3
 Linea 4
""")
print()  # Imprime una linea vacia

# Exercise 10
print("*********# Exercise 10 What was that*********")
print("Special characters:")
print("\t  -> Para tab")
print("\\  -> Para slash invertido")
print("\t* -> Para crear un asterisco")
print()  # Imprime una linea vacia

# Exercise 11
print("*********# Exercise 11 Asking Questions*********")
# input() is used for request data entry from a user
# All the things typed come in as a strings, even if you typed numbers on the
# command line so if you like to convert them, you have to make this
# int(variableName) or int(input())
# print("What is your name? \n")
# name = input()
# print("How old are you? \n")
# age = input()
# print("How tall are you? \n")
# height = input()
# print("How much do you weigh? \n")
# weight = input()
# print("So you are {} with {} years old, {} height and {} weight".format(
#     name, age, height, weight))
print()  # Imprime una linea vacia

# Exercise 12
print("*********# Exercise 12 Prompting People*********")
# print(" Always that I use format I have to use {}")
# print(" Request data and make a question at the same time with input(?)")
# favoriteGame = input("What is your favorite game?")
# print(" His favorite game is {} ".format(favoriteGame))
print()  # Imprime una linea vacia

# Exercise 13
print("*********# Exercise 13 Parameters, Unpacking, Variables *********")
# Obtain the name of the script and the name of the variables
# It needs from sys import argv
pathArchivo = argv  # Desempaqueta lo de argv y lo pasa a nombre
print(" This is the path name of the script ", argv[0])
# Si se pasa un parametro en argv[1] se encontraria  el primer parametro
# Para pasar parametros se realiza de la siguiente forma
# Se ejecuta el script con los siguientes parametros
# python3 basico1.py parametro1 parametro2
print()  # Imprime una linea vacia


# Exercise 14
# print("*********# Exercise 14 Prompting and Passing *********")
# print(" What is your native language ?")
# nativeLanguage = input()
# dogs = int(input("How many dogs do you have?"))
# print(" So you have {} dogs and your native language is {}".format(
#    dogs, nativeLanguage))
print()  # Imprime una linea vacia


# Exercise 18
print("*********# Exercise 18 Names, Variables, Code, Functions *********")
# For define a function, we have the next syntaxis
# def nameOfTheFunction (Parameters):
# For example: define suma(numero1,numero2):


def sumaNumeros(numero1, numero2):
    return numero1+numero2


def sumaNumerosConParametrosN(*args):
    return len(args)


def imprime(nombre, edad):
    return ("Hola mi nombre es {} y tengo {} anios !!".format(nombre, edad))


def funcionSinParametros():
    print("Hola soy una funcion sin parametros")


def fibonacci(numero):
    if(numero <= 1):
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)


def factorial(numero):
    if(numero <= 1):
        return 1
    else:
        return numero * factorial(numero-1)


# Pass en python significa que no haga nada es como un return;
# Llamado de las funciones definidas
print("Suma de {} y {} da como resultado {}".format(2, 4, sumaNumeros(2, 4)))
print(sumaNumerosConParametrosN(4, 5, 6))
print(imprime('Felipe', '20'))
funcionSinParametros()
numeroFibonacci = 8
print("Fibo de {} es =".format(numeroFibonacci), fibonacci(numeroFibonacci))
numeroFactorial = 6
print("Fact de {} es =".format(numeroFactorial), factorial(numeroFactorial))
print()

# Exercise 19
print("*********# Exercise 19 Functions and Variables *********")

number = 4


def modificaraElValor(valor):
    valor = 8
    return valor


print("Mi valor original es ", number)
print("La funcion modifica el valor devuelve ", modificaraElValor(number))

if(number != 4):
    print("El valor se modifico")
else:
    print("El valor no se modifico")

print()

nombre = "Soy Luis Felipe-Vivo en Heredia"
presentacion = nombre.split('-')
print("Presentacion :")
print(presentacion[0])
print(presentacion[1])
print()

# Exercise 28
print("*********# Exercise 28 Boolean Practice *********")
if(4 == 4):
    print(" 4 es igual que 4 ")
else:
    print(" 4 no es igual que 4")

# La palabra tiene que ser exactamente igual
# Ni siquiera puede tener espacios
if("Hola" == "Hola"):
    print(" Hola es igual que Hola")
else:
    print(" Hola no es igual que Hola")


# Exercise 31 Making Decisions
print("*********# Exercise 31 Making Decisions *********")
print(" Welcome to my game, you have to take decisions for survive:")
rendirse = 0
while (rendirse == 0):
    print(" Choose between three doors :")
    numero = int(input())
    if(numero == 1):
        print("You Win !")
        rendirse = 1
    elif (numero == 2):
        print("Now Chosee between two doors: ")
        numero2 = int(input())
        if(numero2 == 1):
            print("You Win !")
            rendirse = 1
        else:
            print("You Loose :(")
            rendirse = int(input("Surrender? "))
    else:
        print("You Loose :(")
        rendirse = int(input("Surrender? "))
print()

# Casting
# int() for whole numbers, float() for number
# with decimals and str() to create an string

# Strings Methods
b = "Hello, World!"
print(b[2:5])
print(b.strip())
print()

# Exercise 32 Loops and Lists
print("*********# Exercise 32 Loops and Lists*********")
print("Creating Loops ")
animals = ['shark', 'tiger', 'snake']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
animals.append("monkey")

# To declare a for-loop, you have to do this structure: for element in elements
cont = 1
for index, creature in enumerate(animals):
    print("{}. {} ".format(index, creature))
    cont += 1
print()
for number in numbers:
    print("Number ", number)
print()
for i in range(0, 6):
    print("El valor de i es", i)

# Exercise 34 Accesing Elements of Lists
print("*********# Exercise 34 Accesing Elements of Lists*********")
people = ['Luis', 'Guillermo', 'Felipe', 'Esteban']
print("The person at 3 is  : ", people[3])
print("The third person is : ", people[2])

# Exercise 38 Doing things to Lists
print("*********# Exercise 38 Doing things to Lists*********")
reverseNumbers = []
for x in range(0, 10):
    reverseNumbers.append(x)
    print("Agregrando el valor", x)
reverseNumbers.reverse()
print(reverseNumbers)
z = 0
while z < len(reverseNumbers):
    print("Sacando el numero ", reverseNumbers.pop())
    print("Mi tamanio es : ", len(reverseNumbers))

# Exercise 39 Dictionaries
print("*********# Exercise 39 Dictionaries*********")
# The dictionaries are based on key and values, the key can be a number or
#  a letter
languages = {
    'Spanish': 'ES',
    'English': 'EN',
    'Catalan': 'CA',
    'Chinese': 'ZH'
}
language = 'Spanish'
print("{} : ".format(language), languages['Spanish'])

print(" Recorriendo dictionario : ")
for language, abbrev in list(languages.items()):
    print(" Language -> {} Abbrev -> {} ".format(language, abbrev))

print(languages)
languages[1] = "Rusian"
# print(languages.items())
print("Clave Chinese , valor : ", languages.get("Chinese"))
print("Clave 1, valor : ", languages.get(1))
print()

# Exercise 40 Modules, Classes, and Objects
print("*********# Exercise 40 Modules, Classes, and Objects*********")
# Module
# A module is like include a file .h in C++ to access variables, functions,...
# 1. First import the .py file
# import basico2
# 2. Second follow this for use what you want:
#    basico2['apple'] get apple from dict
#    basico2.apple() get apple from the module
#    basico2.tangerine same thing, it's just a variable
basico2.apple()


# Clases
# Creamos personas, gracias a la clase importada
personaCreada = persona.Persona("Felipe", 20, "Heredia")
print(personaCreada.presentacion())

# Exercise 42 Inheritance
print("*********# Exercise 42 Inheritance*********")
# Creando empleado a partir de persona
personaEmpleado = empleado.Empleado("Felipe", 20, "Heredia", "50000")
personaEmpleado.presentacion()
print(personaEmpleado.implicit())

# Excercise 43 Composition
print("*********# Exercise 43 Composition*********")
# In the composition, we have an object from another class inside a class
# The main class is animal
animal1 = animal.Animal("Mono", 20, "Cafe")
print("Datos del animal1", animal1.muestraDatos())
animal1.aumentaEdad()
print("Datos del animal1", animal1.muestraDatos())
# Then we have an object from familia class
#  it class have an object of Animal type as a attribute
familia1 = familia.Familia("Perro", 4, "Negro")
print("Datos del animal de la familia : ", animal1.muestraDatos())
animal1.aumentaEdad()
print("Datos del animal de la familia : ", animal1.muestraDatos())
print()

# Other Data Structures
print("*********#  Other Data Structures*********")
# Tuple
# For declare a tuple we have to follow this structure:
# nameOfTheTuple = ("element1","element2","element3")
# The tuples are unchangeable
fruits = ("Pear", "Apple", "Orange", 1)
for fruit in fruits:
    print(fruit)
print("This is the last element: ", fruits[fruits.count(fruits)-1])
print("Thi is the last element: ", fruits[len(fruits)-1])

# Set
fishes = set(("cat-fish", "gupi-fish", "white-fish"))
for fish in fishes:
    print(" Fish: "+fish)
print()
# Lambda
# x = lambda a, b : a * b
# print(x(2,4)) = 8

# Other important things
print("*********#  Other Important Things*********")
date = datetime.datetime.now()
print(date)
print(date.year)
print(date.strftime("%A"))
print()

# Try -Except
try:
    print(variable)
except IOError:
    print('An error occured trying to read the file.')   
except ValueError:
    print('Non-numeric data found in the file.')
except ImportError:
    print "NO module found"    
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
except NameError:
    print("Variable no declarada")
except:
    print("Ocurrio un error")
finally:
    print("Este mensaje se despliega sin importar si ocurrio un error o no")

# Remember you can use a list like an stack  ("last in -> first out")
#                             or like queues ("first in -> first out")
#   (https://docs.python.org/3/tutorial/datastructures.html)

# Funciones Utiles
# 1. Number of items of a container :
# len()
# 2. Separate a string depending of the parameter, creating an array:
# split()
# 3. Request data from the user :
# input() or input("Type your request")
# 4. Range allow to iterate from n times :
# range(0,6) do 0 to 5 counts
# 5. Append that add another element to an array :
# animals.append("monkey")
# 6. To declare an array (List) you have to make this:
# array = []
# 7. You can abort the program with:
# exit(0)
# 8. Stop a loop:
# break
# 9. For set a value like null, you have to make this:
# valor = None
# 10. For declare a list you have to make this:
# dicts = { }
# 11. You can check if a variable is empty:
# if not variable
# 12. Use type for check the type of a variable:
# type(variable)
