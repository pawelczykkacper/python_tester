"""
operatory
- arytmetyczne +, -, *, /, % (modulo - reszta z dzielenia), **
- porownania ==, !=, <, >, <=, >=
- logiczne and, or, not
- bitowe & (AND), | (OR), ~(NOT), <<, >>
"""
import math

x=20
y=10

#arytmetyczne
print(x+y) #dodawanie
print(x-y) #odejmowanie
print(x*y) #mnozenie
print(x/y) #wynikiem bedzie typ float
print(x%y) #modulo reszta  zdzielenia
print(x**y) #potegowanie
print(math.sqrt(x)) #pierwistkowanie

#porownania
print(x==y) #rowne
print(x!=y) #rozne

#logiczne
print(x>3 and x<10)
print(x>3 or x<10)
print(not(x>3))

#bitowe
a = 6
b = 3
print(a & b) #0110 and 0011 = 0010 -> 2
print(a | b) #0110 or 0011 = 0111 -> 7
print(~b)    #not 0110 = -1100 -> -4
print(a ^ b) #0110 xor 0011 =0101 -> 5



#print(0110 & 0011)



#operator trojargumentowy
#luty = rok_przesetpny ? 29 : 28
rok_przestepony = True
luty = 29 if rok_przestepony else 28
print(luty)


a,b,c,name, age = 1,2,"G","Agnieszka", 18
