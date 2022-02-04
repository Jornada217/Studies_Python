import numpy as np
#values() returns a view object. The view object contains the values of the dictionary, as a list.
#values() doesn't take any parameters

#Example 01:
car = {'Brand': 'Ford',
       'Model': 'Mustang',
       'Colour': 'Green',
       'Doors': 'Four Doors',
       'Engine': 'V8 Bi-turbo',
       'Year': '2021'}
print(car)
values = car.values()
print(values)
car['year'] = 1964
print(car)
print(values)
print()
#Parsing values based on selecting ids:
values_car = np.unique(values)
print('Type of data for values_car: ', type(values_car))
print(values_car)
chunks = dict()
for i in values_car:
       selection = values_car[:, ] == i
       print(selection)
       print(type(selection))
       # chunks[i] = values_car[selection, :]
       # print(chunks[i])

#Values() is a view object, that updates every time the list changes.

# values[:, chunk_index]