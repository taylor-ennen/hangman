import random
import hangman_art
import hangman_words

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
display = ""
x = -1
solved = False
for char in chosen_word:
	display += "_"
print(display)
lives = 6

while not solved:
	print(hangman_art.stages[lives])
	if lives == 0:
		print("You lost though. Why did you do this though?")
		solved = True
	if lives !=0:
		guess = input("Guess a letter: ").lower()
		x = -1
		correct = False
	for letter in chosen_word:
		x += 1 #x start at negative one allowing us each loop to add one this causes the index to start at 0 on the first loop since counting on the loop is independent of whether the guess is correct
		if guess == letter:     #when the users guessed letter equals the letter being checked
			display = list(display)		#TURN displayed found characters into list for manipulation of characaters
			display[x] = guess
			display = ''.join(display)
			correct = True
	print(display)
	if correct != True:
		lives -= 1
	if "_" not in display:
		solved = True
		print("You did it, Hooray!")
