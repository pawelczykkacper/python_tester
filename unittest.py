"""
Unittest - framework do tstowania w Pythonie, głównie do testowania jednostkowego
pozwala na pisanie i uruchamianie testów automatycznych w celu sprawdzanie poprawnosci kodu
komponenty unittest:
 - klasa testowa, dzidziczy po unittest.TestCase i zawiera metody testowe
 - metoda testowa - każda metoda w klasie tetsowej, zaczyna sie od słowa test..., jest traktowana jako test
 - asercje - metoda, która srawdza czy wynik jest zgodny z oczekiwaniami, assertTrue
  - uruchomienie testu - możemy to zrobić za pomoca unittest.main(), ktory automatycznie znajduje wszystkie
   metody zaczynajace sie od test... i je uruchamia
"""
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()



