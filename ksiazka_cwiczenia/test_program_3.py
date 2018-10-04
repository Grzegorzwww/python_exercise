#!/usr/bin/python3

class Worker:
	def __init__(self, name, pay) :
		self.name = name
		self.pay = pay
	def lastName(self) :
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)


def main():




	bob = Worker('Rober Zielony', 50000)
	anna = Worker('Anna Czerwona', 60000)
	print(bob.lastName())
	print(anna.lastName())
	anna.giveRaise(.10)
	print(anna.pay)









main();
quit();

