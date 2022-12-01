#from human import Human
import time
from human import Human
from ai import Ai

class Game:

    def __init__ (self):
        self.player_one = None
        self.player_two = None
        pass

    def run_sim (self):
        self.display_welcome ()
        self.rules ()
        self.choose_players ()
        self.play_rounds ()
        self.declare_winner ()
        pass


    def display_welcome (self):
        print ()
        print ("\n Welcome to Rock, Paper, Scissors, Lizard, Spock! \n")

    

    def rules (self):
        print ("")
        print ("These are the rules! ")
        print ("")
        time.sleep (.5)
        print ("Rock crushes Scissors ")
        time.sleep (.5)
        print ("Scissors cuts Paper ")
        time.sleep (.5)
        print ("Paper covers Rock")
        time.sleep (.5)
        print ("Rock crushes Lizard ")
        time.sleep (.5)
        print ("Lizard poisons Spock ")
        time.sleep (.5)
        print ("Spock Smashes Scissors ")
        time.sleep (.5)
        print ("Scissors decapitates Lizard ")
        time.sleep (.5)
        print ("Lizard eats Paper ")
        time.sleep (.5)
        print ("Paper disproves Spock ")
        time.sleep (.5)
        print ("Spock vaporizes Rock ")
        time.sleep (.5)
        print ("")

    def choose_players(self):
        user_choice = input("Press 1 for single player and 2 for multi-player ")
        if user_choice == "1":
            user_name = input("what is player ones name? ")
            self.player_one = Human(user_name)
            self.player_two = Ai()
        if user_choice == "2":
            player_one_name = input("What is player ones name? ")
            self.player_one = Human(player_one_name)
            player_two_name = input("What is player twos name? ")
            self.player_two = Human(player_two_name)

    def play_rounds(self): # check if tie, check if player one win, else player two wins
        while self.player_one.wins <2 and self.player_two.wins <2:
            self.player_one.get_input()
            self.player_two.get_input()
            if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
                print("its a tie keep playing")
            elif self.player_one.chosen_gesture == 'Rock' and (self.player_two.chosen_gesture == 'Scissors' or self.player_two.chosen_gesture == 'Lizard'):
                print(f'{self.player_one.chosen_gesture} beats {self.player_two.chosen_gesture} one point awarded to {self.player_one.name}')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Scissors' and (self.player_two.chosen_gesture == 'Paper' or self.player_two.chosen_gesture == 'Lizard'):
                print(f'{self.player_one.chosen_gesture} beats {self.player_two.chosen_gesture} one point awarded to {self.player_one.name}')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Paper' and (self.player_two.chosen_gesture == 'Rock' or self.player_two.chosen_gesture == 'Spock'):
                print(f'{self.player_one.chosen_gesture} beats {self.player_two.chosen_gesture} one point awarded to {self.player_one.name}')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Lizard' and (self.player_two.chosen_gesture == 'Spock' or self.player_two.chosen_gesture == 'Paper'):
                print(f'{self.player_one.chosen_gesture} beats {self.player_two.chosen_gesture} one point awarded to {self.player_one.name}')
                self.player_one.wins += 1
            elif self.player_one.chosen_gesture == 'Spock' and (self.player_two.chosen_gesture == 'Rock' or self.player_two.chosen_gesture == 'Scissors'):
                print(f'{self.player_one.chosen_gesture} beats {self.player_two.chosen_gesture} one point awarded to {self.player_one.name}')
                self.player_one.wins += 1
            else:
                print (f"{self.player_two.chosen_gesture} beats {self.player_one.chosen_gesture} one point awarded to {self.player_two.name}")
                self.player_two.wins += 1

            
    def declare_winner (self):
        if self.player_one.wins == 2:
            print (f'{self.player_one.name} wins!')
        elif self.player_two.wins == 2:
            print (f"{self.player_two.name} wins!")



            
        

