#! /usr/bin/env python3

class ShipMap:
    def __init__(self):
        self.grid = {'Flight Deck': '.', 'Lab': '.', 'Commander': '.', 'Science Officer': '.', 'Pilot': '.', 'Mission Specialist': '.', 'Flight Engineer': '.', 'Cryo Chamber': '.', 'Docking Bay': '.'}
        self.position = 'Flight Deck'

    def move(self, new_position):
        self.grid[self.position] = '.'
        self.position = new_position
        self.grid[self.position] = 'X'

    def print_map(self):
        for key, value in self.grid.items():
            print(key, value)
