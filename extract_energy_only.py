import sys
import mmap

#read in files to extract data from
file = sys.argv[1]

#open each file
with open(file, "r") as fil:
	#memory map the file
	map = mmap.mmap(fil.fileno(), 0, prot=mmap.PROT_READ)
	
	#search for last occurence of word
	i = map.rfind(b"E(RB3LYP)")
	
	#seek to the location
	map.seek(i)
	
	# read the line
	line = map.readline()
	
	#print to cmd line
	print(f'file: {file}, Energy: {line[11:30]}')
