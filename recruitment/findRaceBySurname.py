from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function
import csv
import string

setup_environ(settings)

from pnm.models import PNM

def preparePNMS():
	data = open('surnameBreakdown/black.txt', 'rb')
	reader = csv.reader(data)
	blackSurnames = []
	for row in reader:
		name = ''.join(e for e in row if e.isalnum())
		blackSurnames.append(name)

	data = open('surnameBreakdown/asian-pacislander.txt', 'rb')
	reader = csv.reader(data)
	asianSurnames = []
	for row in reader:
		name = ''.join(e for e in row if e.isalnum())
		asianSurnames.append(name)

	data = open('surnameBreakdown/latino.txt', 'rb')
	reader = csv.reader(data)
	latinoSurnames = []
	for row in reader:
		name = ''.join(e for e in row if e.isalnum())
		latinoSurnames.append(name)

	data = open('surnameBreakdown/white.txt', 'rb')
	reader = csv.reader(data)
	whiteSurnames = []
	for row in reader:
		name = ''.join(e for e in row if e.isalnum())
		whiteSurnames.append(name)

	'''Get the pnms scores in the correct order'''
	pnms = PNM.objects.all()
	for pnm in pnms:
		lastName = string.upper(str(pnm.lastName))
		if lastName in asianSurnames:
			pnm.race = 'Asian/Pacific Islander'
		elif lastName in latinoSurnames:
			pnm.race = 'Latino'
		elif lastName in blackSurnames:
			pnm.race = 'White'
		elif lastName in whiteSurnames:
			pnm.race = 'White'
		else:
			pnm.race = 'Unknown'
			print pnm.lastName + str(pnm.id)
		pnm.save()

preparePNMS()
