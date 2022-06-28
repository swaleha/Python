"""
Object oriented programming
"""

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make_car = make
        self.model_car = model

    def info(self):
        print("Make of the car:" + self.make_car)
        print("Model of the car:" + self.model_car + "\n")


c1 = Car('BMW', '550i')
c1.info()


c2 = Car('Audi', 'Q3')
c2.info()


c3 = Car('Benz', 'E350')
c3.info()
