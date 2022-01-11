#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

def check_guess():
	return chosen_word.count(guess)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
display = ""
x = -1
solved = False
for char in chosen_word:
	display += "_"
print(display)

while not solved:
	guess = input("Guess a letter: ").lower()
	x = -1

	for letter in chosen_word:
		x += 1 #x start at negative one allowing us each loop to add one this causes the index to start at 0 on the first loop since counting on the loop is independent of whether the guess is correct
		if guess == letter:     #when the users guessed letter equals the letter being checked
			display = list(display)		#TURN displayed found characters into list for manipulation of characaters
			display[x] = guess
			display = ''.join(display)
	print(display)
	if "_" not in display:
		solved = True
		print("You did it, Hooray!")
