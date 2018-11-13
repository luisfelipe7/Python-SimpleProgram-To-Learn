# Author: Luis Felipe Castro Sánchez
# Creation Date: 12/11/18
# GitHub User: luisfelipe7
# Version: 1.0.0
# Country: Costa Rica


from sys import argv
import datetime
from People.person import Person

# Class to create an Employee


class Employee(Person):

    # Init Method

    def __init__(self, *args):
        super().__init__(*args)
        self.company = args[3]
        self.salary = args[4]

    # Print Method

    def __str__(self):
        return (super().__str__())+'\n'+"I work for " + \
            self.company+" and they pay me "+str(self.salary)
