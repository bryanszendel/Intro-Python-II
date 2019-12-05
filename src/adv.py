from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", items=['dirt', 'map']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items=['flashlight', 'umbrella']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items=['binoculars', 'sword', 'gunpowder']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items=['spear', 'medicine']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items=['coin', 'torch']),
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
    print(f"There are {len(player1.current_room.items)} items here:")
    for x in player1.current_room.items:
        print(f"- {x}")

    print("")
    cmd = input(">>> ")
    print("")

    available_items = player1.current_room.items # shorten access to available items

    if len(cmd) > 1:
        action_cmd = cmd.split(' ')
    if action_cmd[0] == 'get' or action_cmd[0] == 'take':
        if action_cmd[1] in available_items:
            player1.getItem(action_cmd[1])
        else:
            print("That item isn't here...")
            
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

    

    