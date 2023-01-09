#! /usr/bin/env python3

a = " bottles of beer on the wall! "
b = " bottles of beer! Take one down, pass it around! "
print("Pick a number between 1 and 100")
start = int(input(" >"))

while start >= 100 and start <= 1:
    print("Sorry, that is not a number between and 100, try again")
    print(input(">"))


for num in range (start,0,-1):
    print(str(num) + a + str(num) + b)
    newnum = num - 1
    print(str(newnum) + a)
    print("\n")


