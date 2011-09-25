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
	
	#curve = runClassifier.learningCurveSet(dt.DT({'maxDepth': 5}), datasets.CFTookAI)
	#runClassifier.plotCurve('DT on AI', curve)
	
	#curve = runClassifier.hyperparamCurveSet(dt.DT({'maxDepth': 5}), 'maxDepth', [1,2,3,4,5,6,7,8,9,10], datasets.CFTookAI)
	#runClassifier.plotCurve( 'DT on AI (hyperparameter)', curve )
	
	print "WU4:"
	h = dt.DT({'maxDepth': 3})
	h.train( datasets.CFTookCG.X, datasets.CFTookCG.Y )
	print h

	print "0", datasets.CFDataRatings.courseNames[6], datasets.CFDataRatings.courseIds[6]
	print "1-left", datasets.CFDataRatings.courseNames[34], datasets.CFDataRatings.courseIds[34]
	print "1-left-2-left", datasets.CFDataRatings.courseNames[48], datasets.CFDataRatings.courseIds[48]
	print "1-left-2-right", datasets.CFDataRatings.courseNames[27], datasets.CFDataRatings.courseIds[27]
	print "1-right", datasets.CFDataRatings.courseNames[54], datasets.CFDataRatings.courseIds[54]
	print "1-right-2-left", datasets.CFDataRatings.courseNames[32], datasets.CFDataRatings.courseIds[32]
	print "1-right-2-left", datasets.CFDataRatings.courseNames[53], datasets.CFDataRatings.courseIds[53]

	return
	
if __name__=="__main__":
	main()