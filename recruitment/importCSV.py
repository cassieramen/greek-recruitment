from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function

setup_environ(settings)

import csv
import argparse
from pnm.models import PNM

def importCSV(filePath):
#Send in the string filepath to import all the data in that csv into the PNM model
	with open(filePath, 'rb') as data:
		reader = csv.reader(data)
		items = []
		for row in reader:
			year = 1 #They are freshman
			if row[16] == 'Sophomore' or row[16] == 'sophomore':
				year = 2
			#prep zipcode
			zip = row[13][:5]
			if zip.isdigit():
				zip = int(zip)
			else:
				zip = 0
			#a -1 indicates the information doesn't exist
			pnm = PNM(	firstName=row[4],
						lastName = row[3],
						year = year,
						country = row[8],
						address = row[9],
						city = row[11],
						state= row[12],
						zip = zip,
						highSchool = row[14],
						major = row[17],
						dorm = row[19],
						facebookScore = row[24] if row[24] else -1,
						preselectScore = row[25] if row[25] else -1,
						setOneScore = row[27] if row[27] else -1,
						setTwoScore = row[28] if row[28] else -1,
						setThreeScore = row[29] if row[29] else -1,
						setFourScore = row[30] if row[30] else -1,
						setReleased = -1,
					)
			pnm.save()
		data.close()
		print 'Successfully added the data'

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Get the filepath')
	parser.add_argument('filePath', type=str, help = 'csv filepath')

	arg = parser.parse_args()
	importCSV(arg.filePath)