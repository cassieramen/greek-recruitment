from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function
import csv
import urllib2
import string

setup_environ(settings)

from pnm.models import PNM

def preparePNMS():

	'''Get the pnms scores in the correct order'''
	pnms = PNM.objects.all()
	for pnm in pnms:
		if pnm.income is None:
			pnmUrl = 'http://api.census.gov/data/2011/acs5?get=B19061_001E&for=zcta:' + str(pnm.zip) + '&key=3281d5c5108b7bb83422e9d0888048f90a50ef2d'
			try:
				r = urllib2.urlopen(pnmUrl)
			except urllib2.URLError as e:
				r = e
			if r.code in (200, 401):
				data = r.read()
				info = data.split(',')[2]
				info = ''.join(e for e in info if e.isalnum())
				print info
				info = info[:-2]
				print pnm.firstName + pnm.lastName
				if info.isdigit():
					pnm.income = int(info)
					pnm.save()

preparePNMS()

