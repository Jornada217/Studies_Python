import numpy as np

#The unique() function is used to find the unique elements of an array.
list1 = [[1, 1], [2, 3], [3, 4]]
array1 = np.array(list1)
print(np.unique(array1))
print(np.unique(array1, return_index=True))
print(np.unique(array1, return_inverse=True))
print(np.unique(array1, return_inverse=True)[0])
print(np.unique(array1, return_inverse=True)[1])
print(np.unique(array1, return_counts=True))