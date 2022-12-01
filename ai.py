from player import Player
import random

class Ai (Player):
    def __init__ (self):
        super ().__init__("AI")


    def get_input(self):
        self.chosen_gesture = random.choice(self.gestures)
        print (f"AI chooses {self.chosen_gesture}")

       