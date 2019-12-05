# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
# north = Room(name='North Room', description='The room to the North')
# south = Room(name='South Room', description='The room to the South')
# east = Room(name='East Room', description='The room to the East')
# west = Room(name='West Room', description='The room to the West')