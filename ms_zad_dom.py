"""

### Zadanie 2.1 | Interakcja i proste obliczenia (ok. 2 godz.)
Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
"""

"""
cena_ziemniakow = int(input('podaj cene ziemniakow za kg: '))
ile_ziemniakow = int(input('podaj ile ziemniakow chcesz zakupic w kg: '))

cena_bananow = int(input('podaj cene bananow za kg: '))
ile_bananow = int(input('podaj ile bananow chcesz zakupic w kg: '))

koszt_z = cena_ziemniakow * ile_ziemniakow

koszt_b = cena_bananow * ile_bananow

koszt_calkowity = koszt_b + koszt_z

#print(f' {ile_ziemniakow} kg ziemniakow po {cena_ziemniakow} zl bedzie kosztowac {koszt_z} zl')

#print(f' {ile_bananow} kg ziemniakow po {cena_bananow} zl bedzie kosztowac {koszt_b} zl')




print(f'za te zakupy bedziesz musial zaplacic {koszt_calkowity} zlotych.')

if koszt_z > koszt_b:
    print(f'wieksza czesc tej kwoty stanowi koszt ziemniakow')
elif koszt_b > koszt_z:
    print(f'wieksza czesc tej kwoty stanowi koszt bananow')
elif koszt_z == koszt_b:
    print(f'kwoty za banany i ziemniaki sa rowne')







"""




"""

### Zadanie 2.2 | Buty do szewca (ok. 1 godz.)
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, 
wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.

Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej, możesz założyć, 
że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

"""
"""



print()

print("podajesz dzien tygodnia, kiedy oddales buty do szewca (gdzie poniedziałek to dzień 1,")
print("wtorek to dzień 2 itd) oraz dlugosc naprawy (maksymalnie tydzien tj 7 dni) ")
print()

oddanie = input('podaj dzien tygodnia, od 1 do 7:  ')    # pobranie dnia tygodnia

oddanie = int(oddanie)                                   # zmiana typu danych wejsciowych na integer

naprawa = input('podaj ile dni trwa naprawa: ')          # pobranie dlugosci naprawy

naprawa = int(naprawa)                                   # zmiana typu danych wejsciowych na integer

if oddanie > 0 and oddanie < 8:                          # sprawdzenie poprawnosci wprowadzanych dni

    if naprawa > 0 and naprawa < 8:                      # sprawdzenie poprawnosci wprowadzanych dni

        if naprawa + oddanie > 7:                        # gdy termin oddania wypada w nastepnym tygodniu 
            print(f'buty beda gotowe do zwrotu {naprawa + oddanie - 7}. dnia nastepnego tygodnia')

        else:                                            # gdy termin oddania wypada w tym samym tygodniu
            print(f'buty beda gotowe do zwrotu {naprawa + oddanie}. dnia tego samego tygodnia')

    else:
        print('wprowadzono niepoprawna ilosc dni naprawy')
        exit()

else:
    print('wprowadzono niepoprawny dzien tygodnia')
    exit()


"""

"""

### Zadanie 2.3 | Współczynnik BMI (ok. 2 godz.)
Napisz trzy programy, które dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypiszą współczynnik BMI, 
oraz podsumowanie informujące o stanie/zaleceniach. 
(Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie). 
Programy mają różnić się sposobem interakcji z użytkownikiem.

"""

# ver 1

"""

print()
print('Celem obliczenia wskaznika BMI podaj swoj wzrost w cm oraz wage ciala w kg')
print()
waga = int(input('podaj wage w kg: '))
wzrost = int(input('podaj wzrost w cm: '))


if waga < 10 or waga > 500 or wzrost < 50 or wzrost > 250:              # ograniczenia na dane wejsciowe
    print('cos nie tak z podanymi danymi')
    exit()

bmi = float( (waga) / ((wzrost / 100) **2)   )                                  # wyliczenie bmi

if bmi < 16:
    print(f'twoj wskaznik BMI jest bardzo niski: {bmi} - wskazuje wyglodzenie, '
    'musisz natychmiast udac sie do lekarza po pomoc')
elif bmi >= 16 and bmi < 17:
    print(f'jako ze twoj wskaznik BMI jest niski: {bmi} - wksazuje wychudzenie, '
    'powinienes skonsultowac sie z lekarzem')
elif bmi >= 17 and bmi < 18.5:
    print(f'jako ze twoj wskaznik BMI jest dosc niski: {bmi} - wskazuje niedowage, '
    'sugeruje udac sie na konsultacje z lekarzem lub dietetykiem aby dopracowac twoja diete')
elif bmi >= 18.5 and bmi < 25:
    print(f'mr perfect :) optymanle BMI: {bmi} ')
elif bmi >= 25 and bmi < 30:
    print(f'twoje BMI {bmi} wskazuje nadwage - moze czas odpuscic te slodycze i zaczac sie wiecej ruszac? :) ')
elif bmi >= 30 and bmi < 35:
    print(f'uzyskany wynik BMI jest dosc wysoki: {bmi} - wskazuje otylosc I stopnia. '
    'wskazana jest konsultacja z lekarzem lub dietetykiem')
elif bmi >=35 and bmi < 40:
    print(f'twoj wskaznik BMI jest wysoki: {bmi} - wskazuje otylosc II stopnia. '
    'udaj sie na konsultacje z lekarzem')
else:
    print(f'twoj wskaznik BMI jest bardzo wysoki: {bmi} - wskazuje otylosc III stopnia. musisz natychmiast udac sie '
          f'do lekarza po pomoc')

"""

## ver 2 i 3 - jakie sa inne mozliwe interakcje?

