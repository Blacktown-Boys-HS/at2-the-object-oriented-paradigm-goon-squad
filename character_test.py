from character import Character
harry = Character("Harry", "A smelly Wumpus")
harry.describe()
class Character:
    ...
    def set_conversation(self, conversation):
        self.conversation = conversation
harry.set_conversation ("Come closer.I can’t see you!")
harry.talk() 

    def set_conversation(self, conversation):
        self.conversation = conversation

harry.set_conversation ("Come closer.I can’t see you!")
harry.talk()


harry.set_weakness("vegemite")

print("What will you fight with?")
fight_with = input()
harry.fight(fight_with)

harry.set_character

harry.get_character

while True:
    print("\n")         
    current_cave.get_details()
    # Add your code here
    command = input("> ")    
    current_cave = current_cave.move(command)

    inhabitant = current_cave.get_character()
if inhabitant is not None:
    inhabitant.describe()





