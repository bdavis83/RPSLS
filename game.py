#from human import Human
import time

class Game:

    def __init__ (self):
    
        pass

    def run_sim (self):
        self.display_welcome ()
        self.rules ()
        pass


    def display_welcome (self):
        print ("")
        print ("\n Welcome to Rock, Paper, Scissors, Lizard, Spock! \n")

    

    def rules (self):
        print ("")
        print ("These are the rules!")
        print ("")
        time.sleep (.5)
        print ("Rock crushes Scissors")
        time.sleep (.5)
        print ("Scissors cuts Paper ")
        time.sleep (.5)
        print ("Paper covers Rock")
        time.sleep (.5)
        print ("Rock crushes Lizard ")
        time.sleep (.5)
        print ("Lizard poisons Spock")
        time.sleep (.5)
        print ("Spock Smashes Scissors")
        time.sleep (.5)
        print ("Scissors decapitates Lizard ")
        time.sleep (.5)
        print ("Lizard eats Paper")
        time.sleep (.5)
        print ("Paper disproves Spock")
        time.sleep (.5)
        print ("Spock vaporizes Rock ")
        time.sleep (.5)
        print ("")




""" o	Rock crushes Scissors   
Scissors cuts Paper  
Paper covers Rock  
Rock crushes Lizard  
Lizard poisons Spock  
Spock smashes Scissors  
Scissors decapitates Lizard  
Lizard eats Paper  
Paper disproves Spock  
Spock vaporizes Rock  
 """