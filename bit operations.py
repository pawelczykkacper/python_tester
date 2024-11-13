"""
Operator AND &
sprawdz parzystosc liczby 10 wykorzystujac
operator AND i instrukcje warunkawa if
"""
"""
a & 1 zwraca 0 dla liczb parzystych ponieważ ostatni bit wynosi 0

       
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
       ^
       |
bit parzystosci

10 = 1010
1  = 0001
&    0000 == 0

11 = 1011
1  = 0001
&    0001 != 0        

"""
a = 10
if (a & 1) == 0:
    print(a, " jest parzyste")
else:
    print(a, " jest nieparzyste")


