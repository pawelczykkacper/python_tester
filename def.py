"""
Funkcje tworzymy aby nie powtarzac wielokrotnie podobnej do siebie instrukcji
def nazwa_funckji(parametr):
    cialo funkcji

Funkcja posiada paremntry - czyli nazwa zmiennej, ktora przechowuje przeslany argument.
"""

def wiadomosc_powitalna(imie):
    print("Cześć", imie, "miło mi powitać cię w moim programie")

#wywołanie funkcji dla waksanazych imion
wiadomosc_powitalna("Inga")
wiadomosc_powitalna("Monika")
wiadomosc_powitalna("Marek")


"""
Za pomoca funkcji policzy pole prostokąta, przy uzyciu print()
"""
def pole_prostokata(a, b):
    print("Pole prostokata wynosi:",a * b)

pole_prostokata(5,4)
"""
aby stworzyc wiecej niz jeden parametr wystarczy miedzy argumentami dac przecinek (,)
aby wywołać funkcję piszemy nazwę funkcji, nastepnie w nawiasach w tej samej kolejności w jakiej mamy
okreslone parametry, przesyłamy wartości argumenty, w naszym przypdaku najbipierw "a" potem "b"
"""

"""
Funkcja z wieloma parametrami
Stwórz funkcję, która będzie obliczać pole powierzchni trapezu
P=1/2*(a+b)*h
"""

def pole_trapezu(a, b, h):
    print("Pole trapezu o podstawach 3 i 5 oraz wysokości 4 wynosi:", (a+b)/2*h)

pole_trapezu(3,5,4)

"""
Funkcja z listą jako argument
Wyswietlicz elementy listy przy uzyciu funkcji, lista owoce = [jablko, banan, wiśnia]
"""
def wypisz_elementy(lista):
    print("elementy listy:")
    for element in lista:
        print(element)

owoce = ["jablko", "banan", "wiśnia"]

wypisz_elementy(owoce)

"""
Funkcja z petlą for i wypisanie wyników

Wypisz kwadraty liczby n
"""

def wypisz_kwadraty(n):
    for i in range(1,n+1):
        print("kwadrat liczby", i, "wynosi:", i**2)

wypisz_kwadraty(5)

"""
Funkcja z instrukcja warunkowa if
sprawdz parzystość
przyjmujemy specjalny przypadek dla liczby 0, wyswietlajacy komunikat:
"0 nie jest traktowane jako liczba parzysta ani nieparzysta"
"""

def czy_parzyste(liczba):
    if liczba == 0:
        print("0 nie jest traktowane jako liczba parzysta ani nieparzysta")
    elif liczba % 2 == 0:
        print("liczba", liczba, "jest parzysta")
    else:
        print("liczba", liczba, "nie jest parzysta")

czy_parzyste(12)
czy_parzyste(-3)
czy_parzyste(0)


"""
Znaczenie wartości "return"
W jednym z przykładów gdzie tworzylismy funkcje gdzie tworzylismy
funkcje oblioczajaca pole prostokąta napisaliśmy:

def pole_prostokata(a, b):
    print(a * b)

print(a * b) - wartośc ta została wypisana, nie powinismy korzystac z funkcji print() wewnątrz funkcji,
jeżeli coś obliczamy, ponieważ nie jestesmy użyć, wykorzystać tego wyniku ponownie, aby tą wartość
wykorzystać uzyjemy instrukcji "return"

instrukcja "return" służy do powrócenia nam do miejsca wywołania funkcji i zwrócenia zawartości
po prawej stronie tej instrukcji

def pole_prostokata(a, b):
    return a * b

print(5 * pole_prostokata(4, 5)

return - zwraca, czyli powraca do miejsca wywołania w tym przypadku do pole_prostokata(4, 5)
i zwraca a * b, czyli print(5 * 20)

Jeżeli chcemy zapistac wynik funkcji i wykorzystac w późniejszym momencie możemy stworzyc zmienna
która ten wynik przechowa

def pole_prostokata(a, b):
    return a * b

pole_prostokata_A = pole_prostokata(4, 5)
print(5 * pole_prostokata_A)

"""

def pole_prostokata(a, b):
    return a * b

pole_prostokata_A = pole_prostokata(4, 5)
print(5 * pole_prostokata_A)



"""
Przy uzyciu funkcji/instrukcji return obliczyć powierzchnie figur:
prostokąt, kwadrat, trójkąt, trapez, koło
"""

import math

def pole_prosotkata(a, b):
    return a * b

def pole_kwadratu(a):
    return a * a

