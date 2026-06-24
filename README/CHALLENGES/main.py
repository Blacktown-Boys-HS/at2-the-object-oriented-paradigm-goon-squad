import cave
from character import Enemy, Character
from item import Item

# Set up the caves
cavern = cave.Cave("Cavern")
cavern.set_description("A dank and dirty cave")
dungeon = cave.Cave("Dungeon")
dungeon.set_description("A large cave with a rack")
grotto = cave.Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")


cavern.link_cave(dungeon, "south")
dungeon.link_cave(cavern, "north")
dungeon.link_cave(grotto, "west")
grotto.link_cave(dungeon, "east")


harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

vegemite = Item("vegemite")
vegemite.set_description("A Wumpus's worst nightmare")
grotto.set_item(vegemite)

# Game loop
current_cave = cavern
dead = False
bag = []

print("Welcome to the Cave Adventure!")
print("Commands: north, south, east, west, look, take, fight, talk, pat, help")

while not dead:
    print("\n")
    current_cave.describe()
    
    inhabitant = current_cave.get_character()
    item = current_cave.get_item()
    
    if item is not None:
        item.describe()
    
    command = input("> ").lower().strip()
    
    if command == "help":
        print("Commands: north, south, east, west, look, take, fight, talk, pat")
    
    elif command == "look":
        current_cave.describe()
    
    elif command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)
        else:
            print("There is nothing to take here")
    
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to")
    
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input("> ").lower().strip()
            if inhabitant.fight(fight_with):
                print("Bravo, hero! You won the fight!")
                current_cave.set_character(None)
                if Enemy.enemies_to_defeat == 0:
                    print("Congratulations, you have survived another adventure!")
                    dead = True
            else:
                print("Scurry home, you lost the fight.")
                print("That's the end of the game")
                dead = True
        else:
            print("There is no one here to fight with")
    
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")

    else:
        print("I don't understand that command. Type 'help' for commands.")

