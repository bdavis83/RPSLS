class Player:

    def __init__(self, name) -> None:
        self.name = name
        #self.gesture_list = ["Rock", "Paper", "Scissor "]
        #self.get_input ()
 #       self.gestures ()
  #      print (self.gesture_list)

    
    def get_input (self):
        gesture_list = ["Rock", "Paper", "Scissor"]
        user_input = input (f'Choose from {gesture_list}')
        print (f"Player one chooses {user_input}")
        
        print (user_input)
        #return user_input

   
   
 #   def gestures (self):
  #      gesture_one = "rock" 
  #      self.gesture_list.append (gesture_one)
  #      gesture_two = "paper" 
  #      self.gesture_list.append (gesture_two)
  #      gesture_three = "scissor" 
  #      self.gesture_list.append (gesture_three)
        


   









    #user_action = gesture_input ()
   # print (user_action)