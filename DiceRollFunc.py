import random

def dice_roll(): 
    press_enter = "Press Enter to roll the dice: > "
    user_input = input(press_enter)
    roll = random.randint(1, 6)
    
    if roll == 1:
        print('''
             _________
            |         |
            |         |
            |    O    |
            |         |
            |_____ ___|
              
              ''')

    if roll == 2:
        print('''
             _________
            |         |
            |    O    |
            |         |
            |    O    |
            |_____ ___|
              
              ''')

    if roll == 3:
        print('''
             _________
            |         |
            |  O      |
            |    O    |
            |      O  |
            |_________|
              
              ''')
        
    if roll == 4:
        print('''
             _________
            |         |
            |  O   O  |
            |         |
            |  O   O  |
            |_____ ___|
              ''')
 
    if roll == 5:
        print('''
             _________
            |         |
            |  O   O  |
            |    O    |
            |  O   O  |
            |_____ ___|
              
              ''')

    if roll == 6:
        print('''
             _________
            |         |
            |  O   O  |
            |  O   O  |
            |  O   O  |
            |_____ ___|
              
              ''')

dice_roll()