
import random


class npc():

    def __init__(self, health=10, stamina=10):
        self.health = health
        self.stamina = stamina
    
    def npc_parry_action(self, cost_parry=5):
        self.stamina -= cost_parry
   
        result = random.randint(1, 6)

        if result: 
            2, 4 or 6 
            print("Enemy Parried!")
            self.stamina += 5
        else: 
            print("Enemy Missed!")
            self.stamina -= 5    

    def npc_block_action(self, cost_block=5):
        self.stamina -= cost_block
   
        result = random.randint(1, 6)
     
        if result == (3, 4, 5 or 6):
            print("Enemy Blocked")
        else:
            print("Enemy missed the block")
   

    def npc_attack_action(self, cost_atk=5):
        self.stamina -= cost_atk
   
        result = random.randint(1, 6)

        if result in (3, 4, 5, 6):
            print("Enemy Hit!")
        else: 
            print("Enemy Missed the Attack")
   

    def npc_take_action(self):
        take_action = random.randint(1,3)
        if take_action == 1:
            self.npc_parry_action()
        if take_action == 2:
            self.npc_block_action()
        if take_action == 3:
            self.npc_attack_action()
        
        
        if hasattr(self, 'last_action') and self.last_action == take_action:
            if hasattr(self, 'repeat_count'):
                self.repeat_count += 1
            else:
                self.repeat_count = 1
        else:
            self.repeat_count = 1

        self.last_action = take_action

        if self.repeat_count >= 3:
            take_action = random.choice([1, 2, 3])
            while take_action == self.last_action:
                take_action = random.choice([1, 2, 3])
            self.repeat_count = 1

npc = npc(10, 10)
npc.npc_take_action()