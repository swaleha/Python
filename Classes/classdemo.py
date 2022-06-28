import random


class Person:

    def __init__(self, fname, lname, health, status):
        "initialize attributes to be used by all methods in the class by creating objects of the class"

        self.fname = fname
        self.lname = lname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hi, I am {} {}.".format(self.fname, self.lname))

    def emote(self):
        emotion = random.randrange(1, 3)

        if emotion == 1:
            print("{} is happy today".format(self.fname))

        elif emotion == 2:
            print("{} is sad today".format(self.fname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))

        elif self.health >= 75:
            print("{} is little bit tired today.".format(self.fname))

        elif self.health >= 51:
            print("{} feels unwell.".format(self.fname))

        elif self.health >= 40:
            print("{} goes to the doctor".format(self.fname))

        else:
            print("{} is unconscious".format(self.fname))


Maria = Person("Maria", "Gutierrez", 95, status=True)
Ray = Person("Ray", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

Maria.introduce()
Ray.introduce()
Lee.introduce()

Maria.status_change()
Ray.status_change()
Lee.status_change()
