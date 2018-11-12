# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica


from sys import argv
import datetime
from Animals.animal import Animal
from People.employee import Employee
from People.person import Person

# Class to create a family with multiple members and a animal (dog)


class Family(object):

    # Method to initialize the family and each member

    def __init__(self, *args):
        self.name = args[0]
        print("How many members have your family?")
        self.numberOfMembers = int(input())
        self.initPeopleList(self.numberOfMembers)

    # Method to initialize and request the data to creata the members

    def initPeopleList(self, number):
        membersOfTheFamily = []
        for i in range(0, number):
            print("Type the name of a member")
            name = str(input())
            print("Type Women or Mand depending of the gender of the member")
            gender = str(input())
            print("Type the age of the member")
            age = int(input())
            person1 = Person(name, gender, age)
            membersOfTheFamily.append(person1)
        self.members = membersOfTheFamily

    # Method to get the data from the family

    def __str__(self):
        familyData = "The family name is "+self.name + \
            " and have "+str(self.numberOfMembers)
        membersData = ". The family members are: "
        for member in self.members:
            membersData += "\n "+member.name+" , " + \
                member.gender+" - "+str(member.age)
        return familyData+membersData

    # Sort the members of the family by the age of each one in asc order

    def orderFamilyByAge(self):
        self.members = sorted(
            self.members, key=lambda x: x.age)  # ASC ORDER BY AGE
    #   self.members = sorted(self.members, key=lambda x: x.age, reverse=True) # DESC ORDER BY AGE
