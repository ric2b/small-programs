import sys
import time

def check_args():
	""" checks if a file was supplied to the script """
	if len(sys.argv) != 2 and len(sys.argv) != 3:
		print "Usage: python " + sys.argv[0] + " <message_file> (mandatory) [settings_file] (optional)\n"
		exit()
	if len(sys.argv) == 2:
		return sys.argv[1], None
	else:
		return sys.argv[1], sys, argv[2]

def transcodeMessage(filename):
	
	try:
		f = open(filename, 'r')
	except IOError:
		print "Failed to open '" + filename + "'."
		exit()
	
	while True:
		character = f.read(1)
		time.sleep (0.2)
		if character == '':
			break
		print character 

	f.close()	# close the file
	return None


messageFile, settingsFile = check_args()
#setup()
message = transcodeMessage(messageFile)