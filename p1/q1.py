#!/usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import *
from pylab import *
import dumbClassifiers
import datasets
import runClassifier

def main():
	#predictOne = dumbClassifiers.AlwaysPredictOne({})
	#h.train(datasets.TennisData.X, datasets.TennisData.Y)
	#h.predictAll(datasets.TennisData.X)
	#print "Training Accuracy: ", mean((datasets.TennisData.Y > 0) == (h.predictAll(datasets.TennisData.X) > 0) )
	#print "Test Accuracy: ", mean((datasets.TennisData.Yte > 0) == (h.predictAll(datasets.TennisData.Xte) > 0) )
	#runClassifier.trainTestSet(h, datasets.TennisData)
	#predictFrequent = dumbClassifiers.AlwaysPredictMostFrequent({})
	#predictOne = dumbClassifiers.AlwaysPredictOne({})
	#predictFrequent = dumbClassifiers.AlwaysPredictMostFrequent({})
	#runClassifier.trainTestSet(predictOne, datasets.CFTookAI)
	#runClassifier.trainTestSet(predictFrequent, datasets.CFTookAI)
	runClassifier.trainTestSet(dumbClassifiers.FirstFeatureClassifier({}), datasets.TennisData)
	runClassifier.trainTestSet(dumbClassifiers.FirstFeatureClassifier({}), datasets.CFTookAI)
	runClassifier.trainTestSet(dumbClassifiers.FirstFeatureClassifier({}), datasets.CFTookCG)
	
if __name__=="__main__":
	main()