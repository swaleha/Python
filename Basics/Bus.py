class Vehicle:
    color = 'White' 
    def __init__(self,name,max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"seating capacity of {self.name} is {capacity} passengers"
        
    
class Bus(Vehicle):
    
   color = 'Red'
    
class Car(Vehicle):

    pass

b = Bus('School Volvo',150, 50)
print(b.color, b.name,b.max_speed,b.mileage)
c = Car('honda', 180, 50)
print(c.color, c.name, c.max_speed, c.mileage)

print(type(b))
print(isinstance(b, Vehicle))