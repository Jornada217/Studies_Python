from collections import Counter

list = ['Joao LD', 'Joao NY', 'Joao MG', 'Pedro LD', 'Pedro NY', 'Paulo NY',
        'Otavio RJ', 'Peter LD', 'Luis C MG', 'Pai MG', 'Mae - Dirce MG', 'Luis Andre MG', 'Olbi NY']

def cities(lst):
    cnt = []
    for i in lst:
        city = i[-2:]
        cnt.append(city)
    return cnt

c = cities(list)

n_cities = Counter(c)
print(n_cities)

#Most recurring cities:
sorted_n_cities = sorted(n_cities, reverse=True, key=n_cities.get)[:3]
print(sorted_n_cities)

