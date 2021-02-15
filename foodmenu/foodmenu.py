#!/usr/bin/env python

"""
A function that generates a menu for what to eat
"""
#import random
import pandas as pd

# path to a CSV of food options and prices
URL  = "https://raw.githubusercontent.com/CLan2021/hack-program/main/menu_option.csv"
df = pd.read_csv(URL, sep=",")

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
	
	Parameters
	----------
	String(breakfast, lunch, dinner)
	"""

	b_menu = df["breakfast"]
	l_menu = df["lunch"]
	d_menu = df["dinner"]
	option = df["option"]

	if arg == "breakfast":
		print("Enjoy your breakfast!! Here's your " + b_menu.sample())
	elif arg == "lunch":
		print("Enjoy your lunch!! Here's your " + l_menu.sample())
	elif arg == "dinner":
		print("Enjoy your dinner!! Here's your " + d_menu.sample())

def option():
	"""
	Function that returns the method for getting food
	"""
	option = df["option"]
	print("You can " + option.sample())
	

if __name__ == "__main__":
	menu("breakfast")
	menu("lunch")
	menu("dinner")
	option()


	
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

