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

player1 = Player('Bryan', room['outside']) # Make a new player object that is currently in the 'outside' room.

while True:
    print(f"{player1.name} is currently at the {player1.current_room.name}")
    cmd = input("--> ")
    if cmd == 'n':
        if player1.current_room.n_to is None:
            print("Not allowed. Choose another move...")
        else: 
            player1.current_room = player1.current_room.n_to
    elif cmd == 's':
        if player1.current_room.s_to is None:
            print("Not allowed. Choose another move...")
        else:
            player1.current_room = player1.current_room.s_to
    elif cmd == 'e':
        if player1.current_room.e_to is None:
            print("Not allowed. Choose another move...")
        else:
            player1.current_room = player1.current_room.e_to
    elif cmd == 'w':
        if player1.current_room.w_to is None:
            print("Not allowed. Choose another move...")
        else:
            player1.current_room = player1.current_room.w_to
    elif cmd == 'q':
        print("Goodbye!")
        break