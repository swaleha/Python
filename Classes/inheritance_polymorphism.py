"""
Program demonstrates use of inheritance and polymorphism through video game example
"""
class Person():

    def __init__(self, fname, lname, health, status):

        self.fname = fname
        self.lname = lname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hi, I am {} {}".format(self.fname, self.lname))


class Enemy(Person):
    def __init__(self, weapon, fname, lname, health, status):
        super().__init__(fname, lname, health, status)
        self.weapon = weapon

    def hurt(self, other):

        if self.weapon == 'rock':
            other.health -= 10

        elif self.weapon == 'stick':
            other.health -= 5

        print(other.health)


    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.fname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.fname))

        if other.status == True:
            other.status = False

    def introduce(self):
        print("You are my mortal enemy!!!")


Maria = Person("Maria", "Gutierrez", 95, status = True)
Rey = Person("Rey", "Jones", 88, status = False)
Lee = Person("Lee", "Williams", 77, status = True)
Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False)

Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Rey)

Maria.introduce()
Rey.introduce()
Alex.introduce()

