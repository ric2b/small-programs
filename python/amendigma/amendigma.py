import sys
import string
import time

def check_args():
	""" checks if a file was supplied to the script """
	if len(sys.argv) != 2 and len(sys.argv) != 3:
		print "(E) Usage: python " + sys.argv[0] + " <message_file> (mandatory) [settings_file] (optional)\n"
		exit()
	if len(sys.argv) == 2:
		print "(W) No settings file given, will use the defaults. (No plugboard)"
		return sys.argv[1], None
	else:
		return sys.argv[1], sys.argv[2]


def Setup(settingsFile):

	# Defaults	
	rotorPositions	= [0,0,0]
	rotor1File 		= "rotorA.txt"
	rotor2File 		= "rotorB.txt"
	rotor3File 		= "rotorC.txt"
	plugboardFile 	= None
	destinationFile	= "encoded.txt"

	if settingsFile != None:
		try:
			f = open(settingsFile, 'rU') # converts all newlines to \n
 		except IOError:
			print "(E) Failed to open the settings file '" + settingsFile + "'."
			exit()

		lines = f.readlines()
		if len(lines) > 6:
			print "(W) The settings file has more than 6 lines, remaining ones will be discarded"

		temp = lines[0].rstrip()
		rotorPositions[0] = int(temp.split(' ')[0])
		rotorPositions[1] = int(temp.split(' ')[1])
		rotorPositions[2] = int(temp.split(' ')[2])

		rotor1File 	= lines[1].rstrip()
		rotor2File 	= lines[2].rstrip()
		rotor3File 	= lines[3].rstrip()		
		if len(lines) >= 5:
			plugboardFile 	= lines[4].rstrip()
		if len(lines) >= 6:
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

def getIndexFromChar(character):
	if ord(character) in range(ord('a'), ord('z')+1):
		index = ord(character) - ord('a') + 10
	elif ord(character) in range(ord('0'), ord('9')+1):
		index = ord(character) - ord('0')
	else:
		index = None

	return index

def getCharFromIndex(index):
	offset = 0
	if index in range(10, 36):
		offset = ord('a') - 10
	elif index in range(0, 10):	
		offset = ord('0')

	return str(unichr(index+offset))

def getPlugboard(plugboardFile):
	if plugboardFile == None:
		return None

	plugboard = {}

	try:
		f = open(plugboardFile, 'rU')
	except IOError:
		print "(E) Failed to open '" + plugboardFile + "', will run with unconnected plugboard."
		print f
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
	rotorFW = []
	rotorBW = []

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
		rotorFW.append(lines[i][0])
		rotorBW.append(0) #initialize rotorBW
	
	f.close()

	for x, y in enumerate(rotorFW):
		index = getIndexFromChar(y)

		rotorBW[index] = getCharFromIndex(x)

	return (rotorFW, rotorBW)


def travelPlugboard(character, plugboard):
	if plugboard == None:
		return character

	try:
		transcoded = plugboard[character.lower()]
	except KeyError:
		transcoded = character

	if character.istitle():
		return transcoded.upper()
	
	else:
		return transcoded


def travelRotor(character, rotor, direction, rotorPosition = 0):

	index = getIndexFromChar(character.lower())

	if index == None:
		return character
	else:
		if direction == "forward":
			transcoded = rotor[0][(index + rotorPosition)%36]
		if direction == "backwards":
			transcoded = rotor[1][(index + rotorPosition)%36]

	if character.istitle():
		return transcoded.upper()
	else:
		return transcoded


def turnRotors(rotorPositions):
	
	rotorPositions[0] += 1
	if rotorPositions[0] == 36:
		rotorPositions[0] = 0
		
		rotorPositions[1] += 1
		if rotorPositions[1] == 36:
			rotorPositions[1] = 0
			
			rotorPositions[2] += 1
			if rotorPositions[2] == 36:
				rotorPositions[2] = 0
	return rotorPositions


def travelReflector(character):
	# pair all the characters in a random way
	firstHalf	= {'a':'3', 'b':'4', 'c':'x', 'd':'v', 'e':'y', 'f':'0', 'g':'2', 'h':'w', 'i':'t', 'j':'9', 'k':'7', 'l':'z', 'm':'1', 'n':'5', 'o':'s', 'p':'8', 'q':'6', 'r':'u'} # 36/2 = 18 
	secondHalf	= {v: k for k, v in firstHalf.iteritems()}

	reflected = character

	try:
		reflected = firstHalf[character]
	except KeyError:
		pass

	try:
		reflected = secondHalf[character]
	except KeyError:
		pass
	
	return reflected	


def transcodeMessage(message, plugboard, rotor1, rotor2, rotor3, rotorPositions):
	transcodedMessage 	= []

	for i in range(0, len(message)):
		#rotorPositions = turnRotors(rotorPositions)
		# first pass
		step0 = travelPlugboard(message[i].lower(), plugboard)
		step1 = travelRotor(step0, rotor1, "forward", rotorPositions[0])
		step2 = travelRotor(step1, rotor2, "forward", rotorPositions[1])
		step3 = travelRotor(step2, rotor3, "forward", rotorPositions[2])
		# reflect and second pass
		step3 = travelReflector(step3)
		step2 = travelRotor(step3, rotor3, "backwards", rotorPositions[2])
		step1 = travelRotor(step2, rotor2, "backwards", rotorPositions[1])
		step0 = travelRotor(step1, rotor1, "backwards", rotorPositions[0])
		transcodedMessage += travelPlugboard(step0, plugboard)
		
	
	return ''.join(transcodedMessage)
#	return ''.join(intermediate1)

messageFile, settingsFile = check_args()
plugboard, rotor1, rotor2, rotor3, rotorPositions, destinationFile = Setup(settingsFile)
message = readMessage(messageFile)
transcodedMessage = transcodeMessage(message, plugboard, rotor1, rotor2, rotor3, rotorPositions)

print travelRotor('p', rotor1, "backwards", 5)
print travelRotor('5', rotor1, "forward", 5)

print '\n' + transcodedMessage

if destinationFile != None:
	try: 
		f = open(destinationFile, 'w')
		f.write(transcodedMessage)
		f.close()
	except IOError:
		print "(E) Unable to write the output file."
	exit()