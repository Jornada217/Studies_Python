
#Two sum question:
from itertools import combinations
n = 5
array1 = [1, 2, 3, 4]
array2 = [1, 2, 6]
def check_sum(array, target):
    for i in combinations(array, 2):
        if i[0] + i[1] == target:
            return True
    return False
print(check_sum(array1, n))
print(check_sum(array2, n))


#Fibonacci:
n = 11
def fibonacci(num):
    if num == 0 or num ==1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(n))

#Remove duplicates of a list
list = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 6, 6, 6, 6, 3]
def rem_dup(list):
    ind = []
    item = None
    list.sort()
    for i in list:
        if item != i:
            ind.append(i)
            item = i
    return ind
print(rem_dup(list))

#Intersection: Return the intersection of two dorted arrays.
l1 = [1, 1, 2, 3, 3, 5, 5, 5, 7, 10, 13]
l2 = [3, 5, 10, 10, 13, 21, 23, 23, 26, 26]
def intersect(list1, list2):
    n_list1 = rem_dup(list1)
    n_list2 = rem_dup(list2)
    int_list = []
    #i1, i2 = None
    for i in n_list1:
        for j in n_list2:
            if i == j:
                int_list.append(i)
    return int_list
print(intersect(l1, l2))

#Union of two sorted arrays:
l1 = [1, 2, 3, 4, 5, 2, 2, 4]
l2 = [4, 5, 6, 7, 8, 9, 10, 4, 5, 5, 6]
def union(list1, list2):
    list_union = []
    n_list1 = rem_dup(list1)
    n_list2 = rem_dup(list2)
    # list_union.append(n_list1)
    for i in n_list1:
        for j in n_list2:
            if i != j:
                list_union.append(j)
    n_union = rem_dup(list_union)
    return n_union
print(union(l1, l2))

#Addition of list to to integer and operations.
l1 = [9, 9]
l2 = [2]
def operation(list1, list2):
    strng1 = ''
    strng2 = ''
    for i in list1:
        strng1 = strng1 + str(i)
    for j in list2:
        strng2 = strng2 + str(j)
    result = float(strng1) + float(strng2)
    result_list = []
    for k in str(result)[:3]:
        result_list.append(float(k))
    return result_list
print(operation(l1, l2))

#Sort words by given alphabet:
words = ['Joao', 'Ana', 'Luis', 'Mom', 'Richard']
alphabet = 'bcdefghijklmnopqrstuvwxyza'
def sort(word, alpha):
    word = sorted(word, key = lambda wordd: [alpha.index(c) for c in wordd])
    return word
# print(sort(words, alphabet))

#Binary search tree:

