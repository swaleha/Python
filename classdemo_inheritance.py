class Car(object):
    def __init__(self):
        print("You just created the car instance (i.e object)")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped")


class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW's instance")


c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()