"""
typy danych
- int, integer, typ numeryczny, liczby calkowite
- w python liczby calkowite moga miec dowolna dlugosc
- python automatycznie zarzadza pamiecia aby przechowywac licby o dowolnej wielkosci, ograniczone tylko RAM w systemie
- konwersja na inne typy
"""
from Scripts.string import string

number = 8
print(number)
print(type(number))

number_float = float(number)
print(number_float)
print(type(number_float))
number_string = str(number)
print(number_string)
print(type(number_string))

float(number)      #uzycie wbudowanej funkcji konwersjii
number.__float__() #uzycie metody specjalnej

number_f = 9.5
number_int = int(number_f) #obcina liczby po przecinku
print(+number_int)

