# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica


from People.person import Person
from People.employee import Employee
from Animals.animal import Animal
from Group.family import Family


# +++++++++++++++++++++++++ Working with classes +++++++++++++++++++++++++

# Creating a Person (Normal)
person1 = Person("Luis Felipe", "Man", 21)
print("Person 1")
print(person1)

# Creating an Employee (Inheritance)
employee1 = Employee("Guillermo", "Man", 21, "Solvo", 1.550)
print("Employee 1")
print(employee1)

# Creating an Animal (Normal)
animal1 = Animal("Tiger", 21, "Amazonas")
print("Animal 1")
print(animal1)

# Creat a pause on the command
input("Press enter to continue")

# Clear the screen
print("\033[H\033[J")

# Creating a family (Composition)
family1 = Family("Family 1")
print("Family 1")
print(family1)

# Sort the family list of elements
family1.orderFamilyByAge()
print("Family 1 Sorted by Age in ASC Way")
print(family1)
