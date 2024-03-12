from enum import Enum


class pippo:
	def run(self):
		print("My name is pippo")

class pluto:
	def run(self):
		print("My name is pluto")


class disney(Enum):
	pippo = 1
	pluto = 2


def run(t):
	mapping = { disney.pippo:pippo, disney.pluto:pluto}
	obj = mapping[t]()
	obj.run()

ac = "pippo"

run(disney.pluto)

	
