
#!/usr/bin/python
import sys
import types


imie = "Grzesiek"
nazwisko = "warchol"

print( "Witaj, %s %s!" % (imie, nazwisko))


data_urodzenia = [17,9,1988]
print ("Data urodzenia: %s" % data_urodzenia)


dane = ("Jan Kowalski", 5, 10)

print ("%s mieszka w bloku nr %d w mieszkaniu %d" % dane)


napis = "Hello World 11"
print ("Hello World 11 - dlugosc = "+str(len(napis)))


napis = "Hello World p1"
print (napis.index("H")) #0
print (napis.index("d")) #10

print (napis[0])



print (napis[6:11] )

print (napis[6:len(napis)])

napis = "abcdef"
print (napis[-1])    # f
print (napis[-4:-2]) # cd
print (napis[-4:] )  # cdef
print (napis[:-2] )  # abcd

napis = "witaj"
print (napis.upper())

napis = "Ala ma kota."
tablica_slow = napis.split(" ")
print (tablica_slow) # ['Ala', 'ma', 'kota']