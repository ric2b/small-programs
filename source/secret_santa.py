import sys
import pprint
import random
import os

# Get the names from the user
user_input = raw_input("Please input the names with a space in between >> ").split(" ")

# Get number of names and check if there are at least 2
n_people = len(user_input)
if n_people < 2:
	print "You gift yourself, go make some friends"
	exit()

# Make sure there are no repeated names
names = dict(zip(range(n_people), user_input))
if len(names.values()) != len(set(names.values())):
	print "you entered the same name(s) more than once, try again"
	exit()

# For each person generate a random match that has not been used and is not the person itself
raffle = {}
for key in names:
	valid = False
	while valid == False:
		attempt = random.randint(0,n_people-1)
		valid = True 
		if names[attempt] in raffle.values() or attempt == key:
			valid = False
				
	raffle[names[key]] = names[attempt]		

# Show each person their match
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	query = raw_input("Who are you? >> ")	
	try:
		print "You're " + raffle[query] + "'s secret santa! :D"
		raw_input("\nPress Enter and allow the next person to query")
	except: 
		print "This name wasn't entered into the raffle, try again"
		raw_input("(Press Enter)")
