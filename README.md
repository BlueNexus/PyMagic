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


# Abilities:
These will be located on the wiki at some point, but i'll list them here for now.

1. "First Strike" - Hits before the opponent
2. "Leech" - Gets some life for damage dealt
3. "Double Strike" - Gets a first strike hit, then a regular hit
4. "Flying" - Can't be blocked by anything without flying
5. "Reach" - Can block creatures with flying
6. "Cowardly" - Can't attack on its own
7. "Ranged" - Can attack without retaliation
8. "Cleave" - Deals damage to all enemy creatures

More will be added with time.
