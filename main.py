#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

def check_guess():
	return chosen_word.count(guess)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ""
guess = input("Guess a letter: ").lower()
for char in chosen_word:
		display += "_"
print(display)
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
x = -1
for letter in chosen_word:
		x += 1 #x start at negative one allowing us each loop to add one this causes the index to start at 0 on the first loop since counting on the loop is independent of whether the guess is correct
		if guess == letter:     #when the users guessed letter equals the letter being checked
			display = list(display)		#TURN displayed found characters into list for manipulation of characaters
			print(display) #TESTING CLARITY
			display[x] = guess
			display = ''.join(display)
			print(display)
		else:
			print("Wrong")
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
