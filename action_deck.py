import random



def parry_action(self, cost_parry=5):
    self.stamina -= cost_parry
    print('''Roll 1d6, If the result is an even number, You parry the next atack and gain 5 stamina.
             If the result is an odd number, Miss the parry and loose 5 stamina''') 
    
    print(result)
    if result: 
        2, 4 or 6 
        print("You Parried!")
        self.stamina += 5
    else: 
        print("You missed!")
        self.stamina -= 5


def block_action(self, cost_block=5):
    self.stamina -= cost_block
    print("Roll 1d6 to block")

    result = random.randint(1, 6)
     
    print(result)

    if result == (3, 4, 5 or 6):
        print("You blocked")
    else:
        print("You missed the block")


def attack_action(self, cost_atk=5):
    self.stamina -= cost_atk
    print("Roll 1d6 to Attack")

    result = random.randint(1, 6)

    print(result)

    if result == (3, 4, 5 or 6):
        print("You hit!")
    else: 
        print("You missed")