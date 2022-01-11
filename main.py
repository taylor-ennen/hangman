import random
import hangman_art
import hangman_words
import time
import os
import intro



def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def restart():
	game()

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
def game():

		lives = 6
		chosen_word = random.choice(hangman_words.word_list)
		display = ""
		x = -1
		solved = False


		for char in chosen_word:
			display += "_"

		print(hangman_art.logo)
		time.sleep(5)
		print(display)

		while not solved:
			
			clearConsole()
			print(display)
			print(hangman_art.stages[lives])

			if lives == 0:
				clearConsole()
				print(display)
				solved = True
				input(f"You lost though. Why did you do this though? The word was {chosen_word}.\nPlay Again? Press Enter: ")
				clearConsole()
				restart()
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
				clearConsole()
				print(display)
				input("You did it, Hooray!\nPlay Again? Press Enter: ")
				solved = False
				clearConsole()
				restart()
		

restart()