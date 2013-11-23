from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function

setup_environ(settings)

from pnm.models import PNM
import csv

''' We want the baseline for each set. 
	Set One: We accepted 
'''

def computeBaseline():
	pnms = PNM.objects.all()
	setTwoPnms = getPnmsForSet(1,pnms)

	setOneAccuracy,setOneCuts = getSetAccuracy(pnms, setTwoPnms)

	setThreePnms = getPnmsForSet(2,setTwoPnms)
	setTwoAccuracy, setTwoCuts = getSetAccuracy(setTwoPnms, setThreePnms)

	setFourPnms = getPnmsForSet(3,setThreePnms)
	setThreeAccuracy, setThreeCuts = getSetAccuracy(setThreePnms, setFourPnms)

	b = open('baseline.csv', 'w')
	a = csv.writer(b)
	data = [setOneCuts,\
	        setTwoCuts,\
	        setThreeCuts]
	a.writerows(data)
	b.close()

def getPnmsForSet(set, pnms):
	'''this function will return a list of pnms that made it to that set'''
	nextSetPnms = []
	for pnm in pnms:
		if pnm.setReleased>set:
			nextSetPnms.append(pnm)
	return nextSetPnms

def getSetAccuracy(pnmsInSet, pnmsInNextSet):
	sortedPnms = sorted(pnmsInSet,key=lambda x: x.setOneScore, reverse=True)
	#Calculate the accuracy of the set
	cutoff = len(pnmsInNextSet)
	#we know how many got to the next set so let's just pick that many based on their score
	correct = 0
	cutOffPnms = []
	for i in range(0,cutoff):
		cutOffPnms.append(sortedPnms[i])
		if sortedPnms[i] in pnmsInNextSet:
			correct = correct + 1
	return float(correct)/float(cutoff), cutOffPnms


computeBaseline()