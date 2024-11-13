"""
petla while - słuzy do zapetlania, czyli powtarania danych instrukcji wielokrotnie dopoki warunek bedzie prawdziwy
pętla while z continue - pomija dalsza interakcje w danej pętli
petla while break - przerywa i konczy dzialanie pętli
"""

#wypisuje liczby od 0 do 4
number = 0
while number <= 4:
    print(number)
    number += 1

#czytanie hasla z 2 probami
password = ""
counter = 0
while password != "secret" and counter <=2:
    password = input("Password: ")
    if password == "secret":
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        counter += 1
    if counter == 3:
        print("INCORRECT PASSWORD LIMIT")

#wypisuje parzyste liczby od 1 do 10
number = 1
while number <= 10:
    if number % 2 == 0:
        number+=1
        continue
    print(number)
    number += 1

#wypisuje liczby od 1 do 10 ale bez 5
number = 1
while number <= 10:
    if number == 5:
        break
    print(number)
    number += 1

#wprowadzanie liczby od uzytkownika, pisze czy jest parzysta i pyta o kolejna az do podania slowa "koniec"
input_data = ""
while input_data != "koniec":
    input_data = input("Podaj liczbe lub 'koniec' aby zakonczyć ")
    if input_data == "koniec":
        print("Koniec programu")
        break
    elif int(input_data) % 2 == 0:
        print("Liczba", input_data, "jest parzysta")
        continue

