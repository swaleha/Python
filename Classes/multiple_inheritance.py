# class Animal():
#     def __init__(self, sound, look):
#
# class Place():
#     def __init__(self, climate, lat, lon):
#
# class Mammal(Animal, Place):
#     def __init__(self, sound, look, climate, lat, lon, food):
#         Animal.__init__(self, sound, look)
#         Place.__init__(self, climate, lat, lon)
#         self.food = food

# Parent class 1

class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("This sku is {}".format(self.sku))

# Parent class 2

class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}".format(self.section, self.type))

# child class

class Shirts(Item, Garment):

    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color

        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} is on sale!".format(self.name, self.color))


Blouse = Shirts("00001", 43, "Tops", "Formal Blouses", "White")

Blouse.print_sku()
Blouse.print_shirt()
Blouse.print_garment()