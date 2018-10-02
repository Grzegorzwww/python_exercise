

#!/usr/bin/python
import sys
import types

wielewitaj = "witaj" * 10

print(wielewitaj)

print ([1,2,3] * 3)


x_tab = [i for i in range(10)]
y_tab = [i for i in range(10, 20)]

print(x_tab)
print(y_tab)


duza_tablica = x_tab + y_tab
print(duza_tablica)


print ("dwa do kwadratu = "+str( 2**2))

a = 0b00111100
b = 0b00001101

#print(a&b)
print (" a = "+("{0:b}".format(a)))
print (" b = "+("{0:b}".format(b)))

print (" a & b = "+"{0:b}".format(a&b))


print (" a | b = "+"{0:b}".format(a | b))

#print(a^b )
print (" a ^ b = "+"{0:b}".format(a ^ b))

#print(~a )
print (" ~a = "+"{0:b}".format(~a))


