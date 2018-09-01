"""
(c) Ramzi Al Haddad 2002-2018

Crack the Code Game

Game Layout

- Choose a random number from 0 to 9 for each of the 3 combination numbers of the lock

- Choose numbers that are not from the chosen 'key' numbers that will be used for the hint boxes

- There are 5 text hints with numbers that correspond to them and they are as listed
	- One number is correct and well placed
	- One number is correct but wrong placed
	- Two numbers are correct but wrong placed
	- Nothing is correct
	- One number is correct but wrong placed

"""

import random # For our random numnber generation
from os import system # To clear the console
from time import sleep

def main(magic):

	def keyNumberGeneration(): # Lets start with our key number generation
		key = []

		while True:
			if len(key) == 3:
				break
			else:
				randomNumber = random.randint(0,9)

				if randomNumber not in key:
					key.append(randomNumber)

		return key

	def invalidNumbers(key, length):
		invalidNumbers = []

		while True:
			if len(invalidNumbers) == 3:
				break
			else:
				randomNumber = random.randint(0,9)

				if randomNumber not in key and randomNumber not in invalidNumbers:
					invalidNumbers.append(randomNumber)

		return invalidNumbers

	def gameGeneration():

		key = keyNumberGeneration()
		invalidNumber = invalidNumbers(key, 3)
		attempt = []

		while attempt != key:
			system("cls")

			print([key[0]], [invalidNumber[2]], [invalidNumber[0]], "One number is correct and well placed")
			print([invalidNumber[1]], [invalidNumber[0]], [invalidNumber[2]], "Nothing is correct")
			print([invalidNumber[0]], [key[0]], [invalidNumber[2]], "One number is correct but wrong placed")
			print([key[1]], [key[2]], [invalidNumber[0]], "Two numbers are correct but wrong placed")
			print([invalidNumber[1]], [invalidNumber[2]], [key[0]], "One number is correct but wrong placed")
			print("\n")
			
			attemptRaw = str(input())

			attempt = [int(attemptRaw[0]), int(attemptRaw[1]), int(attemptRaw[2])]
			

	gameGeneration()	


magic = "Computer Magic!"
main(magic)