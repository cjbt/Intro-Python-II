import sys
from room import Room
from item import Item
from player import Player

# Declare all the rooms

s = Item("sword", "It's a weapon... use it.")
gs = Item("greatsword", "It's a bigger weapon... use it.")
d = Item("dagger", "It's a tiny weapon... use it.")
b = Item("boot", "Someone's boot and it's not even a pair of boots.")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [s, gs, d]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [b]),
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

cj = Player('Cecil John', room['outside'], [])

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

# print(cj.current_room.name)
# print(type(cj.current_room.n_to))
# if (cj.current_room.s_to == False):
#     print('hello')
print("Welcome to this game, btw.")
print("So youre cj.")
print('Directions: n: north, s: south, e: east, w: west, and if youre a quitter, type quit')
print("type 'o' to see check for items around the room")

while True:
    print('==========================================')
    print('==========================================')
    print(
        f'Your current room is {cj.current_room.name}. {cj.current_room.description}. Around the room the items that are available are: {[str(i.name) for i in cj.current_room.items]}. What do you want to do or where do you want to go?')
    current_room = input('Direction: ').strip().lower().split()
    print('==========================================')

    if len(current_room) == 2:
        if current_room[0] == 'get' or current_room[0] == 'take':
            item = [
                i.name for i in cj.current_room.items if i.name == current_room[1]]
            index = [i.name for i in cj.current_room.items]
            indexed = item.index(item[0])
            print(indexed)
            if len(item) > 0:
                current_item = item[0]
                cj.inventory.append(current_item)
                del cj.current_room.items[indexed]
            else:
                print('item not found')
        else:
            print('unknown commands')
            break

    if len(current_room) == 1:
        if len(current_room[0]) > 1:
            print('unknown commands')
            break
        if current_room[0] == 'q':
            break
        elif current_room[0] == 'n':
            if hasattr(cj.current_room, 'n_to'):
                cj.current_room = cj.current_room.n_to
            else:
                print('you cannot go there')
        elif current_room[0] == 's':
            if hasattr(cj.current_room, 's_to'):
                cj.current_room = cj.current_room.s_to
            else:
                print('you cannot go there')
        elif current_room[0] == 'e':
            if hasattr(cj.current_room, 'e_to'):
                cj.current_room = cj.current_room.e_to
            else:
                print('you cannot go there')
        elif current_room[0] == 'o':
            print([str(i.name) for i in cj.current_room.items])
        elif current_room[0] == 'i':
            print(f'Your inventory: {cj.inventory}')
        elif current_room[0] == 'w':
            if hasattr(cj.current_room, 'w_to'):
                cj.current_room = cj.current_room.w_to
            else:
                print('you cannot go there')
        else:
            print('you cannot go there')
