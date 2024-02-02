import sys
import mmap

#read in files to extract data from
file = sys.argv[1]
#list of specific phrases in log file which correspond to final energy and specific bond lengths: Pd-Cl, Pd-P, Pd-P, Pd-P(donor)
measurements = [b'E(RB3LYP)', b'R(1,3)', b'R(1,4)', b'R(1,5)', b'R(1,6)']

#cmd line formatting
print(f'{file}')

#open each file
with open(file, "r") as fil:
	#memory map the file
	map = mmap.mmap(fil.fileno(), 0, prot=mmap.PROT_READ)
	
	for m in measurements:
		#search for last occurence of measurement you want to extract
		i = map.rfind(m)
		#seek to the location
		map.seek(i)
		# read the line
		result = map.readline()
		#print to cmd line
		print(f'{result}')
	print('------------------------------------------------------------------------')


