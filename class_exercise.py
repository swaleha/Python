class Fruit(object):

    def __init__(self):
        print("You just chose to eat a fruit!")

    def nutrition(self):
        print("Fruits are nutrient dense")

    def fruit_shape(self):
        print("Fruits come in different shapes, aroma, taste and texture" + "\n")


class Mango(Fruit):

    def __init__(self):
        print("You just chose to eat Mango. Yum Yum!")

    def nutrition(self):
        print("Mango is rich in vitamins, minerals and antioxidants.")

    def fruit_shape(self):
        print("Mango is oval, long and slender, kidney-shaped, heart-shaped or round in shape")

    def fruit_color(self):
        print("Mango is yellow, red or green in color")


F = Fruit()
F.nutrition()
F.fruit_shape()

M = Mango()
M.nutrition()
M.fruit_shape()
M.fruit_color()