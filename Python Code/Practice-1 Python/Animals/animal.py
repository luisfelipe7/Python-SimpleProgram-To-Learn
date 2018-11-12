# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica

from sys import argv
import datetime


class Animal(object):

    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.place = args[2]

    def __str__(self):
        return "I am an animal with the name "+self.name+", with "+str(self.age)+" years old"+" and native from "+self.place
