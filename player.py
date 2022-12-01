class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.chosen_gesture = ''
        self.wins = 0
        pass
    
    #def get_input(self):
    #    user_input = input (f'Enter 0 to select Rock, 1 to select Paper 2 to select Scissors, 3 for Lizard and 4 for Spock ')
     #   try:
     #       converted_input = int(user_input)
     #   except:
     #       print("You entered a value that's not a number")
     #   self.chosen_gesture = self.gestures[converted_input]
        
        

    def get_input(self):
        user_input = input (f'Enter 0 to select Rock, 1 to select Paper 2 to select Scissors, 3 for Lizard and 4 for Spock ')
        converted_input = int(user_input)
        if converted_input < 0 or converted_input > 4:
            input ("You entered a value that's not a valid selection. Please enter a a valid selection")
        else:
            self.chosen_gesture = self.gestures[converted_input]


   









  