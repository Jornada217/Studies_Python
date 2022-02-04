
array1 = '1 2 3 4 5 6 7 8 9'
array2 = '22 50'

def parse_input(array):
    lst = list(map(int, array.rstrip().split()))
    print(lst)
    print(type(lst))
    return lst

parse_input(array1)
print()
parse_input(array2)


