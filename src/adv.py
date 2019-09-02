import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

cj = Player('Cecil John', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# print(cj.location.name)
# print(type(cj.location.n_to))
# if (cj.location.s_to == False):
#     print('hello')
print("Welcome to this game, btw.")
print("So youre cj.")
print('Directions: north, south, east, west, and if youre a quitter, type quit')

while True:
    print('==========================================')
    print('==========================================')
    print(
        f'Youre currently {cj.location.name}, {cj.location.description}: What direction do you want to move to?')
    location = input('Direction: ')
    if location == 'quit':
        break
    elif location == 'north':
        if hasattr(cj.location, 'n_to'):
            cj.location = cj.location.n_to
        else:
            print('you cannot go there')
    elif location == 'south':
        if hasattr(cj.location, 's_to'):
            cj.location = cj.location.s_to
        else:
            print('you cannot go there')
    elif location == 'east':
        if hasattr(cj.location, 'e_to'):
            cj.location = cj.location.e_to
        else:
            print('you cannot go there')
    elif location == 'west':
        if hasattr(cj.location, 'w_to'):
            cj.location = cj.location.w_to
        else:
            print('you cannot go there')
    else:
        print('you cannot go there')
