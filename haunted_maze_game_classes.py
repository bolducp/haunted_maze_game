from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter() ."
        exit(1)
        

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()
        
        
class Death(Scene):
    quips = [
        "Haunted mazes are tough, man. Better luck next time.", 
        "A headless horseman gallops up and carries you away into the haunted maze forever.",
        "Hundreds of spiders descend from the sky and weave you into a human cocoon for supper.",
        ]
        
    def enter(self):
        print "\n" + Death.quips[randint(0, len(self.quips)-1)] + "\n"
        exit(1)
        
    
class Maze_beginning(Scene):
    def enter(self):
        print "\nWelcome to the haunted maze.\n"
        print "Enter the corn maze and choose a path.\n"
        
        path = raw_input("\nDo you go left or right? ")
	
        if path == "left" or path == "Left":
            return "Jack_the_ripper"
            
        elif path == "right" or path == "Right":
            return "Witch"
            
        else:
            print "That's not a path!"
            return "Death"
    
    
class Jack_the_ripper(Scene):
    def enter(self):
        print "\nAs you walk down the path, you trip over a rock and fall into the arms of Jack the Ripper."
        print "\nJack gives you one chance to answer his riddle. If you are correct, he'll let you continue on the path."
        print "\nHere's the riddle: \nWhat is greater than God,\nmore evil than the devil,\nthe poor have it,\nthe rich need it,\nand if you eat it, you'll die?"
        
        guess = raw_input("\nWhat's your answer? ")
	
        if guess == "nothing" or guess == "Nothing":
            return "Continue_on_path"
        else:
            print "\nSorry. Jack says that's incorrect."
            return "Death"
    
    
class Witch(Scene):
    def enter(self):
        print "\nYou take a step into the dark and find yourself standing in a witch's cauldron.\nShe says that if you can solve her riddle, she won't make you into stew. You have three guesses."
        print "\nHere's the riddle: What travels around the world while staying in a corner?"
	
        guess_correct = False
	
        for _ in range(3):
            guess = raw_input("\nWhat's your guess? ")
            guess_correct = self.check_witch_guess(guess)
            if guess_correct:
                print "\nWell done. You escape the witch."
                return "Continue_on_path"
                break
            else: 
                print "\nThe witch says that's wrong. Guess again."
                
        if not guess_correct:
            print "\nThat's three guesses."
            return "Death"
           

    def check_witch_guess(self, guess):
        return guess in ["A stamp", "a stamp", "Stamp", "stamp"]
        
        
    
class Continue_on_path(Scene):
    def enter(self):
        print "\nYou continue down the path when you finally come to a fork in the corn maze."
        path = raw_input("\nDo you go left or right? ")
	
        if path == "left" or path == "Left":
            return "Sphinx"
            
        elif path == "right" or path == "Right":
            return "Ghost_dog"
        
        else:
            print "\nThat's not a path."
            return "Death"
    
    
class Sphinx(Scene):
    def enter(self):
        print "\n Suddenly a giant sphinx blocks your path.\nShe says that she'll show you the way out of the maze if you can answer her riddle.\nShe gives you a piece of paper that says:\nComplete the letter sequence:\n O  T  T  F  F  S  S  E   ___  ___  ___"
	
        guess = raw_input("\nWhat do you write down? ")
        
        while not self.check_sphinx_guess(guess):

            if guess == "give up":
                print "You've given up."
                return "Death"
                
            elif guess == "hint":
                print "\nCan you count to eleven?"
            else:
                print "\nThe Sphinx shakes her head. Incorrect.\nType 'hint' for a clue, type 'give up' to surrender, or guess again."
		
            guess = raw_input("\nGuess again: ")
		
        print "Excellent. You solved the sphinx's riddle and escape the maze!"
        return "Finished"


    def check_sphinx_guess(self, answer):
        return answer in ["NTE", "N T E", "nte", "n t e"]
    
    
class Ghost_dog(Scene):
    def enter(self):
        print "\nYou see a ghost dog running up ahead, and you can hear him barking."
        print "What do you do?"
	
        while True:
            choice = raw_input("> ")
            if "follow" in choice or "pet" in choice or "give" in choice:
                print "\nGood choice. The dog is a friend. He leads you past a dangerous pit of snakes, saving your life, and disappears."
                print "\nYou see the exit door ahead and walk out. You win!"
                return "Finished"
                
            elif "yell" in choice or "hit" in choice or "throw" in choice:
                print "\nBad decision. That dog was a friend. You should have been nice."
                return "Death"
                
            else:
                print "Nothing happens. Try something else."
        
        
class Finished(Scene):
    def enter(self):
        print "\nYou won! Congratulations."
        exit(1)
       
       
class Map(object):

    scenes = {
        "Maze_beginning": Maze_beginning(),
        "Jack_the_ripper": Jack_the_ripper(),
        "Witch": Witch(),
        "Continue_on_path": Continue_on_path(),
        "Sphinx": Sphinx(),
        "Ghost_dog": Ghost_dog(),
        "Death": Death(),
        "Finished": Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
        
a_map = Map('Maze_beginning')
a_game = Engine(a_map)
a_game.play()
    

    

        
        
        
        
        