def pole_trojkata(a, h):
    return (a * h) / 2

def pole_trapezu(a, b, h):
    return (a +b ) * h / 2

def pole_kola(r):
    return  math.pi * r**2

print("Pole prostokata o bokach 3 i 6 wynosi:", pole_prosotkata(3, 6))
print("Pole kwadratu o bokach 4 wynosi:", pole_kwadratu(4))
print("Pole trójkąta o podstawie 2 i wysokości 3 wynosi:", pole_trojkata(2, 3))
print("Pole trapezu o podstawach 4 i 8 i wysokości 10 wynosi:", pole_trapezu(4, 8, 10))
print("Pole koła o promieniu 10 wynosi:", pole_kola(10))

"""
napisz funkcję która przyjmuje 2 argumenty: liczba całkowita a i liczba całkowita b
funkcja powinna zwrócic sumę tych dwóch liczba z odpowiednim komunikatem
wykorzystaj return
"""

def suma_liczb(a, b):
    return a + b

wynik = suma_liczb(5,6)
print("suma liczb 5 i 6 wynosi:",wynik)

"""
napisz funkcję która przyjmuje 2 argumenty: a i b (całkowite)
funkcja powinna zwrócic wiekszą z tych liczb
"""

def wieksza_liczba(a,b):
    return max(a,b)

wynik = wieksza_liczba(5, 8)
print("Większa liczba to:",wynik)


"""
*args - to składnia pozwalajaca przekazać dowolna liczbe argumentow do funkcji
przy użyciu *args można przesyłać do funkcji wiele argumentów bez konieczności
określania ich ilości z góry
*args to tzw "argument pozycyjny", który przechowuje wszystkie przekazane
dodatkowe argumenty jako krotka (tuple)
"""

def suma(*args):
    wynik = 0
    for liczba in args:
        wynik += liczba
    return wynik

print(suma(1,2,3))
print(suma(4,5,6,7))
print(suma(10))

"""
w powyższym przykładzie funkcja suma() przyjmuje dowolną liczbę argumentów dzięki *args
argumenty są traktowane jako krotka wewnątrz funckji i można wykonywac na nich różne operacja 
np. sumowanie elemetów
"""
"""
kolejny przykład wykorzystania *args może być użyte do przekazania wielu
argumentów do funkcji aby je wydrukowała

"""

def wypisz_imiona(*args):
    for imie in args:
        print("cześć",imie)

wypisz_imiona("Ania", "Bartek", "Celina")

"""
*args - przekazwyanie różnych typów danych

"""

"""
*args - przekazwyanie różnych typów danych

"""

def wypisz_dane(*args):
    for dana in args:
        print("argument:", dana, "typ:", type(dana))
    return args

wypisz_dane(5, "heloł", 3.14, [1,2,3], True)
print(type(wypisz_dane()))

"""
**kwargs - umożliwiaprzekazanie dowolnej liczby argumentów nazwanych
(w formie klucz:wartość) do funkcji
dzięki **kwargs mozna w elastyczny sposób przekazywać różne parametry
bez konieczności okreslenia ich liczby
**kwargs zbiera wszytskie nazwane argumenty w postaci słownika (dict), w którym
klucze to nazwy argumentów, a wartości to przypisane im dane
"""

def informacja_o_osobie(**kwargs):
    for klucz, wartosc in kwargs.items():
        print(klucz, ":", wartosc)
        #print(f"{klucz}:{wartosc}")
informacja_o_osobie(imie="Kasia", wiek=25, miasto="Warszawa")
"""
w powyższym przykładzie items() to metoda, która zwaraca pary klucz:wartosc
ze słownika kwargs w formie krotki
każda para składa sie z klucza (imie, wiek, miasto) i odpowiadajacych 
im wartości ("Kasia", 25, "Warszawa")
metoda items() (umozliwia iteracje po słowniku dzięki czemu możemy łatwo 
przetwarzać klucze i wartości
"""
"""
domyślna wartość w **kwargs
możemy ustawić wartości domyslne dla argumentów w **kwargs w przypadku gdy nie zostaną przekazane
"""
def przedstaw_sie(**kwargs):
    imie = kwargs.get("imie", "Nieznajomy")
    wiek = kwargs.get("wiek", "Nieznany")
    print("imie:", imie)
    print("wiek:", wiek)

przedstaw_sie(imie="Anna", wiek=30)
przedstaw_sie(imie="Jan")
"""
używamy metody .get() na słowniku aby pobrać wartości z kwargs 
jeżeli klucz ne istnieje można ustawić wartośc domyślną, np. "Nieznany"
"""





