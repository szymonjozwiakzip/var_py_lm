# Tak piszemy komentarz jednoliniowy
'''
Tak
robimy
komentarz
blokowy
(zawiera więcej niż jedną linijkę)
'''

"""
To
również
komentarz
blokowy
nie ma więc znaczenia, czy wykorzystamy '', czy ""
"""

#Rodzaje zmiennych i jak je deklarować

liczba = 11 #int - liczba stałoprzecinkowa, inaczej całkowita
liczbaZmiennop = 5.7 #float - liczba zmiennoprzecinkowa, inaczej zawierająca część dziesiętną
napis = 'auto' # str = string - napis
wartosc = True #bool - wartość logiczna, reprezentuje prawdę (True) lub fałsz (False)

'''
 Bardzo często w innych językach (takich jak C++) musimy deklarować typ zmiennej już przy jej tworzeniu (np. int liczba =11;)
 Python tego nie wymaga, zdarza się jednak, że musimy zmieniać typ danych ręcznie, w zależności od potrzeb programu, 
 jednak na szczęście da się zrobić to w łatwy sposób
'''


'''
 Wartości logiczne typu boolean (bool)

1 - True
0 - False
'''

print(liczba) # W ten sposób wypisujemy liczby na konsoli

liczba = 'napis' # Możemy też dowolnie nadpisywać zmienną, nawet zmieniając jej docelowy typ danych

print(liczba)

test = 'test'

print('Teraz sprawdzimy typ danych przedstawiających zmienną o treści: test ', type(test)) 
#W ten sposób, korzystając z funkcji type() jesteśmy w stanie sprawdzić typ danych reprezentujący daną zmienną

test = wartosc #teraz zmieniamy wartosc zmiennej test, nadpisująć ją wartością zmiennej wartosc

print('Sprawdżmy wartość zmiennej test, nadpisując ją zmienną typu bool: ', test, type(test))
print ('\n') # W ten sposób jesteśmy w stanie wypisać enter (n to skrót od end line)
"""
RODZAJE ZAPISYWANIA ZMIENNYCH

Camel Case -> toJestNazwaZmiennej  
Pascal Case -> ToJestNazwaZmiennej - powinno używać się do nazywania klas 
Snake Case -> to_jest_nazwa_zmiennej - powinno używać się do nazywania zmiennych i funkcji
UpperCase -> TO_JEST_NAZWA_ZMIENNEJ

"""

print('RODZAJE ZAPISYWANIA ZMIENNYCH')
print('\n Camel Case -> toJestNazwaZmiennej \n Pascal Case -> ToJestNazwaZmiennej \n Snake Case -> to_jest_nazwa_zmiennej \n UpperCase -> TO_JEST_NAZWA_ZMIENNEJ')

#Warto zaznaczyć, że wszystkie nazwy zmiennych są case-sensitive, czyli to, czy nazwa zaczyna się wielką, czy małą literą, 
# czy używamy Pascal Case, czy Snake Case ma ogromne znaczenie, gdyż są to dwie różne zmienne! Niżej przykład: 

zmienna = 1
Zmienna= 2
ZMIENNA = 3

print(zmienna, Zmienna, ZMIENNA)

print('\n \t TYPY DANYCH\n') #\t to znak tabulacji, tym samym tworzymy wcięcie tego tekstu
#int
a = 10
print('int \n', a, type(a))
a=-2560
print(a, type(a), '\n')

#float
b= 125.012385
print('float \n', b, type(b))
b= -0.9991
print(b, type(b), '\n')

#bool
c = True
print('bool \n', c, type(c))
c= False
print(c, type(c), '\n')

#str
d= 'Twoj napis'
print('string \n',d, type(d))
d = 'To tez jest tekst'
print(d, type(d))
d = 'a'
print(d, type(d))
d = '23'
print(d, type(d), '\n')

print('Widzimy więc, że string może być reprezentowany różnie, nawet jako liczba, która będzie traktowana jako napis')
e = '17'
f = d + e
print('Wynik działania 23+17 w przypadku w którym mamy do czynienia z typem danych string: ', f, type(f))
g=23
h=17
i=g+h
print('Wynik działania 23+17 w przypadku w którym mamy do czynienia z typem danych int: ', i, type(i))

'''
KONWERSJA TYPOW DANYCH
 
1.float -> int           / zostaje tylko czesc calkowita liczby -> 5.7 = 5
2.bool -> int           / w przypadku prawdy zwroci 1, w przypadku falszu 0 
3.string -> int        / tylko jesli string sklada sie z cyfr 
4.int -> float        / 5 -> 5.0
5.bool -> float      / w przypadku prawdy zwroci 1.0, a w przypadku falszu 0.0
6.string -> float   / tylko wtedy, gdy cały string składa się z cyfr, kropka jest opcjonalna
7.int -> bool      / w przypadku 0 fałsz w kazdym innym mamy prawde
8.float -> bool   / w przypadku 0.0 zwraca fałsz, w każdym innym prawdę
9.string -> bool / zwraca fałsz jedynie dla pustego stringa, w każdym innym przypadku mamy prawdę
Wszystkie konwersje na string zmieniają po prostu wszystko na napis
'''

print('KONWERSJA TYPÓW DANYCH - PRZYKŁADY')

print('\n1. float -> int')
a = 3.8 
print('float:', a)
a = int(a) #używamy w tym celu funkcji int(), która oczywiście konwertuje wartość w nawiasie na typ int
print('Po konwersji: ',a, type(a))

print('\n2. bool -> int')
a = True
print('bool: ', a)
a= int(a)
print('Po konwersji: ',a, type(a))

print('\n3. string -> int')
a = '10'
print('string: ',a)
a = int(a)
print('Po konwersji: ',a, type(a))

print('\n4. int -> float')
a = 10
print('int: ', a)
a = float(a)
print('Po konwersji: ', a, type(a))

print('\n5. bool -> float')
a = False
print('bool: ', a)
a = float(a)
print('Po konwersji: ', a, type(a))

print('\n6. string -> float')
a = '7'
print('strong: ', a)
a = float(a)
print('Po konwersji: ', a, type(a))

print('\n7. int -> bool')
a = 5
print('int: ', a)
a = float(a)
print('Po konwersji: ',a, type(a))

print('\n8. float -> bool')
a= 0.0
print ('float: ', a)
a = bool(a)
print('Po konwersji: ', a, type(a))

print('\n9. string -> bool')
a= 'test'
print('string: ', a)
a = bool(a)
print('Po konwersji: ', a, type(a))