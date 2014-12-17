import sys
ignoreFirst = 11 #the first 50 bytes of the pbm file are discarded, 11 for PhotoShop files
extensionLenght = 4

def check_args():
	""" checks if a file was supplied to the script """
	if len(sys.argv) != 2:
		print "need the filename, dumb dumb"
		exit()
	else: 
		return sys.argv[1]


filename = check_args()
filenameNoExtension = filename[0:(len(filename)-extensionLenght)]

try:
	f = open(filename, 'r')
except IOError:
	print "Failed to open '" + filename
	exit()

bytes_read = open(filename, "rb").read()
newFile = open(filenameNoExtension + ".bit", "wb")
newFile.write(bytes_read[ignoreFirst:])
newFile.close()

print filename + " was converted. (WOLOLO)"
