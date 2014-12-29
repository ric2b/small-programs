import sys
import string
import time

def check_args():
	""" checks if a file was supplied to the script """
	if len(sys.argv) != 2 and len(sys.argv) != 3:
		print "Usage: python " + sys.argv[0] + " <message_file> (mandatory) [settings_file] (optional)\n"
		exit()
	if len(sys.argv) == 2:
		return sys.argv[1], "default.txt"
	else:
		return sys.argv[1], sys.argv[2]

def readMessage(filename):
	
	try:
		f = open(filename, 'r')
	except IOError:
		print "Failed to open '" + filename + "'."
		exit()
	
	message = f.read()

	f.close()	# close the file
	return message

def getplugboard(plugboardFile):
	plugboard = {}

	try:
		f = open(plugboardFile, 'r')
	except IOError:
		print "Failed to open '" + plugboardFile + "'."
		print "Will run with unconnected plugboard."

	for digit in string.digits:
		plugboard[digit] = digit

#	for line in f:
#		plugboard	

	return {'a': 'b', 'b': 'c', 'c': 'd'}

def rotor1(character):
	plugboard = getplugboard("plugboardA.txt")

	try:
		transcoded = plugboard[character]
	except KeyError:
		transcoded = character

	return transcoded


def transcodeMessage(message):
	transcodedMessage = []

	for i in range(0, len(message)):
		transcodedMessage += rotor1(message[i])

	return ''.join(transcodedMessage)


messageFile, settingsFile = check_args()
message = readMessage(messageFile)
transcodedMessage = transcodeMessage(message)
print transcodedMessage