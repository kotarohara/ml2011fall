#!/usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import *
from pylab import *
import dt, datasets, runClassifier

def main():
	h = dt.DT({'maxDepth': 5})
	h.train( datasets.TennisData.X, datasets.TennisData.Y )
	print h
	print
	
	runClassifier.trainTestSet(dt.DT({'maxDepth': 1}), datasets.TennisData)
	runClassifier.trainTestSet(dt.DT({'maxDepth': 2}), datasets.TennisData)
	runClassifier.trainTestSet(dt.DT({'maxDepth': 3}), datasets.TennisData)
	runClassifier.trainTestSet(dt.DT({'maxDepth': 5}), datasets.TennisData)	
	print
	
	runClassifier.trainTestSet(dt.DT({'maxDepth': 1}), datasets.CFTookCG)
	runClassifier.trainTestSet(dt.DT({'maxDepth': 3}), datasets.CFTookCG)
	runClassifier.trainTestSet(dt.DT({'maxDepth': 5}), datasets.CFTookCG)
	print 
	
	curve = runClassifier.learningCurveSet(dt.DT({'maxDepth': 5}), datasets.CFTookAI)
	runClassifier.plotCurve('DT on AI', curve)
	return
	
if __name__=="__main__":
	main()