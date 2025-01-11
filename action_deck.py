import random



def parry_action(self, cost_parry=5):
    self.stamina -= cost_parry
    print('''Roll 1d6, If the result is an even number, You parry the next atack and gain x stamina.
             If the result is an odd number, Miss the parry and loose x stamina''') 
               
    
    result = random.randint(1, 6)
    
    print(result)
    if result: 
        2, 4 or 6 
        print("You Parried!")
        self.stamina += 5
    else: 
        print("You missed!")
        self.stamina -= 5
    
   