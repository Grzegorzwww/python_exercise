#!/usr/bin/python3

class MojaKlasa:
    zmienna = "blah"
    def funkcja(self):
        print("To jest wiadomosc wewnatrz klasy.")

    def moja_data(self):
            print("zmienna = " + self.zmienna)

def main():
    mojobiekt = MojaKlasa()
    mojobiekt.funkcja()
    mojobiekt.zmienna = "kot"
    print( mojobiekt.zmienna)
   # mojobiekt.print_data()
