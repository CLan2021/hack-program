#!/usr/bin/env python

"""
A function that generates a menu for what to eat
"""
import random
import pandas as pd

# path to a CSV of food options and prices
FILE = "/home/catherine/hacks/hack-program/foodmenu/menu.csv"
MENU = pd.read_csv(FILE, sep=",")

#class WhatToEat(option):
	#def __init__(self, name, price):
        #self.data = pd.read_csv(FILE, sep=",")
		#self.name = name
        #self.price = price
	
	#def getprice(self):
		#return self.price
	
	#def __str__(self):
        #return self.name + ' : ' + str(self.getprice())
	
def menu(arg):

	"""
	Function returns a food option based on 1 of the args: 
	breakfast, lunch or dinner
	"""

	b_menu = MENU["breakfast"]
	l_menu = MENU["lunch"]
	d_menu = MENU["dinner"]

	if arg == "breakfast":
		print("Enjoy your breakfast!! Here's your " + b_menu.sample())
	elif arg == "lunch":
		print("Enjoy your lunch!! Here's your " + l_menu.sample())
	elif arg == "dinner":
		print("Enjoy your dinner!! Here's your " + d_menu.sample())

#def price():
#	"""
#	Function that returns the price of the food
#	"""
#	append

if __name__ == "__main__":
	menu("breakfast")
	menu("lunch")
	menu("dinner")


	
	#def run(self, arg):
		#"""
		#Put it all together into a single function call that returns
		#"""
		#self.menu(arg)
		#return self.data

#breakfast = [
    #"chocolate pancakes and coffee",
    #"omelette and juice",
    #"cereal and milk"
#]

#lunch = [
    #"egg and avocado sandwich",
    #"chipotle bowl",
    #"chicken caesar salad"
#]

#dinner = [
	#"quinoa with chicken and lentils",
	#"shrimp pad thai",
	#"beef pho"
#]

