import csv
with open('pnms.csv', 'rb') as f:
    reader = csv.reader(f)
    items = []
    for row in reader:
    	items.append(row)
    f.close()
with open('psfbscores.csv', 'rb') as p:
	otherReader = csv.reader(p)
	matchItems = []
	for newRow in otherReader:
	   	matchItems.append(newRow)

	foundScore = False
	for row in items:
		foundScore = False
		for newRow in matchItems:
			if newRow[3] == row[1] and newRow[4] == row[0]:
				foundScore = True
				print newRow[25] #24 for preselect, 35 for facebook
		if not foundScore:
			print "-1"