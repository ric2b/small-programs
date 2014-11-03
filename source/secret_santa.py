import sys
import pprint
import random
import os

user_input = raw_input("Please input the names with a space in between >> ").split(" ")

n_people = len(user_input)
if n_people < 2:
	print "You gift yourself, go make some friends"
	exit()
names = dict(zip(range(n_people), user_input))

raffle = {}
for key in names:
	valid = False
	while valid == False:
		attempt = random.randint(0,n_people-1)
		valid = True 
		if names[attempt] in raffle.values() or attempt == key:
			valid = False
				
	raffle[names[key]] = names[attempt]		
			
#print raffle

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	query = raw_input("Who are you? >> ")	
	try:
		print "You're " + raffle[query] + "'s secret santa! :D"
		raw_input("\nPress Enter and allow the next person to query")
	except: 
		print "This name wasn't entered into the raffle, try again"
		raw_input("(Press Enter)")
	

