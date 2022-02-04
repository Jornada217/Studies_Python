import numpy as np

#nan, isnan
list1 = [1, 0, np.nan, 3]
print(list1)
for i in list1:
    print(np.isnan(i))
print()

#nanmedian() - calucate the median of array ignoring the NaN value.
print('nanmedian')
list2 = [[1, np.nan, 2, 7, np.nan,20, 34], [15, 6, np.nan, 27, 8, 19, np.nan], [23, 2, np.nan, 54, np.nan, 1, 4]]
array2 = np.array(list2)
print(array2.shape, array2.shape[0], array2.shape[1])
print(array2)
for i in array2:
    print(np.isnan(i))
print('Median of array including nan values: ', np.median(array2))
print('Median of array using nanmedian() function: ', np.nanmedian(array2))