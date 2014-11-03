import sys
import pprint
import random

user_input = raw_input("Please input the names with a space in between >> ").split(" ")

n_people = len(user_input)
names = zip(range(n_people), user_input)

print names

raffle = []

for key, name in names:
	raffle.append((name, random.randint(0,n_people-1))) 
	
print raffle

gifts_to = []

for gifter_name, giftee_key in raffle:
	gifts_to.append((gifter_name, names[giftee_key][1]))
	
print gifts_to
