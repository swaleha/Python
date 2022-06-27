"""
Object oriented programming
"""

class Car(object):

    def __init__(self, make, model = '550i'):
        self.make_car = make
        self.model_car = model


c1 = Car('bmw')
print(c1.make_car)

c2 = Car('audi')
print(c2.make_car)

c3 = Car('benz')
print(c3.make_car)

print(c1.model_car)