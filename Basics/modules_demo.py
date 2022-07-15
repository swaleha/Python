"""
https://docs.python.org/3/library
"""
#import math
from math import sqrt

#import modulespackage.car as car
#from modulespackage import car

from modulespackage.car import info

class ModulesDemo(object):

    def builtin_modules(self):
        print(sqrt(100))

    def car_description(self):
        make = "BMW"
        model = "550i"

        #car.info(make, model)

        info(make, model)


m = ModulesDemo()
m.builtin_modules()
m.car_description()
