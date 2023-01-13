#! /usr/bin/env python3

import time

def moving_spaceship():
    spaceship = [" _______  ",
                 "//      \\",
                 "|| (__V__)|",
                 "||[_____]||",
                 "\\_______//"]
    for i in range(10):
        for line in spaceship:
            print(line, end='\r')
            time.sleep(0.5)
        for j in range(len(line)):
            print(" ", end='\r')
            time.sleep(0.5)
    print("The spaceship has reached its destination!")

moving_spaceship()
