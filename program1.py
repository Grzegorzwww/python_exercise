
#!/usr/bin/python
import sys
import types




def main():

	print"Hello World"
	zmienna = "kot i pies"
	print (zmienna)
	print(" i mysza")

	pi = 3.14
	multiply = 2
	print(pi * multiply)

	str_1 = "napisz_1"
	str_2 = "napisz_1"

	stan = (str_1 == str_2)
	print(stan)


	napis = "witaj"

	rzeczywista = 10

	calkowita = float(20.0)

	if isinstance(napis, str) :
		print(napis)

	if isinstance(rzeczywista, int) :
		print(rzeczywista)

	if isinstance(calkowita, float) :
		print(calkowita)




main()
quit()