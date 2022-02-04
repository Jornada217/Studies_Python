import numpy as np

# numpy.median(arr, axis = None) : Compute the median of the given data (array elements) along the specified axis.
# Median = middle term if total no. of terms are odd.
# Median = Average of the terms in the middle (if total no. of terms are even)

list1 = [20, 2, 7, 1, 34]
print(np.median(list1))

list2 = [1, 2, 7, 20, 34, 68]
print(np.median(list2))
print()

#3d array
print('working with 3D array')
list3 = [[1, 2, 7, 20, 34], [15, 6, 27, 8, 19], [23, 2, 54, 1, 4]]
print(np.median(list3))
print(np.median(list3, axis=0))
print(np.median(list3, axis=1))

result_array = np.arange(3)
print("list 4 arange: ", result_array)
print('median of list4 in result array: ', np.median(list3, axis=1, out=result_array))