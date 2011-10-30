from subprocess import *
from logging import *
basicConfig(level=DEBUG)
import pdb

WEIGHT_ON_NEIGHBORS = "1.0"
MAXIMUM_LAYERS = 10

### Filename heads
weightFileHead = 		"temp/weight"
predictionFileHead =	"temp/pred"
exampleFileHead = 		"temp/example"

def main():
	crossValidate( 5 )
	return

def crossValidate( splitNum ):
	fn_nber = "citeseer/citeseer.nber"
	fn_edge = "citeseer/citeseer.edge"
	fn_vert = "citeseer/citeseer.vert"
	
	fi_nber = open( fn_nber, "r" )
	fi_edge = open( fn_edge, "r" )
	fi_vert = open( fn_vert, "r" )
	
	lineCount = len( fi_nber.read().split("\n") )
	numExPiece = lineCount / splitNum
	
	for idx in range( splitNum ):
		print "--- CROSS VALIDATION: ", idx+1
		fi_nber.seek( 0 ) # go to the beginning of the file
		fi_edge.seek( 0 )
		fi_vert.seek( 0 )
		
		nberList = fi_nber.read().split("\n")
		edgeList = fi_edge.read().split("\n")
		vertList = fi_vert.read().split("\n")
		
		nberTrList = nberList[0:idx*numExPiece] + nberList[(idx+1)*numExPiece:]
		nberTeList = nberList[idx*numExPiece:(idx+1)*numExPiece]
		
		edgeTrList = edgeList[0:idx*numExPiece] + edgeList[(idx+1)*numExPiece:]
		edgeTeList = edgeList[idx*numExPiece:(idx+1)*numExPiece]
		
		vertTrList = vertList[0:idx*numExPiece] + vertList[(idx+1)*numExPiece:]
		vertTeList = vertList[idx*numExPiece:(idx+1)*numExPiece]
		
		# write files to do cross validation
		exTrWriter = open( "temp/example.tr.1", "w" )
		exTeWriter = open( "temp/example.te.1", "w" )
		edgeTrWriter = open( "temp/edge.tr", "w" )
		edgeTeWriter = open( "temp/edge.te", "w" )
		vertTrWriter = open( "temp/vert.tr", "w" )
		vertTeWriter = open( "temp/vert.te", "w" )
		
		for line in nberTrList:
			exTrWriter.write( line + "\n" )
		for line in nberTeList:
			exTeWriter.write( line + "\n" )
		for line in edgeTrList:
			edgeTrWriter.write( line + "\n" )
		for line in edgeTeList:
			edgeTeWriter.write( line + "\n" )
		for line in vertTrList:
			vertTrWriter.write( line + "\n" )
		for line in vertTeList:
			vertTeWriter.write( line + "\n" )
		
		exTrWriter.close()
		exTeWriter.close()
		edgeTrWriter.close()
		edgeTeWriter.close()
		vertTrWriter.close()
		vertTeWriter.close()
		
		# do cross validation using files generated
		k = 1
		K = MAXIMUM_LAYERS
		while k <= K:
			print "Training", k, "th layer",
			stackTrain( k )
			k += 1
		k = 1
		while k <= K:
			print "Testing", k, "th layer"
			stackTest( k )
			k += 1
		
	fi_nber.close()
	fi_edge.close()
	fi_vert.close()
	return

def stackTrain( layerNum, initExampleFile="temp/example.tr.1", vertTableFileIn="temp/vert.tr", edgeTableFileIn="temp/edge.tr" ):
	exampleFile = 		exampleFileHead + ".tr"		# temp/example.tr
	predictionFile = 	predictionFileHead + ".tr" 	# temp/pred.tr
	weightFile = 		weightFileHead
	
	# pdb.set_trace()
	### Actual learning part
	if layerNum == 1:
		### Filenames
		exampleFileIn = 	initExampleFile
		weightFileOut = 	weightFile + ".1"
		predictionFileOut = predictionFile + ".1"
		
		# train and write a classifier ( weight file )
		train( exampleFileIn, weightFileOut )
		# predict yhat that you'll use on the next layer
		predict( weightFileOut, exampleFileIn, vertTableFileIn, predictionFileOut )
	else:
		### Filenames
		# Input file
		exampleFileIn =		initExampleFile
		predictionFileIn = 	predictionFile + "." + str( layerNum - 1 ) # take a yhat file from the last layer
		prevExampleFileIn = exampleFile + "." + str( layerNum - 1 )
		# Output files
		exampleFileOut = 	exampleFile + "." + str( layerNum )
		weightFileOut = 	weightFile + "." + str( layerNum )
		predictionFileOut = predictionFile + "." + str( layerNum )
		
		# generate a training file
		generateExampleFile( vertTableFileIn, edgeTableFileIn, initExampleFile, predictionFileIn, exampleFileOut )
		prevReader = open( prevExampleFileIn, "r" )
		currReader = open( exampleFileOut, "r" )
		temp = 	prevReader.read()
		temp += currReader.read()
		prevReader.close()
		currReader.close()
		currWriter = open( exampleFileOut, "w" )
		currWriter.write( temp )
		currWriter.close()
		# use a training file that was made in previous lines.
		# train and make a classifier ( weight file )
		train( exampleFileOut, weightFileOut )
		# spit out a prediction that you'll use on the next layer
		predict( weightFileOut, exampleFileOut, vertTableFileIn, predictionFileOut )

	return

