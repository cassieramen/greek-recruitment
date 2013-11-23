from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function
import csv

setup_environ(settings)

from pnm.models import PNM

def preparePNMS():
	data = open('members.txt', 'rb')
	reader = csv.reader(data)
	currentMembers = []
	for row in reader:
		name = row[0].split()
		currentMembers.append(name[0]+name[1])

	'''Get the pnms scores in the correct order'''
	pnms = PNM.objects.all()
	for pnm in pnms:
		name = pnm.lastName + pnm.firstName
		if pnm.setTwoScore == -1:
			pnm.setReleased = 1
		elif pnm.setThreeScore == -1:
			pnm.setReleased = 2
		elif pnm.setFourScore == -1:
			pnm.setReleased = 3
		elif name in currentMembers:
			pnm.setReleased = 5
		else:
			pnm.setReleased = 4
		if pnm.setOneScore == -1: #didn't show up
			pnm.setReleased = -1
		pnm.save()

preparePNMS()
