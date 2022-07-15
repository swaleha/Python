"""
This program demonstrates the use of nested dictionary
d = {"k1":{"nestk1":"nestvalue1", "nestk2":"nestvalue2"}}
"""

cars = {'bmw':{'model':'550i', 'year':2016}, 'benz':{'model':'E350', 'year':2016}}
bmw_year = cars['bmw']['year']
print(bmw_year)

benz_model = cars['benz']['model']
print(benz_model)