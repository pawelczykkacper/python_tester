#kalkulator.py (dodawanie, odejmowanie, dzielenie i mnożenie+ obłsługa błedów, dzielenia przez 0
#test_kalkulator.py

def addition(a, b):
    return a + b
def substraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("Nie mozna dzielic przez 0")  #zgłaszanie wyjątków
    return a / b

#operation = input("podaj znak działania (+,-,*,/): ")
#a = float(input("podaj liczbe: "))
#b = float(input("podaj liczbe: "))
#if operation == "+":
#    print(addition(a, b))
#elif operation == "-":
#    print(substraction(a, b))
#elif operation == "*":
#    print(multiplication(a, b))
#elif operation == "/":
#    print(division(a, b))
#else:
#    raise ValueError("bledna operacja")
