class user():

    def __init__(self, inventory, health=100, stamina=50): #these are attributes
        self.health = health
        self.stamina = stamina
        self.inventory = inventory # these are paremeters. before the paremeters can be set they must be chained to the attribute
        print(f"{health}, {stamina}")
        if self.stamina >= 0:
            print("your out of stamina")
    
    def manage_inventory(self, capacity=20):
        self.inventory == capacity
        if self.inventory == capacity:
            self.inventory.append()
        else:
            print("inventory full")


    def attack(self, cost_attack=5): #this attribute modifys the stamina attribute within the class
        self.stamina -= cost_attack #Attribute is what you put on top, argument is what you pass from a caller viewpoint, parameter is what's passed from a callee viewpoint.
        print(f"you attacked, {self.stamina}")

    def defend(self, cost_defend=10):
        self.stamina -= cost_defend
        print(f"you defended, {self.stamina}") 

    def parry(self, cost_parry=7):
        self.stamina += cost_parry
        print(f"you parried, {self.stamina}")

player_character = user(inventory=[])
player_character.attack(50)
#player_character.defend(10)
#player_character.parry(7)

