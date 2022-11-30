class Player:

    def __init__(self) -> None:
       
        pass

    def gesture_input ():
        gesture_list = ["rock", "paper", "Scissor", "lizard", "spock"]
        user_input = input ("Enter 0 for rock, 1 for scissor, 2 for paper, 3 for lizard, 4 for spock")
        return user_input


    user_action = gesture_input ()
    print (user_action)