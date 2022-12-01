class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.chosen_gesture = ''
        self.wins = 0
        pass
    
    def get_input(self):
        user_input = input (f'Enter 0 to select Rock, 1 to select Paper 2 to select Scissors, 3 for Lizard and 4 for Spock ')
        try:
            converted_input = int(user_input)
        except:
            print("You entered a value that's not a number")
        self.chosen_gesture = self.gestures[converted_input]
        # if user_input != "Rock" or "Paper" or "Scissor":
        #     input ("User input not valid.  Please re enter an action from the {gesture_list}")
        # print (f"Player one chooses {user_input}")
        

        


   









  