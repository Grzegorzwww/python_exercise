#!/usr/bin/python3


def main():
    moja_funkcja()
    print("------------------------------------------------")
    przedstaw("Grzegorz", "W", 30)

    print("3^2 = "+str(rekurencja_potega(3, 2)))


    temp_2 = moja_lista()
    print( temp_2[0])



def moja_funkcja():
    print("moja_funkcja")


def przedstaw(imie, nazwisko, wiek):
    print("Nazywam sie " + imie + " "+ nazwisko +" i mam lat : " + str(wiek))


def rekurencja_potega(x, y):
    if y == 0 :
        return 1
    if y >= 1 :
       x = (x * rekurencja_potega(x, y - 1))
       return x



def moja_lista() :
    temp = []
    temp.append("1. Kot")
    temp.append("2. Pies")
    temp.append("3.Mysza")

    return temp


main()
quit()