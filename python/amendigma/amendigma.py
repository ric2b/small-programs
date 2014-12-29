import sys
import string
import time

def check_args():
	""" checks if a file was supplied to the script """
	if len(sys.argv) != 2 and len(sys.argv) != 3:
		print "(E) Usage: python " + sys.argv[0] + " <message_file> (mandatory) [settings_file] (optional)\n"
		exit()
	if len(sys.argv) == 2:
		print "(W) No settings file given, will use the defaults."
		return sys.argv[1], None
	else:
		return sys.argv[1], sys.argv[2]


def Setup(settingsFile):

	# Defaults
	plugboardFile 	= "plugboardA.txt"
	rotor1File 		= "rotorA.txt"
	rotor2File 		= "rotorB.txt"
	rotor3File 		= "rotorC.txt"

	if settingsFile != None:
		try:
			f = open(settingsFile, 'r')
		except IOError:
			print "(E) Failed to open '" + settingsFile + "'."
			exit()

		lines = f.readlines()
		if len(lines) > 4:
			print "(W) The settings file has more than 4 filenames, remaining ones will be discarded"

		plugboardFile 	= lines[0]
		rotor1File 		= lines[1]
		rotor2File 		= lines[2]
		rotor3File 		= lines[3]

	plugboard 	= getPlugboard(plugboardFile)
	rotor1 		= getRotor(rotor1File)
	rotor2 		= getRotor(rotor2File) 
	rotor3 		= getRotor(rotor3File)  
	
	return plugboard, rotor1, rotor2, rotor3


def readMessage(messageFilename):
	
	try:
		f = open(messageFilename, 'r')
	except IOError:
		print "(E) Failed to open '" + messageFilename + "'."
		exit()
	
	message = f.read()

	f.close()	# close the file
	return message


def getPlugboard(plugboardFile):
	plugboard = {}

	try:
		f = open(plugboardFile, 'r')
	except IOError:
		print "(E) Failed to open '" + plugboardFile + "', will run with unconnected plugboard."

	for digit in string.digits:
		plugboard[digit] = digit

	for character in string.lowercase:
		plugboard[character] = character

	lines = f.readlines()
	if len(lines) > 18:
		print "(W) plugboard file has more lines than expected, will discard after 18 lines. Remember, connecting x to y will also connect y to x."
	for i in range(0, len(lines)):
		x = lines[i][0]
		y = lines[i][2]
		plugboard[x] = y
		plugboard[y] = x

	return plugboard


def getRotor(rotorFile):
	pass

def travelPlugboard(character, plugboard):
	
	try:
		transcoded = plugboard[character.lower()]
	except KeyError:
		transcoded = character

	if character.istitle():
		return transcoded.upper()
	
	else:
		return transcoded


def travelRotor(character, rotor, rotorPosition):
	
	try:
		transcoded = connections[character]
	except KeyError:
		transcoded = character

	return transcoded


def transcodeMessage(message, plugboard, rotor1, rotor2, rotor3):
	transcodedMessage = []	

	for i in range(0, len(message)):
		transcodedMessage += travelPlugboard(message[i], plugboard)

	return ''.join(transcodedMessage)


messageFile, settingsFile = check_args()
plugboard, rotor1, rotor2, rotor3 = Setup(settingsFile)
message = readMessage(messageFile)
transcodedMessage = transcodeMessage(message, plugboard, rotor1, rotor2, rotor3)

print '\n' + transcodedMessage