# PyMagic
A simple card game loosely based on the Magic the Gathering TCG, written in Python.


# Committing Cards
In order to commit new cards, make a fork of this repository, and add the new cards on seperate lines in the monsterList.csv
file. Monsters follow this format:

"Name", cost, power, defence, "ability", unique id (increment this by one for each monster you add)

So an example monster would be 

"Black_Boa", 2, 2, 1, "First Strike", 1
following the format:
    Name     C  P  D     Ability      I
