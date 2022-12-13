import pandas as pd
import matplotlib.pyplot as plt
import json
from argparse import ArgumentParser
import sys



 
class Player:
""" A class for Player 1.
    Atributes:
        points (int): The default amount of points to be added to for each choice made
	position (int): The player's position in the branching story paths
	log (list): A history where each player choice is saved
	name (str): An empty string for players to enter their names
        """
    def __init__(self):
	""" Assigns attributes to Player
	Atributes:
        	points (int): The default amount of points to be added to for each choice made
		position (int): The player's position in the branching story paths
		log (list): A history where each player choice is saved
		name (str): An empty string for players to enter their names
		
	Side effects:
		creates global variables to stdout
	"""
        self.points = 0
        self.position = "1"
        self.log = []
        self.name = ""
        
    def setName(self):
	""" Establishes player name based on input
	
	Side effects:
		Prompts user for Player name
	"""
        self.name = input("What is your name? ")
	
    def __repr__(self):
	"""Creates formal representation of the user's attributes. Includes the user's name, number of points, their position in the game, and log of points.
	
	Arguments:
		self(str): player attributes.
	Returns:
		Formal represenation of attributes as a string.
	"""
	return f"Player(name={self.name}, points={self.points}, position={self.position}, log={self.log})"

class Player2(Player):
	""" Child of Player class
        """
    def __init__(self):
	""" Initializes Player 2"""
        super().__init__()
	

def main(filename):
""" Path to file with user choices.
	Args:
        	filename(str): Path to text file "adventure.txt" with prompts for the player to choose from
	Side effects:
		begins game for user and presents them with prompts
		"""
    with open(filename) as f:
        exampleDict = json.load(f)
    curPlayer = Player()
    curPlayer.setName()
    answer = ""
    viable = False
    while answer != "quit":
        while viable == False:
            options = [option for option in exampleDict[curPlayer.position]["actions"].keys()]
            print(exampleDict[curPlayer.position]['prompt'])
            print("Your options are:")
            for option in options:
                print(option)
            answer = input("What would you like to do?: ")
            if answer in options or answer == "quit":
                viable = True
            else:
                print("---------------THAT IS NOT A VALID ANSWER---------------")
        if answer.lower() == "quit":
            break
        curPlayer.log.append(answer)
        print(curPlayer.log)
        print(curPlayer.points)
        curPlayer.points += exampleDict[curPlayer.position]["actions"][answer]["points"]
        curPlayer.position = exampleDict[curPlayer.position]["actions"][answer]["location"]
        viable = False
        
    
def points_graph(points):
    """A bar graph that will show different choices and points associated

    Args:
        points (str): string of points from csv
    Side effect:
        Shows bar graph
    """
    df = pd.read_csv("game_points.csv")
    df.plot.bar(y =points)
    plt.show()
points_graph('points')

def good_points(pos_points):
"""Uses pandas filtering to filter only positive points

    Args:
        pos_points (str): string of good points from dataframe

    Returns:
        pos_points: string of only positive points
    """
    df = pd.read_csv("game_points.csv")
    pos_points = df[df['points'] > 0]
    return pos_points
print(good_points('pos_points'))
good_points('pos_points')

def get_points(points):
"""This function gets points from a csv

    Args:
        points (str): string of points from csv

    Returns:
        points: points associated with user selection
    """
    df = pd.read_csv("game_script.csv")
    return df[points].iloc[0]
print(get_points('skip class'))
get_points('skip class')


def parse_args(arglist):
"""Parses command-line arguments from the user input.

   Args:
	arglist(str): command-line argument
	
   Returns:
	Converted command line input into Python script.
   """
	parser = ArgumentParser()
	parser.add_argument("file", help = "JSON file of branching choices/points/prompts")
	return parser.parse_args(arglist)

if __name__ == "__main__":
	args = parse_args(sys.argv)
	main("adventure.txt") # If this does not work, use full path to file
			      # Example: "/Users/home/Desktop/326Homework/adventure.txt"
			      # Make sure text file is in same directory as this script
