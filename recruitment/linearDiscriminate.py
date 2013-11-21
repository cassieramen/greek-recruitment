from __future__ import division
import random
from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function

setup_environ(settings)

'''For validation just break it into ten seperate pieces for 10 fold, how are we deciding to stop?''' 

from pnm.models import PNM

def perceptron4(initialvector, X, Y, Q, Z):
	'''PERCEPTRONA finds a linear discriminate (a line) that seperates data into
	positive and negative outcomes.

	initialvector is the parameter vector(weight vector and treshold value)

	X is the row vector for the training example

	Y is the column vector for the training example

	Z is the result vector for the training example '''

	keepLooping = True
	w = initialvector
	errorRate = 0
	while keepLooping:
		keepLooping = False #we want to stop looping when we can classify 95%
		errorRate = 0
		for i in range(0,len(X)):
			valueVector = [X[i],Y[i],Q[i],1]
			classification = dot(valueVector, w) # weight*value + threshold
			if classification>0 and Z[i]<0: #misclassified as positive
				errorRate = errorRate + 1
				w = [w[0] + X[i]*Z[i], w[1] + Y[i]*Z[i], w[2] + Q[i]*Z[i], w[3] + Q[i]*X[i]*Z[i]*Y[i]]
			elif classification<0 and Z[i]>0: #misclassified as negative
				errorRate = errorRate + 1
				w = [w[0] + X[i]*Z[i], w[1] + Y[i]*Z[i], w[2] + Q[i]*Z[i], w[3] + Q[i]*X[i]*Z[i]*Y[i]]
		if float(errorRate)/float(len(X)) > .05:
			keepLooping = True
			print float(errorRate)/float(len(X))

	print "Error rate is:" + str(float(errorRate)/float(len(X)))
	return w

def perceptron3(initialvector, X, Y, Z):
	'''PERCEPTRONA finds a linear discriminate (a line) that seperates data into
	positive and negative outcomes.

	initialvector is the parameter vector(weight vector and treshold value)

	X is the row vector for the training example

	Y is the column vector for the training example

	Z is the result vector for the training example '''

	keepLooping = True
	w = initialvector
	errorRate = 0
	oldErrorRate = 1 
	while keepLooping:
		keepLooping = False #we want to stop looping when we can classify 95%
		errorRate = 0
		for i in range(0,len(X)):
			valueVector = [X[i],Y[i],1]
			classification = dot(valueVector, w) # weight*value + threshold
			if classification>0 and Z[i]<0: #misclassified as positive
				errorRate = errorRate + 1
				w = [w[0] + X[i]*Z[i], w[1] + Y[i]*Z[i], w[2] + X[i]*Z[i]*Y[i]]
			elif classification<0 and Z[i]>0: #misclassified as negative
				errorRate = errorRate + 1
				w = [w[0] + X[i]*Z[i], w[1] + Y[i]*Z[i], w[2] + X[i]*Z[i] + Y[i]*Z[i]]
		if float(errorRate)/float(len(X)) > .05 and not float(errorRate)/float(len(X)) == oldErrorRate:
			keepLooping = True
			oldErrorRate = float(errorRate)/float(len(X))
			print float(errorRate)/float(len(X))
			print w

	print "Error rate is:" + str(float(errorRate)/float(len(X)))
	return w

def perceptron2(initialvector, X, Y):
	'''PERCEPTRONA finds a linear discriminate (a line) that seperates data into
	positive and negative outcomes.

	initialvector is the parameter vector(weight vector and treshold value)

	X is the row vector for the training example

	Y is the result vector for the training example '''

	keepLooping = True
	w = initialvector
	errorRate = 0
	while keepLooping:
		keepLooping = False #we want to stop looping when we can classify 95%
		errorRate = 0
		for i in range(0,len(X)):
			valueVector = [X[i],1]
			classification = dot(valueVector, w) # weight*value + threshold
			if classification>0 and Y[i]<0: #misclassified as positive
				errorRate = errorRate + 1
				w = [w[0] + X[i]*Y[i], w[1] + X[i]*Y[i]]
			elif classification<0 and Y[i]>0: #misclassified as negative
				errorRate = errorRate + 1
				w = [w[0] + X[i]*Y[i], w[1] + X[i]*Y[i]]
		if float(errorRate)/float(len(X)) > .05:
			keepLooping = True
			print float(errorRate)/float(len(X))

	print "Error rate is:" + str(float(errorRate)/float(len(X)))
	return w

def dot(values, weights):
#dot product helper function
	finalSum = 0
	for i in range(0,len(values)):
		finalSum += values[i]*weights[i]
	return finalSum

def preparePNMS():
	'''Get the pnms scores in the correct order'''
	pnms = PNM.objects.all()
	#trainingSet = random.sample(xrange(len(pnms)),int(len(pnms)*.6)) # use 60% of the population 
	X = []
	Y = []
	Q = []
	Z = []
	for i in range(0,len(pnms)):
		#if pnms[i].setReleased != -1 and i in trainingSet: #They went through recruitment
		if pnms[i].setReleased != -1: #They went through recruitment
			if pnms[i].facebookScore != -1 and pnms[i].preselectScore != -1: #we actually collected data about them
				X.append(pnms[i].facebookScore)
				Y.append(pnms[i].preselectScore)
				Q.append(pnms[i].setOneScore)
				if pnms[i].setReleased>1:
					Z.append(1)
				else:
					Z.append(-1)
	
	#w = perceptron2([1,1],X,Z)
	w = perceptron3([1,1,1],X,Y,Z)
	#w = perceptron4([1,1,1,1],X,Y,Q,Z)
	print w

preparePNMS()
