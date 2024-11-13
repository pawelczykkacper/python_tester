"""
Słownik to pojemnik do przechowywania danych
- kazdy element słownika składa sie z klucza i wartości
- do klucza przypisana jest jedna wartość
- klucze musza byc unikalne
- wartosci moga sie powtarzać
- wartosci po kluczy dwukropkiem:
- klucze rozdzielamy  pzrecinkiem ,
- elementy slownika podajemy w {}
"""
auto = {
    "marka"         : "BMW",
    "kolor"         : "czerwony",
    "pojemnosc"     : "2400",
    "rocznik"       : "2024",
    "rodzaj_paliwa" : "benzyna",
    "przebieg"      : "1000"
}
print(auto)

#duplikat klucza tylko nadpisuje nowa wartosc
auto = {
    "marka"         : "BMW",
    "kolor"         : "czerwony",
    "pojemnosc"     : "2400",
    "rocznik"       : "2024",
    "rodzaj_paliwa" : "benzyna",
    "przebieg"      : "1000",
    "rocznik"       : "2023"
}
print(auto)

#dodajemy element
auto["liczba_miejsc"] = 5
print(auto)
print(auto.keys())
print(auto["marka"])

student = {
    "imie"      : "Jan",
    "wiek"      : 20,
    "kierunek"  : "informatyka"
}

new_key = "nazwisko"
new_value = "Kowalski"
list_from_dictonary = list(student.items())
list_from_dictonary.insert(1,(new_key, new_value))
student = dict(list_from_dictonary)
print(student)

#get(), pop(), popitem()
auto = {
    "brand" : "Volvo",
    "color" : "black",
    "engine" : ("B3 MHEV", "B4 MHEV", "B5 MHEV", "T6 PHEV", "T8 PHEV")
}

print(auto["brand"])
print(auto.get("brand"))
print(auto["engine"] [2])
print(auto)
auto.pop("color")
print(auto)
auto.popitem()
print(auto)
auto["engine"].pop(0)
print(auto)