def stackTest( layerNum, initExampleFile="temp/example.te.1", vertTableIn = "temp/vert.te", edgeTableIn = "temp/edge.te" ):
	exampleFile = 		exampleFileHead + ".te"		# temp/example.te
	predictionFile = 	predictionFileHead + ".te" 	# temp/pred.te
	weightFile = 		weightFileHead
	
	#pdb.set_trace()
	### Actual learning part
	if layerNum == 1:
		weightFileIn = 		weightFile + ".1"
		exampleFileIn =		exampleFile + ".1"
		predictionFileOut = predictionFile + ".1"
		predict( weightFileIn, exampleFileIn, vertTableIn, predictionFileOut )
	else:
		# Input files
		weightFileIn = 		weightFile + "." + str( layerNum )
		predictionFileIn = 	predictionFile + "."+ str( layerNum - 1 )
		prevExampleFileIn = exampleFile + "." + str( layerNum - 1 )
		# Output files
		exampleFileOut =	exampleFile + "." + str( layerNum )
		predictionFileOut = predictionFile + "." + str( layerNum )

		# push prev layer's predictions to ex.
		generateExampleFile( vertTableIn, edgeTableIn, initExampleFile, predictionFileIn, exampleFileOut ) 
		# spit out a prediction
		predict( weightFileIn, exampleFileOut, vertTableIn, predictionFileOut )
	
	return

def generateExampleFile( vertTableIn, edgeTableIn, originalExampleFile, predictionFileIn, newExampleFile ):
	""" generates feature file with previous layer's predictions """
	# make a prediction table
	predictionReader = open( predictionFileIn, "r" )
	predictionTable = {}
	for line in predictionReader:
		v = line.strip().split()[0]
		p = line.strip().split()[1]
		predictionTable[ v ] = p
	predictionReader.close()
	
	# prepare examples
	edgeTableReader = 	open( edgeTableIn, "r" )
	exampleReader = 	open( originalExampleFile, "r" )
	edgeList = 			edgeTableReader.read().strip().split("\n")
	exampleList = 		exampleReader.read().strip().split("\n")
	edgeTableReader.close()
	exampleReader.close()
	
	# pdb.set_trace()
	exampleWriter =		open( newExampleFile, "w" )
	for example, edge in zip( exampleList, edgeList ):
		line_to_write = example + " "
		targets = edge.split()[1:]
		for t in targets:
			if t in predictionTable:
				line_to_write += prediction2Feature( t, predictionTable[ t ] ) + " "
		line_to_write = line_to_write.strip()
		line_to_write += "\n"
		
		exampleWriter.write( line_to_write )
	exampleWriter.close()
	return
	
def prediction2Feature( target, pred ):
	"""
	Agents	0
	AI		1
	DB		2
	IR		3
	ML		4
	HCI		5
	"""
	fval = {}
	fval["Agents"] = "0.0"
	fval["AI"] = "0.0"
	fval["DB"] = "0.0"
	fval["IR"] = "0.0"
	fval["ML"] = "0.0"
	fval["HCI"] = "0.0"
	
	ret = ""
	
	newval = WEIGHT_ON_NEIGHBORS
	if pred=="0":
		ret += target + "_Agents " + newval
		#fval["Agents"] = newval
	elif pred=="1":
		ret += target + "_AI " + newval
		#fval["AI"] = newval
	elif pred=="2":
		ret += target + "_DB " + newval
		#fval["DB"] = newval
	elif pred=="3":
		ret += target + "_IR " + newval
		#fval["IR"] = newval
	elif pred=="4":
		ret += target + "_ML " + newval
		#fval["ML"] = newval
	elif pred=="5":
		ret += target + "_HCI " + newval
		#fval["HCI"] = newval
	else:
		ret += target + "_Other" + newval
		#fval["Other"] = newval

	#for key in fval:
	#	ret += target + "_" + key + " " + fval[key] + " "
		
	#ret += ""
	return ret

def train( trainingFileIn, weightsFileOut ):
	""" trains by megam """
	print "Training file:", trainingFileIn
	# pdb.set_trace()
	command = [ "./megam.opt", "-fvals", "multiclass", trainingFileIn ]
	process = Popen( command, shell=False, stdout=PIPE, stderr=PIPE )
	weights = process.communicate()[0]
	
	fo = open( weightsFileOut, "w" )
	fo.write( weights )
	fo.close()
	return

def predict( weightFileIn, exampleFileIn, vertTableIn, predResultOut ):
	""" predicts using megam """
	# prepare a table
	vertTableReader = open( vertTableIn, "r" )
	vtableList = vertTableReader.read().strip().split("\n")
	vertTableReader.close()
	#command = "./megam.opt -predict weights.nber multiclass citeseer/citeseer.nber".split()
	command = [ "./megam.opt", "-predict", weightFileIn, "multiclass", exampleFileIn ]
	process = Popen( command, shell=False, stdout=PIPE, stderr=PIPE )
	
	comm = process.communicate()
	print comm[1]
	predictions = comm[0]
	predictionsList = predictions.strip().split("\n")	

	# go over table and predictions and put it into a dict
	predictionWriter = open( predResultOut, "w" )
	for vert, pred in zip( vtableList, predictionsList):
		v = vert.split()[1]
		p = pred.split()[0]
		predictionWriter.write( v + " " + str( p ) + "\n" )
	predictionWriter.close()
	return

if __name__=="__main__":
	main()