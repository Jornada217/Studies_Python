import numpy as np

#the elements required for reshaping are equal in both shapes

#Reshape from 1D to 2D
list = [i for i in range(13)[1:]]
array = np.array(list)
print(array)
shp_array_2D = array.reshape(4, 3)
print(shp_array_2D)
shp_array_3D = array.reshape(2, 3, 2)
print(shp_array_3D)
print()

#convert unknown dimensions
print('convert unknown dimensions')
list2 = [i for i in range(9)[1:]]
array2 = np.array(list2)
print(array2)
shp_array2 = array2.reshape(2, 2, -1)
print(shp_array2)
print('Flatten multidimensional arrays: ')
flt_shp_array2 = shp_array2.reshape(-1)
print(flt_shp_array2)