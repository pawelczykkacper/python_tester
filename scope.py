"""
Rodzaje zasięgów w Python
zasięg zmiennych (z ang. scope) określa gdzie zmienne sa widoczne i dostępne w kodzie
zasięg wskazuje w jakich częsciach programu można odwołać sie do danej zmiennej
Python stosuje zasadę LEGB (Local, Enclosing, Global, Built-in) do ustalenia w którym
zasiegu nalezy szukać zmiennych
"""

#zasięg lokalny - dotyczy zmiennych definniowanych wewnątrz funkcji, dostepne tylko wewnątrz danej funkcji
def funckcja():
    zmienna_lokalna = 20
    print(zmienna_lokalna)

funckcja()
#print(zmienna_lokalna)

"""
Rodzaje zasięgów w Python
"""

#zasięg obejmujący (z ang. Enclosing scope) - dotyczy zmiennych zdefinniowanych w funkcji zewnętrznej
# w stosuneku do innej zagnieżdżonej funkcji

def funkcja_zewnetrzna():
    zmienna_obejmujaca = 20
    def funkcja_wewnetrzna():
        print(zmienna_obejmujaca)
    funkcja_wewnetrzna()

funkcja_zewnetrzna()


"""
Rodzaje zasięgów w Python
"""

#zasięg globalna - dotyczy zmiennych zdefuniowanych na wyższym poziemie kodu poza funkcjami
#zmienna globalne są dostepne w całym programie o ile nie są zasłonięte przez zmienna
#lokalne o tej samej nazwie

zmienna_globalna = 10

def funkcja():
    print(zmienna_globalna)

funkcja()
print(zmienna_globalna)



