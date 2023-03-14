import game

kitchen = game.Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

roof = game.Room("Roof")
roof.set_description("A dark place that is very cold.")

dining_hall = game.Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = game.Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

shelter = game.Room("Shelter")
shelter.set_description("A small room with a bed and a table.")

kitchen.link_room(roof, "north")
roof.link_room(kitchen, "south")
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
ballroom.link_room(shelter, "north")
shelter.link_room(ballroom, "south")

dave = game.Enemy("Dave", "A smelly zombie", 20)
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.", 30)
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

catrina = game.Friend("Catrina", "A friendly ghost")
catrina.set_conversation("Boo! I'm a ghost!")
ballroom.set_friend(catrina)

boss = game.UniqueEnemy("Boss", "A huge, scary bull, without head.", 40)
boss.set_conversation("I'm going to eat you!")
boss.set_weakness("sword")
boss.set_weakness("lighter")
roof.set_character(boss)

cheese = game.Item("cheese", 30)
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = game.Item("book", 40)
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

sword = game.Item("sword", 50)
sword.set_description("A sharp and shiny sword")

lighter = game.Item("lighter", 50)
lighter.set_description("A small and useful lighter")

shelter.set_item(lighter)

roof.set_item(sword)
roof.set_character(boss)

current_room = kitchen
backpack = {}

health = 100
dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    if current_room.get_friend() is not None:
        current_room.get_friend().describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:
                health -= inhabitant.get_damage()
                print(f"Your health is now {health}.")
                if inhabitant.fight(fight_with) == True and health > 0:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    if current_room.character.lives == 0:
                        current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack[item.get_name()] = item
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == "give":
        if current_room.get_friend():
            print("What do you want to give?")
            gift = input()
            if gift in backpack:
                health += current_room.get_friend().give(backpack[gift])
                del backpack[gift]
            else:
                print("You don't have a " + gift)
    else:
        print("I don't know how to " + command)
