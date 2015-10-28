import sys
import pprint
import random
import os


class SecretSanta:

    def __init__(self):
        user_input = input("Please input the names with a space in between >> ").split(" ")

        # Get number of names and check if there are at least 2
        n_people = len(user_input)
        if n_people < 2:
            print("You gift yourself, go make some friends")
            exit()

        # Make sure there are no repeated names
        names = dict(zip(range(n_people), user_input))
        if len(names) != len(set(names.values())):
            print("You entered the same name(s) more than once, try again")
            exit()
        self._names = names
        self._n_people = n_people
        self._raffle_table = {}

    # For each person generate a random match that has not been used and is not the person itself
    def raffle(self):
        for key in self._names:  # for each person...
            while True:
                attempt = random.randint(0, self._n_people-1)  # try to find another person who hasn't been assigned
                if self._names[attempt] not in self._raffle_table.values() and attempt != key:
                    break  # verified that the person isn't yet assigned to someone else

            self._raffle_table[self._names[key]] = self._names[attempt]

    def show_results(self):  # Show each person their match
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            query = input("Who are you? >> ")
            try:
                print("You're " + self._raffle_table[query] + "'s secret santa! :D")
                input("\nPress Enter and allow the next person to query")
            except LookupError:
                print("This name wasn't entered into the raffle, try again")
                input("(Press Enter)")

# run a secret santa :)
SS = SecretSanta()
SS.raffle()
SS.show_results()