"""
### Zadanie 2.4 | Opłata hotelowa (ok 1,5 godz.)
Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu,
a program wylicza, ile trzeba zapłacić. Zasady są takie:
- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
    - 200 zł za noc, jeśli nocują jedną noc
    - 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
    - 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki, 
czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.

"""
"""
print()
print('Kalkulator kosztow w Hotelu **** PROGRAMATOR.')
print()
print('Prosimy o podanie wieku i dlugosci pobytu.')
print()

wiek = int(input('Ile masz lat?: '))
dl_pobytu = int(input('Ile dni spedzisz w hotelu?: '))

stawka = 0

if wiek == 0 or wiek > 150 or dl_pobytu == 0 :                      # sprawdzenie danych wejsciowych
    print('Wprowadziles niepoprawne dane!!!')
    exit()

if wiek < 18:                                                        # stawki dla dzieci
    stawka = 100
else:                                                                # stawki doroslych
    if dl_pobytu == 1:
        stawka = 200
    elif dl_pobytu < 5:
        stawka = 180
    elif dl_pobytu >= 5:
        stawka = 150

if wiek >= 65:                                                       # 10% rabatu dla emerytow
    stawka = int(stawka * 0.9)

print()
print(f'Koszt twojego pobytu wyniesie {stawka * dl_pobytu} zlotych.')

"""

"""
### Zadanie 2.5 | Pole trójkąta (ok. 1 godz.)
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta 
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
```
import math
x = math.sqrt(10)
```

"""
"""

import math

print('Podaj 3 dowolne liczby.')
a = int(input('podaj 1. liczbe: '))
b = int(input('podaj 2. liczbe: '))
c = int(input('podaj 3. liczbe: '))

lista_trzech = [a,b,c]
lista_trzech.sort()

# sprawdzam efekt powyzszej linijki :)
#print(f'{lista_trzech}')
#print(f'{lista_trzech[0]}')
#print(f'{lista_trzech[1]}')
#print(f'{lista_trzech[2]}')


p = (lista_trzech[0] + lista_trzech[1] + lista_trzech[2])/2         # polowa obwodu trojkata


if lista_trzech[0] + lista_trzech[1] <= lista_trzech[2]:
    print('podane liczby nie moglyby byc dlugosciami bokow trojkata')
else:
    print(f'podane liczby moglyby byc dlugosciami bokow trojkata o polu powierzchni '
    f'rownym {math.sqrt( (p * (p - lista_trzech[0]) * (p - lista_trzech[1]) * (p - lista_trzech[2])) ):10.10}')

"""



"""
### Zadanie 2.6 | Bilety (ok. 1 godz.)
Założenia:
    - 0-6   - wiek przedszkolny - cena biletu: 0
    - 7-17  - wiek szkolny      - cena biletu: 2.80
    - 18-64 - wiek dorosły      - cena biletu: 3.80
    - +65   - wiek emerytalny   - cena biletu: 1.90
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. 
Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.

"""

"""

print()
print('Kalkulator kosztow w MPK Krakow.')
print()
print('Prosimy o podanie wieku oraz ilosci biletow.')
print()

wiek = int(input('Ile masz lat?: '))
ilosc_biletow = int(input('Ile chcesz zakupic biletow?: '))

cena_biletu = 0

if  wiek > 150 or ilosc_biletow == 0 :
    print('Wprowadziles niepoprawne dane!!!')
    exit()

if wiek < 7:
    print('masz darmowe przejazdy')
    exit()

elif wiek < 18:
    cena_biletu = 2.8

elif wiek < 65:
    cena_biletu = 3.8

else:
    cena_biletu = 1.9

print()
print(f'Koszt {ilosc_biletow} biletow wyniesie {cena_biletu * ilosc_biletow} zlotych.')

"""



"""
### Zadanie 2.7 | Liczenie can (ok. 0,5 godz.)
Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena. 
Wyświetl odpowiedni komunikat.
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł

"""


"""
przedmiot = input('co chcesz kupic?: ')
stawka = int(input('podaj cene towaru: '))
ilosc = int(input('podaj ilosc towaru: '))




print(f'za {przedmiot} ktory/ktore chcesz kupic, musisz zaplacic {stawka*ilosc} zl')
"""


"""
### Zadanie 2.8 | Kalkulator lat psich (ok. 0,5 godz.)
Zakładamy, że 1 ludzki rok, to 5 lat psich.
Za pomocą konsoli wczytaj imię i wiek psa.
Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
Przykład:
Podaj imię psa - Burek
Podaj wiek psa - 3
Gdyby Burek był człowiekiem, miałby 15 lat.


"""
"""
print()
print('witamy w kalkulatorze psich lat :)')
print()

imie = input('jak ma na imie pies?: ')
wiek = int(input(f'ile {imie} ma lat?: '))

print(f'Gdyby {imie} byl czlowiekiem, mialby {wiek*5} lat')
"""



"""

### Zadanie 2.1 | Zagadka matematyczna 

Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). 
Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej). 
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. 
Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
"""

"""
import random

a = random.randint(1,99)
b = random.randint(1,99)

while True:
    input_suma = int(input(f'Podaj sume liczb {a} i {b}: '))
    if input_suma == a + b:
        print('poprawny wynik')
        exit(0)

    print('zle, sprobuj ponownie...')
    print()

"""

"""
### Zadanie 2.2 | Choinka

Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje 
w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:

   *
 * * *
* * * * *

"""

"""

x = int(input('podaj liczbe naturalna: '))

if x <=0:
    print('liczby naturalne to 1,2,3,... itd!!! ')
    exit(0)

for i in range(x+1):                        #jam jest mistrz choinek :)
    print(f' '*(x-i), end='')
    print(f'*'*(2*i-1))

"""





