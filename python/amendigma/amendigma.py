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
			f = open(settingsFile, 'rU') # converts all newlines to \n
 		except IOError:
			print "(E) Failed to open the settings file '" + settingsFile + "'."
			exit()

		lines = f.readlines()
		if len(lines) > 6:
			print "(W) The settings file has more than 4 filenames, remaining ones will be discarded"

		plugboardFile 	= lines[0].rstrip()
		rotor1File 		= lines[1].rstrip()
		rotor2File 		= lines[2].rstrip()
		rotor3File 		= lines[3].rstrip()
		rotorPositions	= lines[4].rstrip()
		destinationFile = lines[5].rstrip()

	plugboard 	= getPlugboard(plugboardFile)
	rotor1 		= getRotor(rotor1File)
	rotor2 		= getRotor(rotor2File) 
	rotor3 		= getRotor(rotor3File)  
	
	return plugboard, rotor1, rotor2, rotor3, rotorPositions, destinationFile


def readMessage(messageFilename):
	
	try:
		f = open(messageFilename, 'rU')
	except IOError:
		print "(E) Failed to open '" + messageFilename + "'."
		exit()
	
	message = f.read()

	f.close()	# close the file
	return message


def getPlugboard(plugboardFile):
	plugboard = {}

	try:
		f = open(plugboardFile, 'rU')
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

		if i == 18:
			break

	f.close()
	return plugboard


def getRotor(rotorFile):
	rotor = []

	try:
		f = open(rotorFile, 'rU')
	except IOError:
		print "(E) Failed to open '" + rotorFile + "'."
		exit()

	lines = f.readlines()
	if len(lines) != 36:
		print "(E) rotor file '" + rotorFile + "' does not have exactly 36 lines, can't be used." 
		exit()
	
	for i in range(0, 36):
		rotor.append(lines[i][0])

	f.close()
	return rotor


def travelPlugboard(character, plugboard):
	
	try:
		transcoded = plugboard[character.lower()]
	except KeyError:
		transcoded = character

	if character.istitle():
		return transcoded.upper()
	
	else:
		return transcoded


def travelRotor(character, rotor, rotorPosition = 0):
	
	if ord(character.lower()) in range(ord('a'), ord('z')+1):
		index = ord(character.lower()) - ord('a') + 10
	elif ord(character) in range(ord('0'), ord('9')+1):
		index = ord(character) - ord('0')
	else:
		index = None

	if index == None:
		transcoded = character
	else:
		transcoded = rotor[index + rotorPosition]

	if character.istitle():
		return transcoded.upper()
	else:
		return transcoded

def turnRotors(rotorPosition1, rotorPosition2, rotorPosition3):
	
	return rotorPosition1, rotorPosition2, rotorPosition3


def transcodeMessage(message, plugboard, rotor1, rotor2, rotor3, rotorPositions):
	transcodedMessage = []
	intermediate = []	

	for i in range(0, len(message)):
		intermediate += travelRotor(message[i], rotor1)

	for i in range(0, len(message)):
		transcodedMessage += travelPlugboard(intermediate[i], plugboard)

	return ''.join(transcodedMessage)
	return ''.join(intermediate)


messageFile, settingsFile = check_args()
plugboard, rotor1, rotor2, rotor3, rotorPositions, destinationFile = Setup(settingsFile)
message = readMessage(messageFile)
transcodedMessage = transcodeMessage(message, plugboard, rotor1, rotor2, rotor3, rotorPositions)

try: 
	f = open(destinationFile, 'w')
	f.write(transcodedMessage)
	f.close()
except IOError:
	print "(E) Unable to write the output file."

print '\n' + transcodedMessage