#!/usr/bin/env python

"""
Command line interface for menu.
"""

import argparse
import random
from test.foodmenu import menu

def parse_command_line():
    "Parses arguments for the menu funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--breakfast",
        help = "Returns a breakfast option",
        action = "store_true")

    # add long args
    parser.add_argument(
        "--lunch",
        help = "Returns a lunch option",
        action = "store_true")

    # add long args
    parser.add_argument(
        "--dinner",
        help = "Returns a dinner option",
        action = "store_true")

    # parse args
    args = parser.parse_args()
    
    # Check that only one argument was entered.
    if sum([args.breakfast, args.lunch, args.dinner]) > 1:
        raise SystemExit(
            "Enter only one argument at a time.")
    return args

def main():
    "Run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # pass argument to call compliments function
    if args.breakfast:
        menu("breakfast")
    elif args.lunch:
        menu("lunch")
    elif args.dinner:
        menu("dinner")


if __name__ == "__main__":
    menu("breakfast")
	menu("lunch")
	menu("dinner")