"""
This program shows what are class, instance and static methods in Python

"""

class Student:
    # class variable
    school_name = 'ABC School'
    
    # instance variables in instance method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # instance method
    def show(self):
        
        # instance variables (name, age)
        print("Student:", self.name, self.age)
        
        # class variable
        print("Student:",Student.school_name)
        
    @classmethod
    def change_school(cls, name):
        cls.school_name = name
        
    @classmethod
    def show_school_name(cls):
        return f"The name of the school is {format(cls.school_name)}"
        
    @staticmethod
    def find_notes(subject_name):
        return ['chapter 1', 'chapter 2', 'chapter 3']
    
    
# create object
jessica = Student("Jessica", 15)
    
# call instance method
jessica.show()

# call class method using the class 
Student.change_school('XYZ school')

# call class method using the class
print(Student.show_school_name())
    
# call class method using the object
jessica.change_school('PQR school')
    
# call static method using the class 
print(Student.find_notes('Math'))
    
# call static method using the object
print(jessica.find_notes('Math'))
