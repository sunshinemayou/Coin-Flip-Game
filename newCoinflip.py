#! /usr/bin/env python

import random
import specialInput

print("This is a Coin guessing game, I will keep tract of your score!")

# I choose heads to be 0, tails to be 1
n = 0
while True:
	guess = raw_input("Please predict heads or tails: ")
	answer = random.choice(["heads", "tails"])
	if answer == guess:
		n = n+1
		print("It is: " + answer + " \n Your score is : " + str(n))
	else:
		print("I am sorry, it is : " + answer + " Game over.")
		break

print("Your score is : " + str(n))
f = open("test.txt", "r+")
fileRecords = int(f.read())
if fileRecords <= n:
	f.seek(0)
	f.write(str(n))
	print("Your highest score is : " + str(n))
elif fileRecords > n:
	print("Your highest score is : " + str(fileRecords))