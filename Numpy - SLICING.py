import numpy as np

#Array slicing
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].

list1 = [i for i in range(7)]
print(list1)
array1 = np.array(list1)
print(array1)
print(array1[2:5]) #See this includes the start index, but excludes the end index.
print(array1[:5])
print(array1[::-2])
print(array1[:1:-1])
print()

#Slicing 2D arrays
print('Slicing 2D arrays')
list2 = [[i for i in range(7)], [j for j in range(14)[7:]]]
array2 = np.array(list2)
print(array2)
print('First element: ', array2[0, ])
print('Second element: ', array2[1, ])
print(array2[1, 1:4]) #From the second element(index1), slice elements from index 1 to index 4(not included)
print(array2[1, :]) #From the second element, return all elements.
print(array2[0:2, 2]) #From both elements, return index 2
print(array2[0:2, 1:4]) #From both elements, return index 1:4(not included)
print()

#Slicing 3D arrays
print('Slicing 3D arrays')
list3 = [[i for i in range(7)], [j for j in range(14)[7:]], [k for k in range(21)[14:]]]
array3 = np.array(list3)
print(array3)
print('First element: ', array3[0, ])
print('Second element: ', array3[1, ])
print('Third element: ', array3[2, ])
print(array3[0:2, 1:4]) #From first 2 elements, return index 1:4(not included)
print(array3[: , 1:4]) #From all elements, return index 1:4(not included)
print()
print(array3[:, 1])

