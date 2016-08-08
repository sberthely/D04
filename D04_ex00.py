#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body

def random_guess():
	num_random = random.randint(1, 25)
	print(num_random)
	number_tries = 0

	while(number_tries < 5):
		number_tries += 1

		user_number = int(input('Pick a number between 1 - 25: '))
		if user_number == num_random:
			return 'YOU GOT IT'
		elif user_number < num_random:
			print('Too low')
		else:
			print('Too high')
	return 'END OF TRIES'


################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    print(random_guess())

if __name__ == '__main__':
    main()