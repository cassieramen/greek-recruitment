from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function

setup_environ(settings)

from pnm.models import PNM

def preparePNMS():
	'''Get the pnms scores in the correct order'''
	pnms = PNM.objects.all()
	for pnm in pnms:
		if pnm.setReleased == -1:
			if pnm.setTwoScore == -1:
				pnm.setReleased = 1
			elif pnm.setThreeScore == -1:
				pnm.setReleased = 2
			elif pnm.setFourScore == -1:
				pnm.setReleased = 3
			else:
				pnm.setReleased = 4
			if pnm.setOneScore == -1: #didn't show up
				pnm.setReleased = -1
			pnm.save()

preparePNMS()
