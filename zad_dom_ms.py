### Zadanie 2.1 | Interakcja i proste obliczenia (ok. 2 godz.)
#Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
# ile kosztuje kilo ziemniaków, ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
#Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
# I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.


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
