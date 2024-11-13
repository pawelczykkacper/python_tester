"""
typy danych
- typ tekstowy/lancuch znakow - str string, czyli tekst podawany w czudzyslowie
- operacje na lancuchach - konkatenacja, laczenie za pomoca operatora +
- typ znakowy - char, znak podawany w apastrofach
- indeksowanie w nawiasach kwadratowych []
A  G  N  I  E  S  Z  K  A
0  1  2  3  4  5  6  7  8
              ...-3 -2 -1
- zakresy od i do n [i:n+1]
"""

name = "Agnieszka"
number = 1
name2 = 'Aga'
sentence = "I'm from Polnad"
sentence2 = ('I\'m from Polnad')
sentence3 = """I'am from 
Poland"""


string =  "tekst"
str = "tekst"
int = 1

surname = "Kowalska"
age = 18

#konkatenacja
person = name + " " + surname
print(person)

#wypisanie
print(name,surname)

#powielanie
print((name +" ") * 10)

#tuple
tuple = name,surname,age
print(type(tuple))

#indeksowanie
print(name[1])  # G - zaczynamy od 0
print(name[8])  # ostatnie a
print(name[-1]) # ostatnie a - liczone od tylu to ujemne wartosci

#zakres - slicing
print(name[0:4]) # Agi - od 0 do n znaku to [0:n+1]
print(name[:4])  # Agi - od samego poczatku, nie trzeba podawac indeksu
print(name[5:9]) # szka - od 5 do 8 to [5:9]
print(name[5:])  # szka - od 5 do konca to [5:]

#male i duze litery
print(name.lower())
print(name.upper())
print(name[0].lower())
print(name,surname)
print(name.join(surname))
lower_name= name.lower()

