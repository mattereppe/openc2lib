from actions import *

# Estende con ipotetiche azioni specifiche per splf (e` solo un esempio,
# in quanto l'azione presa in considerazione e` generica - non ci sono
# azioni in piu` per splf)

@register_action
class Allow(Action):
	id=8
	name='allow'

	def run(self):
		print("Allow")


