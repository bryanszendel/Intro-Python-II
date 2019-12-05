from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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
room['foyer'].n_to = room['overlook']
room['narrow'].n_to = room['treasure']
room['foyer'].s_to = room['outside']
room['overlook'].s_to = room['foyer']
room['treasure'].s_to = room['narrow']
room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Bryan', room['outside'])

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

while True:
    print(f"{player1.name} is currently at the {player1.current_room.name}")
    cmd = input("direction--> ")
    if cmd == 'n':
        if player1.current_room.name == 'Outside Cave Entrance':
            player1.current_room = room['outside'].n_to
        elif player1.current_room.name == 'Foyer':
            player1.current_room = room['foyer'].n_to
        elif player1.current_room.name == 'Narrow Passage':
            player1.current_room = room['narrow'].n_to
            print(player1.current_room.description)
        else: 
            print("Not allowed. Choose another move...")
    elif cmd == 's':
        if player1.current_room.name == 'Foyer':
            player1.current_room = room['foyer'].s_to
        elif player1.current_room.name == 'Grand Overlook':
            player1.current_room = room['overlook'].s_to
        elif player1.current_room.name == 'Treasure Chamber':
            player1.current_room = room['treasure'].s_to
        else:
            print("Not allowed. Choose another move...")
    elif cmd == 'e':
        if player1.current_room.name == 'Foyer':
            player1.current_room = room['foyer'].e_to
        else:
            print("Not allowed. Choose another move...")
    elif cmd == 'w':
        if player1.current_room.name == 'Narrow Passage':
            player1.current_room = room['narrow'].w_to
        else:
            print("Not allowed. Choose another move...")
    elif cmd == 'q':
        print("Goodbye!")
        break