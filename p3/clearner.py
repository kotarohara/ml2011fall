def change4SpacesToTab( filename ):
	fi = open( filename, "r" )
	contents = fi.read()
	contents = contents.replace("    ", "\t")
	fi.close()
	fo = open( filename, "w" )
	fo.write( contents )
	fo.close()

	return

if __name__=="__main__":
	change4SpacesToTab( "dr.py" )