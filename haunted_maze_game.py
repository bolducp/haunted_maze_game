
def start_game():
	print "\nWelcome to the haunted maze.\n"
	print "Enter the corn maze and choose a path.\n"
	path = raw_input("\nDo you go left or right? ")
	
	if path == "left" or path == "Left":
		jack_the_ripper()
	elif path == "right" or path == "Right":
		witch()
	else:
		game_over("\nThat's not a path.")
		
def jack_the_ripper():
	print "\nAs you walk down the path, you trip over a rock and fall into the arms of Jack the Ripper."
	print "\nJack gives you one chance to answer his riddle. If you are correct, he'll let you continue on the path."
	print "\nHere's the riddle: \nWhat is greater than God,\nmore evil than the devil,\nthe poor have it,\nthe rich need it,\nand if you eat it, you'll die?"
	guess = raw_input("\nWhat's your answer? ")
	
	if guess == "nothing" or "Nothing":
		continue_on_path()
	else:
		game_over("\nSorry. Jack says that's incorrect.")
		
	
def witch():
	print "\nYou take a step into the dark and find yourself standing in a witch's cauldron.\nShe says that if you can solve her riddle, she won't make you into stew. You have three guesses."
	print "\nHere's the riddle: What travels around the world while staying in a corner?"
	
	guess_correct = False
	
	for _ in range(3):
		guess = raw_input("\nWhat's your guess? ")
		guess_correct = check_witch_guess(guess)
		if guess_correct:
			print "\nWell done. You escape the witch."
			continue_on_path()
			break
		else: 
			print "\nThe witch says that's wrong. Guess again."
			
	if not guess_correct:
		print "\nThat's three guesses."
		game_over("\nSorry. You become stew.")
	
		
def check_witch_guess(guess):
	return guess in ["A stamp", "a stamp", "Stamp", "stamp"]
		
		
def continue_on_path():
	print "\nYou continue down the path when you finally come to a fork in the corn maze."
	path = raw_input("\nDo you go left or right? ")
	
	if path == "left" or path == "Left":
		sphinx()
	elif path == "right" or path == "Right":
		ghost_dog()
	else:
		game_over("\nThat's not a path.")
	
def sphinx():
	print "\n Suddenly a giant sphinx blocks your path.\nShe says that she'll show you the way out of the maze if you can answer her riddle.\nShe gives you a piece of paper that says:\nComplete the letter sequence:\n O  T  T  F  F  S  S  E   ___  ___  ___"
	
	guess = raw_input("\nWhat do you write down? ")
	while not check_sphinx_guess(guess):

		if guess == "give up":
			game_over("You've given up.")
		elif guess == "hint":
			print "\nCan you count to eleven?"
		else:
			print "\nThe Sphinx shakes her head. Incorrect.\nType 'hint' for a clue, type 'give up' to surrender, or guess again."
		
		guess = raw_input("\nGuess again: ")
		
	game_over("Excellent. You solved the sphinx's riddle and escape the maze!")


def check_sphinx_guess(answer):
	return answer in ["NTE", "N T E", "nte", "n t e"]

#	if answer in ["NTE", "N T E", "nte", "n t e"]:
#		print "\nExcellent. You solved the sphinx's riddle and escape the maze!"
#		exit(0)	
#	elif answer == "give up":
#			game_over("You've given up.")	
#	else: 
#		print "\nThe Sphinx shakes her head. Incorrect.\nType 'hint' for a clue, type 'give up' to surrender, or guess again."
#		answer = raw_input("> ")
#		
#		if answer == "hint":
#			print "\nCan you count to eleven?"
#			new_answer = raw_input("\nGuess again: ")
#			check_sphinx_guess(new_answer)
#		elif answer == "give up":
#			game_over("You've given up.")
#		else:
#			check_sphinx_guess(answer)
		

def ghost_dog():
	print "\nYou see a ghost dog running up ahead, and you can hear him barking."
	print "What do you do?"
	
	while True:
		choice = raw_input("> ")
		if "follow" in choice or "pet" in choice or "give" in choice:
			print "\nGood choice. The dog is a friend. He leads you past a dangerous pit of snakes, saving your life, and disappears."
			print "\nYou see the exit door ahead and walk out. You win!"
			exit(0)
		elif "yell" in choice or "hit" in choice or "throw" in choice:
			print "\nBad decision. That dog was a friend. You should have been nice."
			game_over("Better luck next time.")
		else:
			print "Nothing happens. Try something else."
			
def game_over(reason):
	print reason, "Game over."
	exit(0)
		
		
if __name__ == "__main__":
	start_game()
