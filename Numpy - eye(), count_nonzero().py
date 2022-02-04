import numpy as np

# np.count_nonzero() -> used to give the count of the nonzero elements present in the multidimensional array.

# np.count_nonzero() -> give the count of the nonzero elements present in the multidimensional array.

print(np.eye(4))
print()
print(np.eye(2, 3))
print()
print(np.eye(3, 4, dtype=int))
print()
print(np.eye(3, 4, dtype=float))
print()

array1 = np.eye(5)
print(array1)
count1 = np.count_nonzero(array1)
print(count1)
print()

#Multidimensional array:
array2 = [[0, 4, 6, 0, 3, 0], [1, 4, 0, 3, 4, 0]]
print(array2)
count2 = np.count_nonzero(array2)
print(count2)
count2_0 = np.count_nonzero(array2, axis=0)
count2_1 = np.count_nonzero(array2, axis =1)
print(count2_0)
print(count2_1)