#! usr/bin/env python

"""
A function that generates a menu for what to eat
"""
import random

breakfast = [
    "chocolate pancakes and coffee",
    "omelette and juice",
    "cereal and milk"
]

lunch = [
    "egg and avocado sandwich",
    "chipotle bowl",
    "chicken caesar salad"
]

dinner = [
	"quinoa with chicken and lentils",
	"shrimp pad thai",
	"beef pho"
]


def menu(arg):
	if arg == "breakfast":
		print("Enjoy your breakfast!! Here's your " + random.choice(breakfast))
	elif arg == "lunch":
		print("Enjoy your lunch!! Here's your " + random.choice(lunch))
	elif arg == "dinner":
		print("Enjoy your dinner!! Here's your " + random.choice(dinner))

if __name__ == "__main__":
	menu("breakfast")
	menu("lunch")
	menu("dinner")