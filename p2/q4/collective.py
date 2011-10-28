from subprocess import *
import pdb

def main():
	classifier= "temp/weight.1"
	originalData = "citeseer/citeseer.nber.tr"
	table = "citeseer/citeseer.vert.tr"
	result = "temp/pred.1.te"

	prediction = predict( classifier, data, table, result )

	trainingFile = "citeseer/citeseer.nber.tr"
	trainedWeightsFile = "temp/weight.1"
	#train( trainingFile, trainedWeightsFile )

	#generateExampleFile( "citeseer/citeseer.vert", "citeseer/citeseer.edge", "citeseer/citeseer.nber", "citeseer/pred1", "temp/example" )
	return

def stackTrain( layerNum ):
	dataFileHead = "citeseer.nber.tr"
	weightFileHead = "citeseer.w"
	predictionFileHead = "citeseer.pred"
	exampleFileHead = "citeseer.ex"
	
	vertTable = "temp/citeseer.vert.tr"
	edgeTable = "temp/citeseer.edge.tr"
	
	dataFile = dataFileHead + "." + str( layerNum - 1 ) # name of an example file from the previous layer
	weightFile = weightFileHead + "." + str( layerNum ) # name of a weight file to train
	
	predictionFileOut = predictionFileHead + "." + str( layerNum )
	
	# read a dataFile from the previous layer
	# call train and make a weight file ( classifier ) for this layer
	# spit out a prediction
	# generate example files used for upper layer
	return

def stackTest( layerNum ):
	dataFileHead = "citeseer.nber.tr"
	weightFileHead = "citeseer.w"
	predictionFileHead = "citeseer.pred"
	exampleFileHead = "citeseer.ex"
	
	vertTable = "temp/citeseer.vert.te"
	edgeTable = "temp/citeseer.edge.te"
	pass

def generateExampleFile( vertTableIn, edgeTableIn, originalExampleFile, predictionFileIn, newExampleFile ):
	""" generates feature file with previous layer's predictions """
	# make a prediction table
	fPredIn = open( predictionFileIn, "r" )
	predTable = {}
	for line in fPredIn:
		v = line.strip().split()[0]
		p = line.strip().split()[1]
		predTable[ v ] = p
	fPredIn.close()

	# prepare examples
	fiEdge = open( edgeTableIn, "r" )
	fiFeature = open( originalExampleFile, "r" )
	foExample = open( newExampleFile, "w" )

	edge_list = fiEdge.read().strip().split("\n")
	feature_list = fiFeature.read().strip().split("\n")
	
	for feature, edge in zip( feature_list, edge_list ):
		line_to_write = feature + " "
		targets = edge.split()[1:]
		for t in targets:
			line_to_write += t + "_" + prediction2Feature( predTable[ t ] ) + " "
		line_to_write += "\n"
		foExample.write( line_to_write )

	fiEdge.close()
	fiFeature.close()
	foExample.close()
	
	return
	
def prediction2Feature( pred ):
	"""
	Agents	0
	AI		1
	DB		2
	IR		3
	ML		4
	HCI		5
	"""
	ret = ""
	if pred=="0":
		ret += "Agents"
	elif pred=="1":
		ret += "AI"
	elif pred=="2":
		ret += "DB"
	elif pred=="3":
		ret += "IR"
	elif pred=="4":
		ret += "ML"
	elif pred=="5":
		ret += "HCI"
	else:
		ret += "Other"

	ret += " 1.0"
	return ret

def train( trainingFileIn, weightsFileOut ):
	""" trains by megam """
	command = [ "./megam.opt", "multiclass", "-fvals", trainingFileIn ]
	process = Popen( command, shell=False, stdout=PIPE, stderr=PIPE )
	weights = process.communicate()[0]
	
	fo = open( weightsFileOut, "w" )
	fo.write( weights )
	fo.close()
	return

def predict( weightVectFileIn, exampleFileIn, vertTableIn, predResultOut ):
	""" predicts using megam """
	# prepare a table
	ft = open( vertTableIn, "r" )
	vtable_list = ft.read().strip().split("\n")
	
	#command = "./megam.opt -predict weights.nber multiclass citeseer/citeseer.nber".split()
	command = [ "./megam.opt", "-predict", weightVectFileIn, "multiclass", exampleFileIn ]
	process = Popen( command, shell=False, stdout=PIPE, stderr=PIPE )
	predictions = process.communicate()[0]
	predictions_list = predictions.strip().split("\n")	

	# go over table and predictions and put it into a dict
	resultFile = open( predResultOut, "w" )
	for table, pred in zip( vtable_list, predictions_list):
		#pdb.set_trace()
		v = table.split()[1]
		p = pred.split()[0]
		resultFile.write( v + " " + str( p ) + "\n" )

	resultFile.close()
	return

if __name__=="__main__":
	main()