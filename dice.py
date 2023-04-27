import random

dice1 = 0
dice2 = 0

while True:
	answer = input("Would you like to throw the dice? Y for 'yes', N for 'no': ")
	if answer == "y" or answer == "Y":
		dice1 = random.randrange(1, 7, 1)
		dice2 = random.randrange(1, 7, 1)
		print("You rolled ", dice1, "*"*dice1, " and ", dice2, 
"*"*dice2)
	if answer == "n" or answer == "N":
		print("Thank you! See you some other time.")		
		break
