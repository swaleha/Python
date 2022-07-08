class Vehicle:
    Make = ""
    Model = ""
    Color = ""
    def __init__(self, max_speed, max_mileage):
        self.max_speed = max_speed
        self.max_mileage = max_mileage

ModelX = Vehicle(250, 15)
print("ModelX mileage and Speed is:",ModelX.max_mileage, ModelX.max_speed)
