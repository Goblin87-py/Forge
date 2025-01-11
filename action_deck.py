import random

action_deck = {"Parry": "parry_card()"}

def parry_card(self):
    print('''Roll 1d6, if and even result, parry next attack
          and regain 7 stamina, otherwise miss and loose 7 stamina''')
    use = input("> ")
    if use == "play parry":
        result = random.randint(1, 6)
        print(result)
        if result: 
            2, 4 or 6 
            print("You Parried!")
            self.stamina += 7
        else: 
            print("You missed!")
            self.stamina -= 7
    
