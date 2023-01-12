#! /usr/bin/env python 3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


ne_animals = farms[0]["agriculture"]
w_animals = farms[1]["agriculture"]
se_animals = farms[2]["agriculture"]

#print ne animals
for a in ne_animals:
    print(a)

#user input
print("""Choose a farm!
        A. NE Farm
        B. W Farm
        C. SE Farm""")

farm_choice = input("\n>")
farm_choice = farm_choice.lower()

#output from user input
if farm_choice == 'a':
    print(ne_animals)
elif farm_choice == 'b':
    print(w_animals)
else:
    print(se_animals)



