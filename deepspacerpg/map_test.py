#! /usr/bin/env python3

from ship_map import ShipMap
ship_map = ShipMap()

while True:
    command = input("Enter a command(map, move, exit): ")
    if command == "map":
        ship_map.print_map()
    elif command == "move":
        new_position = input("Enter the room you would like to move to: ")
        if new_position in ship_map.grid:
            ship_map.move(new_position)
        else:
            print("Invalid room")
    elif command == "exit":
        break
    else:
        print("Invalid command")

