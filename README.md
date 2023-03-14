# pb-lab4

## Task 5.

In this task I implemented different classes for game in file [main.py](task5/main.py).

- ```Item``` class is a class for item in game. It has a name, description.
- ```Room``` class is a class for room in game. It has a name, description and list of items in room.
- ```Character``` class is a class for character in game. It has a name, description and list of items in character's inventory.
- ```Enemy``` class derived from ```Character``` class. Adds methods to set weakness and fight. Also have class variable ```defeated``` which is counter of defeated enemies.
- ```Friend``` class derived from ```Character``` class. Is empty cuz it's not used in this task is not present in [main.py](task5/main.py).

The example of gameplay can be found in [log.txt](task5/log.txt) file.

## Task 6.

In this task I made game a bit more complicated by adding new classes and methods and changes existing ones.

Changes in classes:
- ```Item``` class now has a ```value``` field which is used to calculate score.
- ```Enemy``` class now has a ```damage``` which enemy can do to player.

New classes:
- ```UniqueEnemy``` class derived from ```Enemy``` class. Those enemies have more life and damage than usual enemies.
- ```Friend``` class derived from ```Character``` implemented. Is used to help player. If you give them item they will give you something in return(additional health points).

To win in this game you have to defeate at least 2 enemies. If you get the score lover than 1 you lose.

In [main.py](task6/main.py) you can find my variant of game using new classes and methods. This is modified original file and main purpose is just to show how new functionality works. The example of gameplay can be found in [log.txt](task6/log.txt) file. 