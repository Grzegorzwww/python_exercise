
#!/usr/bin/python


imie = "Robert"
lista_imion = ["Jan", "Robert"]

print("---- WYRAZENIA ----")

if imie in lista_imion:
    print ("Nazywasz sie Jan lub Robert")

    x = 2
    if x == 2:
        print ("x wynosi dwa!")
    else:
        print ("x jest rozne od dwoch.")



x = [1,2,3]
y = [1,2,3]
print (x == y) # Wypisze True
print( x is y) # Wypisze False

tablica = [1, 2, 3]
tablica2 = ['a', 'b', tablica]
print( tablica == tablica2[2]) # True
print( tablica is tablica2[2]) # True

tablica.append(4) # Dodajemy do tablicy liczbe 4
print (tablica2[2]) # [1, 2, 3, 4]


print( not False)              # Wypisze True
print ((not False) == (False)) # Wypisze False

print("---- PETLE ----")

pierwsze = [2,3,5,7]

for pierwsza in pierwsze:
    print (pierwsza)

liczby = list(range(5))
print(liczby)

for x in liczby:
    print (x)

licznik = 0
while licznik < 5:
    print (licznik)
    licznik += 1

licznik = 0
while True:
    print(licznik)
    licznik += 1
    if licznik >= 5:
          break

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print("---- CWICZENIE ----")

liczby = list(range(237))
x = 0;
while x < len(liczby) :
    x+= 1
    if x % 2 == 0:
        continue
    else:
        print(x)






