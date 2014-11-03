import sys
import pprint
import random

user_input = raw_input("Please input the names with a space in between >> ").split(" ")
names = zip(range(len(user_input)), user_input)
print names

print random.randint(0,len(user_input)-1)





