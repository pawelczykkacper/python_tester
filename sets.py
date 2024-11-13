"""
zbiory - sets, zestawy - pojemniki do przechwyaywania danch
 - tworzone za pomoca nawiasow klamrowych {}
 - nie maja klucza, tylko same wartości
 - elmenety musza byc unialne, nie moga sie powtarzac
 - zmieniaja kolejnosc po wywolaniu
 - nie jestesmy w stanie zmienic konkretnego elementu
 - mozemy dodac tylko kolejne elementy
"""

birds = {"zimorodek", "bocian", "czapla", "orzel"}
print(birds)

data = {"zimorodek", 1, "bocian", 2.5, "czapla", 1, "orzel"} # -wysiwetla tylko pierwsza wartosc z duplikatu
print(data)

data = {"zimorodek", True, "bocian", 2.5, "czapla", 1, "orzel"} # -True i 1 to duplikat, False i 0 tez duplikat
print(data)

import random
data = {1, 2, 3, 4, 5}
data2 = {3, 4, 5, 6}
print(data)

#dodawanie elementow do istniejacego zbioru add()
data.add(6)
print(data)

#usuwanie elementu remove()
data.remove(5) # usuwany element musi istniec w zbiorze
print(data)

data.discard(99) # usuwany element nie musi istniec
print(data)

#random.sample() wybieramy losowy element
random_element = random.sample(sorted(data), 1)[0]
print(random_element)

chosen_element = random.choice(sorted(data))
print(chosen_element)



#czesc wspolna
common_part = data & data2
print(common_part)

#róznica
div_part = data - data2
print(div_part)

#symetryczna róznica
sym_div_part = data ^ data2
print(sym_div_part)

#stworzenie zbioru z listy usunie duplikaty
list1 = [1, 2, 2, 2, 3, 4, 4, 5]
print(list1)
set1 = set(list1)
print(set1)

#łączenie zbiorów
set2 = {3, 3, 4, 4, 5, 6, 6, 7, 8}
set3 = set1 | set2
print(set3)


