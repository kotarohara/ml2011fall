def main():
	fi = open( "citeseer/citeseer.nber", "r" )
	count = {}
	count[0] = count[1] = count[2] = count[3] = count[4] = count[5] = 0
	for line in fi:
		l = line[0]
		if l == "0":
			count[0] += 1
		elif l == "1":
			count[1] += 1
		elif l == "2":
			count[2] += 1
		elif l == "3":
			count[3] += 1
		elif l == "4":
			count[4] += 1
		elif l == "5":
			count[5] += 1
	
	print count
	
	return

if __name__=="__main__":
	main()