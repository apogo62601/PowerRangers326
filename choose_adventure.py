import pandas as pd
import matplotlib.pyplot as plt
import json
from argparse import ArgumentParser
import sys



#We still need to touch on about 4 more techniques 
class player:
    def __init__(self):
        self.points = 0
        self.position = "1"
        self.log = []
        self.name = ""
        
    def setName(self):
        self.name = input("What is your name? ")
	
    def __repr__(self):
    	#METHOD: __repr__ for formal string representation
    	"""Using magic method to formally represent the player's points.
    
    	Returns:
    	str: string representation of player points.
    	"""
	return f”Player({self.points})”
        
       

def main():
# Interprets JSON dictionary file
# Justin
    with open('/Users/home/Desktop/326Homework/adventure.txt') as f:
        exampleDict = json.load(f)
    curPlayer = player()
    curPlayer.setName()
    answer = ""
    viable = False
    while variable == False:
	#Use a list comprehension to create a list of options
	options = [option for option in exampleDict[ curPlayer.position]["actions"].keys()]
	print(exampleDict[curplayer.position]['prompt'])
	print("Your options are:")
	
            else:
                print("---------------THAT IS NOT A VALID ANSWER---------------")
        if answer == "quit":
            break
        curPlayer.log.append(answer)
        print(curPlayer.log)
        print(curPlayer.points)
        curPlayer.points += exampleDict[curPlayer.position]["actions"][answer]["points"]
        curPlayer.position = exampleDict[curPlayer.position]["actions"][answer]["location"]
        viable = False
        
    
#This is a bar graph that will show good days, okay days, and bad days
#Christian
def points_graph(graph):
    df = pd.read_csv("game_points.csv")
    graph = df.plot.bar(y ='points')
    return graph
points_graph('points')


#This is a filter of only positive points
#Christian
def good_points(pos_points):
    df = pd.read_csv("game_points.csv")
    pos_points = df[df['points'] > 0]
    return pos_points
good_points('pos_points')


  
def get_points(points):
# METHOD: Reading Points File Data
# Christian
"""
Args:
  csv_file(str): csv file

Attributes:
  
Returns:
  Returns user point value as an int
"""
  df = pd.read_csv("game_script.csv")
    points = df['skip class'].iloc[0]
    return points
get_points('skip class')





def parse_args(arglist):
#METHOD: Creates command-line interface for the user
#Akash
	parser = ArgumentParser()
	parser.add_argument("file", help = "file of names and numbers")
	return parser.parse_args(arglist)

if __name__ == "__main__":
#Akash
	args = parse_args(sys.argv[1:])
	main(args.file)
