
import random

class Character(object):

    def __init__(self, health=10, stamina=10):
        self.health = health
        self.stamina = stamina
    
    def display_status(self, name = "Character"):
        print(f''' Name: {name}
 Health: {self.health}
 Stamina: {self.stamina}''')
        
         
                
class CharacterCombatActions(Character):

    def __init__(self, health=10, stamina=10):
        super().__init__(health, stamina)
       
    def parry_action(self, cost_parry=5):
        self.stamina -= cost_parry
        
        result = random.randint(1, 6)

        if result in (2, 4, 6):
            print(f"You rolled:", {result})
            print("You Parried!")
            self.stamina += 5
         
            
        if result in (1, 3, 5):
            print(f"You rolled:", {result})
            print("You Missed!")
            self.stamina -= 5

        self.display_status()  
            
    
    def block_action(self, cost_block=5):
        self.stamina -= cost_block

        result = random.randint(1, 6)
        
        if result in (3, 4, 5, 6):
            print(f"You rolled: {result}")
            print("You blocked!") 
        else:
            print(f"You rolled: {result}")
            print("You missed the block!")


    def atk_action(self, cost_atk=5):
        self.stamina -= cost_atk
        
        result = random.randint(1, 6)

        if result in (3, 4, 5, 6):
            print(f"You rolled: {result}")
            print("You Hit!")    
        
        if result in (1, 2):
            print(f"You rolled: {result}") 
            print("You Missed!")






























