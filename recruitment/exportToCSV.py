from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function
import csv
import urllib2
import string

setup_environ(settings)

from pnm.models import PNM

with open('data.csv', 'wb') as csvfile:

    writer = csv.writer(csvfile, delimiter=',',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['First Name','Last Name','Year','Country','Address','City','State','Zip','High School',
    	'Major','Dorm','Facebook Score','Preselect Score','Set One Score','Set Two Score','Set Three Score',
    	'Set Four Score','Set Released', 'Income', 'Race'])

    '''Get the pnms scores in the correct order'''
    pnms = PNM.objects.all()
    for pnm in pnms:
    	writer.writerow([
    			unicode(pnm.firstName).encode("utf-8"),
    			unicode(pnm.lastName).encode("utf-8"),
    			pnm.year,
    			unicode(pnm.country).encode("utf-8"),
    			unicode(pnm.address).encode("utf-8"),
    			unicode(pnm.city).encode("utf-8"),
    			pnm.state,
				unicode(pnm.zip).encode("utf-8"),
				unicode(pnm.highSchool).encode("utf-8"),
				pnm.major,
				pnm.dorm,
				pnm.facebookScore,
				pnm.preselectScore,
				pnm.setOneScore, 
				str(pnm.setTwoScore),
				str(pnm.setThreeScore),
				str(pnm.setFourScore),
				str(pnm.setReleased),
				str(pnm.income),
				str(unicode(pnm.race).encode("utf-8"))])