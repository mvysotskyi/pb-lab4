"""
Game module.
"""

class Item:
    """
    An item that can be picked up and used.
    """
    def __init__(self, name: str, value: int) -> None:
        self.name = name
        self.value = value
        self.description = None

    def get_name(self) -> str:
        """
        Get the item name.
        """
        return self.name

    def set_description(self, item_description: str) -> None:
        """
        Set the item description.
        """
        self.description = item_description

    def describe(self) -> None:
        """
        Print the item name and description.
        """
        print(f"The [{self.name}] is here - {self.description}")

class Room:
    """
    Room class.
    """
    def __init__(self, room_name: str) -> None:
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.friend = None

    def get_character(self) -> "Character":
        """
        Get the character in the room.
        """
        return self.character

    def set_character(self, character: "Character") -> None:
        """
        Set the character in the room.
        """
        self.character = character

    def get_friend(self) -> "Friend":
        """
        Get the friend in the room.
        """
        return self.friend

    def set_friend(self, friend: "Friend") -> None:
        """
        Set the friend in the room.
        """
        self.friend = friend

    def get_details(self) -> None:
        """
        Print the room name and description.
        """
        print(self.name)
        print("----------------")
        print(self.description)

        for direction, room in self.linked_rooms.items():
            print("The " + room.name + " is " + direction)

    def set_description(self, room_description: str) -> None:
        """
        Set the room description.
        """
        self.description = room_description

    def link_room(self, room_to_link: "Room", direction: str) -> None:
        """
        Link this room to another room in the given direction.
        """
        self.linked_rooms[direction] = room_to_link

    def move(self, direction: str) -> "Room":
        """
        Move to the room linked in the given direction.
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def get_item(self) -> "Item":
        """
        Get the item in the room.
        """
        return self.item

    def set_item(self, item: "Item") -> None:
        """
        Set the item in the room.
        """
        self.item = item

class Character:
    """
    Character class.
    """
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversation: str) -> None:
        """
        Set what this character will say when talked to.
        """
        self.conversation = conversation

    def describe(self) -> None:
        """
        Print the character name and description.
        """
        print(f"{self.name} is here!\n{self.description}")

    def talk(self) -> None:
        """
        Print the character conversation.
        """
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

class Enemy(Character):
    """
    Enemy class.
    """
    defeated: int = 0
    def __init__(self, name: str, description: str, damage: int):
        super().__init__(name, description)

        self.weaknesses = []
        self.defeated = 0
        self.damage = damage
        self.lives = 1

    def describe(self) -> None:
        super().describe()
        print(f"Enemy damage: {self.damage}")

    def get_damage(self) -> int:
        """
        Get the enemy damage.
        """
        return self.damage

    def set_weakness(self, weakness: str) -> None:
        """
        Set the enemy weakness.
        """
        self.weaknesses.append(weakness)

    def get_defeated(self) -> int:
        """
        Get the number of times the enemy has been defeated.
        """
        return Enemy.defeated

    def fight(self, combat_item: str) -> bool:
        """
        Fight the enemy.
        """
        if combat_item in self.weaknesses:
            self.lives -= 1
            print(f"You fend {self.name} off with the {combat_item}")
            Enemy.defeated += 1
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

class UniqueEnemy(Enemy):
    """
    UniqueEnemy class.
    """
    def __init__(self, name: str, description: str, damage: int):
        super().__init__(name, description, damage)
        self.lives = 2

    def fight(self, combat_item: str) -> bool:
        """
        Fight the enemy.
        """
        if combat_item in self.weaknesses:
            if self.lives <= 1:
                print(f"You fend {self.name} off with the {combat_item}")
                Enemy.defeated += 1
            else:
                self.lives -= 1
                print("You hit the enemy, but it is still alive!")
                print(f"{self.name} says: You thing I'm weak? I have {self.lives} lives!")

            return True
        else:
            print(f"{self.name} says: You believed that you can defeate me?! Hahahaha!")
            print(f"{self.name} crushes you, puny adventurer!")
            return False

class Friend(Character):
    """
    Friend class.
    """
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def give(self, gift: Item) -> None:
        """
        Give a gift to the friend.
        """
        print(f"{self.name} receives the {gift.get_name()} and thanks you for it.")
        health =  int(gift.value * 0.8)
        print("Your health increases by " + str(health) + " points.")
        return health
