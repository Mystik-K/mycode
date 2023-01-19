#! /usr/bin/env python3

class ShipMap:
    def __init__(self):
        self.grid = [['.', 'FLIGHT DECK', '.'],
                         ['Lab', 'Commander'],
                     ['Science Officer','Pilot'],
              ['Mission Specialist', 'Flight Engineer'],
                     ['Cryo-Chamber', 'Docking Bay']
                           ['Engine Room']]
        self.x = 3
        self.y = 3

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.grid[x][y] = 'X'

    def move_left(self):
        if self.y > 0:
            self.grid[self.x][self.y] = '.'
            self.y -= 1
            self.grid[self.x][self.y] = 'X'

    def move_right(self):
        if self.y < len(self.grid[0]) - 1:
            self.grid[self.x][self.y] = '.'
            self.y += 1
            self.grid[self.x][self.y] = 'X'

    def move_forward(self):
        if self.x > 0:
            self.grid[self.x][self.y] = '.'
            self.x -= 1
            self.grid[self.x][self.y] = 'X'

    def move_back(self):
        if self.x < len(self.grid) - 1:
            self.grid[self.x][self.y] = '.'
            self.x += 1
            self.grid[self.x][self.y] = 'X'

    def print_map(self):
        for row in self.grid:
            print(' '.join(row))

    def print_position(self):
        print("You are currently at position: ({}, {})".format(self.x, self.y))

ship_map = ShipMap()

while True:
    command = input("Enter a command (left, right, forward, back, map or exit): ")
    if command == "left":
        ship_map.move_left()
    elif command == "right":
        ship_map.move_right()
    elif command == "forward":
        ship_map.move_forward()
    elif command == "back":
        ship_map.move_back()
    elif command == "map":
        ship_map.print_map()
        ship_map.print_position()
    elif command == "exit":
        break
    else:
        print("Invalid command")
