"""
pętla for - jest przeydatna gdy chcecmy przechodzic przez takie elementy jak lista, słowniki, zbiory
- składnia: for element in kolekcja:
- petla for wystepuje czeso w towarzystkie funkcji range()
- range() zaczyna sie domyslnie od 0 do n-1 z iteracją 1
- range(sr=tart, stop, iterator)
"""

fruits = ["jablko", "gruszka", "pomarancza", "banan"]
for fruit in fruits:
    print(fruit)

word = "Python"
for letter in word:
    print(letter)

for fruit in fruits:
    for sign in fruit:
        print(sign)

cars = ["Audi", "Vovlo", "Skoda", "Seat" ]
for car in cars:
    print(car)
    if car == "Skoda":
        break

list = [15, 60, 45, 70, 30, 90]
for element in list:
    if element <= 50:
        print(element)

for element in list:
    if element > 50:
        continue
    print(element)
#zakres 0-5
for i in range(6):
    print(i)
#
for i in range(0,6):
    print(i)

for i in range(0,6,1):
    print(i)

#parzyste od 2 do 20
for i in range(2,21,2):
    print(i)

#suma liczba od 1 do 10
summary = 0
for i in range(11):
    summary += i
print(summary)

#czy liczba 5 jest w lisci [1,3,5,7,9] i przerwie petle po znalezieniu
list = [1, 3, 5, 7, 9]
for i in list:
    if i == 5:
        print(i);
        break

#suma licz dodatnich z listy [10,-5,3,-2,7,-8]
list = [10, -5, 3, -2, 7, -8]
summary = sum(x for x in list if x > 0)
print(summary)

#tabliczka mnozenia od 1 do 5
for x in range(1, 6):
    for y in range(1, 6):
        print(x,"*",y, "=", x*y )
    print()

#tabliczka mnożenia
start = 1
end = 10
step = 1
zakres = [start + i * step for i in range(int((end - start) / step) + 1)]

for i in zakres:
    for j in zakres:
        print("{:2}".format(i*j), end=" ")
    print()




