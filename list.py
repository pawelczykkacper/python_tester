"""
Lista - pojemik do przechowywania elemntów
- jest indeksowany od 0
- elementy listy podajemy w nawiasach kwadratowych []
- pozwala na duplikowanie lementów
- nazwa listy samoopisująca
"""
imiona = ["Agnieszka", "Karol", "Tomek", "Alf", "Tomek"]
print(imiona)
print(imiona[2])
#wyrażenie in, (z ang. w) mozemy sprawdzać czy dany element znajduje sie w liście
print("Karol" in imiona)
#not in - nie ma w liście
if "Agnieszka" not in imiona:
    print("Agnieszka nie wystepuje w liscie ")
else:
    print("Agnieszka wystepuje w liscie ")


"""
Lista
w liście [Marek, Ania, Jarek , Monika] sprawdzic czy imie Monika znajduje sie w liście,
a Anna nie znajduje sie w liście
"""
imiona = ["Marek", "Ania", "Jarek", "Monika"]

if "Monika" in imiona:
    print("Monika występuje w liście")
else:
    print("Monika nie występuje w liście ")
if "Anna" not in imiona:
    print("Anna nie występuje w liście ")
else:
    print("Anna występuje w liscie ")


"""
Otrzymujesz liste osób, które dostana dostęp do tajnych informacji
[Arkadiusz, Wiola, Antek] jeżeli ktos z listy imion zostanie podany
przez użytkownika wyswietli sie komiunikat "Masz dostęp", w przeciwnym "Brak dostępu"
"""
secret_list = ["Arkadiusz", "Wiola", "Antek"]
password = input("Podaj hasło: ").capitalize()
#capitalize() metoda zmiany pierwszej litery ciągu na wielką
if password in secret_list:
    print("Masz dostęp")
else:
    print("Brak dostępu")

"""
Funkcje, które pomagają operować na listach:
- len() - długość, ilość elementów w liście
- append() - dodawanie jednego elementu na końcu listy
- extend() - rozszerzenie listy o liste przesłaną jako argument
"""

lista1 = [66, 31, 5, 47, 66, 12]
lista2 = ["Arkadiusz", "Wiola", "Karol"]
print(len(lista1))
print(len(lista2))
# do lista1 dodaje 4
lista1.append(4)
print(lista1)
# do lista1 przesyłamy argumenty [2, 4, 6]
lista1.extend([2, 4, 6])
print(lista1)

"""
Funkcje, które pomagają operować na listach:
- insert() - wstawia element wewnątrz listy, na podstawie indeksu i objektu
- index() - pozwala otrzymac indeks szukanego elementy listy
* należy pamiętać że index zwraca nam tylko pierwsze wystąpienie danego elementu
"""

lista1 = [66, 31, 5, 47, 66, 12]
lista2 = ["Arkadiusz", "Wiola", "Karol"]

#wtsawiamy "Ania" pod index 1 w liście lista2
lista2.insert(1,"Ania")
print(lista2)
#szukamy 66 w lista1
print(lista1.index(66))

"""
Funkcje, które pomagają operować na listach:
- sort() - sortowanie, funkcja pozwala srotować elementy rosnąco lub malejąco, default jest rosnąco
"""

lista1 = [66, 31, 5, 47, 66, 12]
lista2 = ["Arkadiusz", "Wiola", "Karol"]

#sortowanie rosnąco (default) lista1
lista1.sort()
print(lista1)
#sortowanie rosnąco (default) lista2
lista2.sort()
print(lista2)
#sorotwanie malejąco (musze uzyć argumenty słownego słowa klucz: reverse = True
lista1.sort(reverse = True)
print(lista1)
#użycie reversed da nam ten sam efekt, ale...
x = list(reversed(sorted(lista1)))
print(x)
y = sorted(lista1)[::-1]
print(y)

"""
Funkcje, które pomagają operować na listach:
- max()/min() - maksymalna/minimalna wartość w liście
- count() - pozwala policzyć ile razy dany elemenet występuje w liście
- pop() - usuwa ostatni element z listy i wyświetlenie usunietego elmentu
- remove() - usuwanie pierwszego wystapienia elementu podanego jako parametr
"""
lista1 = [66, 31, 5, 47, 66, 12]
lista2 = ["Arkadiusz", "Wiola", "Karol"]
#max lista1
print(max(lista1))
#min lista1
print(min(lista1))
#ilośc 66 w lista1
print(lista1.count(66))
#usuniecie ostatniego elementu lista1
print(lista1.pop())
#usuwamy 66 z lista1
lista1.remove(66)
print(lista1)

"""
Funkcje, które pomagają operować na listach:
- clear() - czyszczenie listy
- reverse() - odwraca kolejnośc elementów w liście
- pop(x) - metoda pop() domyslnie usuwa ostatni element,
  ale możemy podac mu indeks elementu i wtedy usunie wskazany element np: lista.pop(0)
- del - słowo, jest tak ważne że stoi pierwszy i sam, usuwa całą listę
"""
lista1 = [66, 31, 5, 47, 66, 12]
lista2 = ["Arkadiusz", "Wiola", "Karol"]
#clear lista1
lista1.clear()
print(lista1)
lista1 = [66, 31, 5, 47, 66, 12]
#odwrotna kolejnosc lista1
lista1.reverse()
print(lista1)
#usun element o indeskie 2 z lista1
lista1.pop(2)
print(lista1)
lista1 = [66, 31, 5, 47, 66, 12]
#del lista1
del lista1
print(lista1)


#pobieramy zakres liczb od uzytkownika
start = float(input("Początek zakresu: "))
end = float(input("Koniec zakresu: "))
step = float(input("Krok: "))
zakres = [round(start + i * step, 2) for i in range(int((end - start) / step) + 1)]

for i in zakres:
    for j in zakres:
        print("{:6.2f}".format(i*j), end=" ")
    print()

#losowanie elementu
students = ["Asia","Kasia","Basia","Stasia","Jasia",]
notes = ["A", "B", "C", "D", "E", "F"]
note = random.choice(notes)
for student in students:
    note = random.choice(notes)
    print(f"{student} otrzymala ocene: {note}")









