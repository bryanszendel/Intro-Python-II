# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def __str__(self):
        return f"name: {self.name}, current_room: {self.current_room}"
    def getItem(self, item):
        self.items.append(item)
        print(f"You got the {item}!")
    def dropItem(self, item):
        self.items.remove(item)
        print(f"You dropped the {item}.")