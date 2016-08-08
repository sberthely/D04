# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_word(s, i):
	new_string = ''
	for letter in s:
		new_string = new_string + chr(ord(letter) + i)
	return new_string

#ord #converts a character to a numeric code ('a' - ord = 97 and there are 32 letters alphabet)

#chr #which converts numeric codes to characters.

def main():
	s = input('Write a phrase: ')
	i = int(input('Set the rotation: '))
	print(rotate_word(s, i))

if __name__ == '__main__':
    main()