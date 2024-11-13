""""
operacja wejscia input()
"""
#suma dwoch liczba uzytkownaika
a = float(input("Liczba a = "))
b = float(input("Kolejna liczba b = "))
c = a + b
#print("Suma " + str(a) + " i " + str(b) + " to " + str(c))
print("liczba:", c)

#parzystosc liczby uzytkownika
liczba = int(input("Liczba a = "))
wynik = "parzysta" if liczba % 2 == 0 else "nieparzysta"
print("Liczba " +str(liczba) + " jest " + wynik)
#szort werszyn
print("parzysta" if int(input("Podaj liczbe: ")) % 2 == 0 else "nieparzysta")

#kalkulator liczb
a = int(input("Liczba a = "))
b = int(input("Liczba b = "))
znak = input("operacja: ")
if znak == "+":
    print(a + b)
elif znak == "-":
    print(a - b)
elif znak=="*":
    print(a * b)
elif znak=="/":
    if b != 0:
        print(a / b)
    else:
        print("Nie dziel przez 0")
else:
    print("Zly operator")

#pogodynka
temp=float(input("temperatura: "))
if temp < 0:
    print("mroz")
elif 0 <= temp < 16:
    print("chlodno")
elif 16 <= temp < 25:
    print("przyjemnie")
elif 25 <= temp:
    print("goraco")
else:
    print("To nie jest poprawna temperatura")

#liczba dodatnia, ujemna czy zero
number = float(input("liczba: "))
if number > 0:
    print("liczba ", number, " jest dodatnia")
elif number < 0:
    print("liczba ", number, " jest ujemna")
elif number == 0:
    print("liczba ", number, " jest zerem")

