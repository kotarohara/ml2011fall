""" 
This program changes Citeseer dataset into megam (multiclass) compatible

classes:
Agents	0
AI		1
DB		2
IR		3
ML		4
HCI		5
"""


def main():
	# berNonImplicitize( "citeseer/citeseer.content", "citeseer/citeseer.nber.table", "citeseer/citeseer.vert" )
	# cleanEdges( "citeseer/citeseer.cites", "citeseer/citeseer.vert", "citeseer/citeseer.edge" )
	# joinBerEdge( "citeseer/citeseer.ber", "citeseer/citeseer.edge", "citeseer/citeseer.data" )
	return

def label2LabelVal( labelIn ):
	label = labelIn
	
	if label=="Agents":
		return 0
	elif label=="AI":
		return 1
	elif label=="DB":
		return 2
	elif label=="IR":
		return 3
	elif label=="ML":
		return 4
	elif label=="HCI":
		return 5
	else:
		return 0


# take .content files and convert it into the bernolli implicit format
# described in www.umiacs.umd.edu/~hal/megam/
# (id) (label) (feature 0/1)+
def berImplicitize( filenameIn, filenameOut ):
	fi = open( filenameIn, "r" )
	fo = open( filenameOut, "w" )
	lines_to_write = ""
	
	# for each document ( one line corresponds to one document )
	for i, line in enumerate( fi ):
		items = 	line.strip().split("\t")
		fvalues = 	items[1:-1]
		label =		items[-1]
		id =		items[0]
		
		# get a feature if it is on (1)
		print id, label
		#lines_to_write += str( label2LabelVal( label ) ) + " "
		lines_to_write += id + " " + str( label2LabelVal( label ) ) + " "
		for idx, fvalue in enumerate( fvalues ):
			fidx = "w" + str( idx )
			if fvalue == "1":
				# print fidx,
				lines_to_write += fidx + " "
		
		lines_to_write += "\n"	# end of one document
	
	print lines_to_write.strip()
	fo.write( lines_to_write )
	fi.close()
	fo.close()
	return


# make a non-implicit multiclass megam file.
# make a vertex table
def berNonImplicitize( filenameIn, filenameOut, vertTableOut ):
	fi = open( filenameIn, "r" )
	fo = open( filenameOut, "w" )
	fo_v = open( vertTableOut, "w" )
	lines_to_write = ""	
	# for each document ( one line corresponds to one document )
	for i, line in enumerate( fi ):
		items = 	line.strip().split("\t")
		fvalues = 	items[1:-1]
		label =		items[-1]
		id =		items[0]
		# get a feature if it is on (1)
		# print id, label
		# lines_to_write += str( label2LabelVal( label ) ) + " "
		lines_to_write += id + " " + str( label2LabelVal( label ) ) + " "
		for idx, fvalue in enumerate( fvalues ):
			fidx = "w" + str( idx )
			if fvalue == "1":
				# print fidx,
				lines_to_write += fidx + " 1.0 "
		fo_v.write( id + " v" + str( i ) + "\n" )
		lines_to_write += "\n"	# end of one document
	# print lines_to_write.strip()
	fo.write( lines_to_write )
	fi.close()
	fo.close()
	fo_v.close()
	return


# Read .cite files and make a cleaned version .edge
def cleanEdges( edgeFileIn, vertexTableIn, edgeFileOut ):
	# load a vertex table
	vtf = open( vertexTableIn, "r" )
	vtable = {}
	vlist = []
	for line in vtf:
		vtable[ line.split()[0] ] = line.split()[1]
		vlist.append(line.split()[1])
	vtf.close()

	efi = open( edgeFileIn, "r" )
	edges = {}
	for line in efi:
		items = 	line.strip().split("\t") # split a line into source and target
		target = 	items[0]
		source = 	items[1]
		
		if not source in edges:
			edges[ source ] = []
		edges[ source ].append( target )

	efi.close()
	
	edge_table = {}
	for key in vtable:
		if key in edges:
			clean_edge = []
			for e in edges[key]:
				if e in vtable:
					clean_edge.append( vtable[e] )
			edge_table[ vtable[key] ] = " ".join( clean_edge ) + "\n"
		else:
			edge_table[ vtable[key] ] = "\n"

	efo = open( edgeFileOut, "w" )
	for v in vlist:
		efo.write( v + " " + edge_table[v] )
	
	efo.close()
	return


def joinBerEdge( berFileIn, edgeFileIn, dataFileOut ):
	fi_ber = 	open( berFileIn, "r" )
	fi_edge = 	open( edgeFileIn, "r" )
	
	data = {}
	for line in fi_ber:
		items = line.strip().split()
		data[ items[0] ] = []
		data[ items[0] ].append( items[1:] )
	
	for line in fi_edge:
		items = line.strip().split()
		if items[0] in data:
			data[ items[0] ].append( items[1:] )
	
	fo = open( dataFileOut, "w" )
	for key in data:
		# word features
		line_to_write = key + " " + " ".join( data[key][0] ) + " "
		
		# edge features
		#if len( data[key] ) == 2:
		#	line_to_write += " 1.0 ".join( data[key][1] )
		line_to_write += "\n"
		fo.write( line_to_write )
	fo.close()
	fi_ber.close()
	fi_edge.close()
	return


if __name__=="__main__":
	main()