#zip() iterator
#Complete walkthrough:
#https://realpython.com/python-zip-function/#understanding-the-python-zip-function

#1
for i in zip([1, 2, 3], ['tic', 'tac', 'toe']):
    print(i)

#2
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipp = zip(numbers, letters)
print(zipp) #returned an interator object
print('type of zipped: ', type(zipp))
zipped2 = list(zipp)
print('Type of list zipped object: ', zipped2)
print(zipped2)
print()

# This means that the resulting list of tuples will take the form:
        # [(numbers[0], letters[0]), (numbers[1], letters[1]),..., (numbers[n], letters[n])]
        # However, for other types of iterables (like sets), you might see some weird results:
#3
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}
zipped3 = list(zip(set1, set2))
print(type(zipped3))
print(zipped3) #[(1, 'a'), (2, 'c'), (3, 'b')]
print()
# sets don't have an specif order, and so will be the zip function, pairing unordered sets.
    #Keep this in mind when working with this function.

#4: One argument
set1 = [1, 2, 3]
zipped4 = list(zip(set1))
print(type(zipped4))
print(zipped4)
print()

#5: Multiple input iterables:
set1 = [1, 2, 3]
set2 = ['a', 'b', 'c']
set3 = ['red', 'blue', 'white']
zipped5 = list(zip(set1, set2, set3))
print(zipped5)
print()

#6: Lenght of arguments is the lenght of the shortest argument.
set1 = range(5)
set2 = range(100)
zipped6 = list(zip(set1, set2))
print(zipped6)
print()

#7: The iterator will split strings:
set1 = range(7)
set2 = 'ab+cd@123'
zipped7 = list(zip(set1, set2))
print(zipped7)
print()

#looping over multiple iterables: The most common user case of zip() function.
#8:
set1 = [1, 2, 3, 4, 5]
set2 = ['a', 'b', 'c', 'd', 'e']
for i, j in zip(set1, set2):
    print(f'Item: {i}: {j}')
print()

#9: Traversing dictionaires in parallel:
dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (x1, y1), (x2, y2) in zip(dict_one.items(), dict_two.items()):
    print(x1, ': ', y1)
    print(x2, ': ', y2)
print()

#10: Unzipping python objects:
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)