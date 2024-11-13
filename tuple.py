"""
typy danych
- sekwencje: list, tuple, range, słowniki

krotki (tuple) to pojmenik do przechowywania wartosci
 - zawartosc krotki nie mzoemy pozniej zmienic
 - krotki zapsujemy w (), dopuszczlany jest tez zapis bez nawiasow
 - z krotki korzystamy, gdy spodizewamy sie wartosci ktore beda niezmienne
 do konca dizalania programu
 - krotka pozwla azaosczedzic miejsce w pamieci i przyspieszyc dzialaie
 - mozna duplikowac, bo opieraja sie na indeksoaniu od 0
"""
fruits = ("cherry", 4, "raspberry", True, "strawberry", "blueberry", 3.5)
#fruits[2] = "pear" - nie mozna zmienic elementow krotki
print(fruits)
print(type(fruits))
print(fruits[0],fruits[-1])
print(len(fruits))

notes = (4, 5, 3, 5, 4)
avg = sum(notes) / len(notes)
print("średnia ocen wynosi:", avg)
print(f"średnia ocen wynosi: {avg}")
print("średnia ocen wynosi:" + str(avg))

name = input("imie: ")
surname = input("nazwisko: ")
age =  int(input("wiek: "))
city = input("miasto: ")
data = (name, surname, age, city)
print(data)
print(f"pobrane dane: imie {data[0]}, nazwisko {data[1]}, wiek {data[2]}, miasto {data[3]}")

#edycja krotki poprzez zmiane na liste
colors = ("green", "violet", "blue", "gray")
print(colors)
colors_list = list(colors)
colors_list[0] = "red"
colors = tuple(colors_list)
print(colors)

#zmien drugi element na 20
score = (5, 10, 15)
print(score)
score_list = list(score)
score_list[1] = 20
score = tuple(score_list)
print(score)

#drugi sposob - tworzymy nowa krotke ze starej
score = (5, 10, 15)
print(score)
score = (score[0], 20, score[2])
print(score)

#sprawdz czy zawiara 10 i czyz awiera 25
numbers = (5, 10, 15, 20)
print(numbers)

if 10 in numbers:
    print("10 wystepuje w krotce")
else:
    print("10 nie wystepuje w krotce")
if 25 in numbers:
    print("25 wystepuje w krotce")
if 10 in numbers:
    print("25 nie wystepuje w krotce")







