def user_info(name, age=1, city="Tucson"):
    """
    This function prints name, age and city 
    from arguments provided to the function.
    """
    print("{} is {} years old, from {}".format(name, age, city))


user_info("John",18,"Raleigh")
user_info("Jerry")
user_info(age=54, name='Macey')

def application(fname, lname, company, email, *args, **kwargs):
    """
    This function shows the use of *args and **kwargs
    *args allows any number of variables (positional arguments) that follow 
    formal positional arguments within a single function without 
    defining them ahead of time

    **kwargs allows any number of keyword arguments that follow  
    formal positional arguments within a single function without 
    defining them ahead of time 
    
    """
    print("{} {} works at {}. Her email ID is {}".format(fname, lname, company, email))


application("Jane", "Doe", "Google", "jane.doe@google.com", "Learn2Code.org", 100000, hire_date = '08-10-2022')