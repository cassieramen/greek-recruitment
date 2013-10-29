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
			if row[2] == 'S' or row[2] == 's':
				year = 2
			#a -1 indicates the information doesn't exist
			pnm = PNM(firstName=row[0],
							lastName = row[1],
							year = year,
							facebookScore = row[3] if row[3] else -1,
							preselectScore = row[4] if row[4] else -1,
							setOneScore = row[5] if row[5] else -1,
							setTwoScore = row[6] if row[6] else -1,
							setThreeScore = row[7] if row[7] else -1,
							setFourScore = row[8] if row[8] else -1,
							setReleased = row[9] if row[9] else -1,
							)
			pnm.save()
		data.close()
		print 'Successfully added the data'

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Get the filepath')
	parser.add_argument('filePath', type=str, help = 'csv filepath')

	arg = parser.parse_args()
	importCSV(arg.filePath)