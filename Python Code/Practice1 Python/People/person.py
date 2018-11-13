# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica


from sys import argv
import datetime


class Person(object):

    def __init__(self, *args):
        self.name = args[0]
        self.gender = args[1]
        self.age = args[2]

    def __str__(self):
        return "Hello! I am "+str(self.age)+" years old, my name is "+self.name+" and I am a "+self.gender
