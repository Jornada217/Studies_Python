#Factorial
def factorial(n):
    result = 1
    for i in range (2, n+1):
        result *= i
    return result

print(factorial(4))


#Mean of numbers in a list
list1 = [4, 36, 45, 50, 75]
list2 = []

def mean(numbers):
    if len(numbers) > 0:
        return sum(numbers) / len(numbers)
    else:
        return float('NaN')
print(mean(list1))
print(mean(list2))


#Calculate Standard Deviation
from math import sqrt
list3 = [1, 2, 3, 4]
def std_dev(numbers):
    if len(numbers) > 1:
        avg = mean(numbers)
        var = sum((i - avg)**2 for i in numbers) / (len(numbers)-1)
        std = sqrt(var)
        return std
    else:
        return float('Nan')
print(std_dev(list3))


# remove duplicate elements in a list
list4 = [1, 2, 3, 1]

def rem_dupl(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst
print(rem_dupl(list4))


#Count how many times an element in a list occurs:
list5 = [1, 3, 2, 2, 1, 1, 1, 4, 5, 6, 6, 7]
from collections import Counter
count = Counter(list5)
print(count)

#Is string palindrome? Python slicing technique.
w1 = 'ololo'
w2 = 'cafe'
def palindrome(word):
    return word == word[::-1]
print(palindrome(w1))
print(palindrome(w2))

