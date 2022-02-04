import numpy as np

#range() and len() are often used together when iterating over a MUTABLE SEQUENCE,
    # to access each item in the sequence by index.

#Use range() and len() in a FOR-LOOP to access each item by index

#1-D list and array
list = [i for i in range(7)]
print(list)
print('Len of list is: ', len(list))
for index in range(len(list)):
    print(list[index])
print()
array = np.array(list)
print(array)
for i in range(len(array)):
    print(array[i])
print()

