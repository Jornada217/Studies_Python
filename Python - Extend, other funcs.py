import numpy as np
#list.extend() -> The list.extend() is a built-in Python function that adds the specified list elements
                   # (or any iterable) to the end of the current list.

l1 = ['John', 'Paul', 'Bill']
l2 = ['Apple', 'Banana', 'Tomatoe']
l1.extend(l2)
print(l1)

#Appending tupple to lists:
l1 = ['John', 'Paul', 'Bill']
t1 = ('Apple', 'Banana', 'Tomatoe')
l1.extend(t1)
print(l1)

#Appending a set to a list:
l1 = ['John', 'Paul', 'Bill']
s1 = {'Apple', 'Banana', 'Tomatoe'}
l1.append(s1)
print(l1)

#appending arrays:
l1 = [1, 2, 3]
s1 = [4, 5, 6]
A1 = np.array(l1)
A2 = np.array(s1)
print(A1)
print(A2)
A3 = np.append(A1, A2, axis=0)
print(A3)