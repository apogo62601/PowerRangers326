import pandas as pd



#We still need to touch on about 4 more techniques 
class Player:
  def __init__(self,name):
   self.name = name
 
  
if __name__ == "__main__":

 class Choices:
  
   def __init__(self):
      pass
  
  
  
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
get_points('wake up')



def Conditional_Choices(Storychoice1, Storychoice2, Storychoice = None):
# METHOD: Printing prompted if storychoice#1 or storychoice#2 is chosen
# Aelina
"""Checks between routes that are choosable and adds to history list of choices made
Args:
  Storychoice1 (str): A user route option
  Storychoice2 (str): Another user route option
  Storychoice3 (str): Optional parameter for certain choice prompts
  
Attributes:
  self.list (list): Storage of previous choices made

RaiseError:
  Error if chosen user option is not valid. Loops back to prior options
  
"""
with open """akash's file""" as conditions:

 for x in """akash's file""":
  print(f"Your choice is {"""choice"""}, you currently have {"""points"""} points.")



def Set_Story_Intersections(person_day):
# METHOD: Checking if story choices have the same text-outcome and/or points amount
# Justin
""" Check overall user route to determine if a mojority of choices were good/bad to determine how the day was
Args:
  person_day (str): description of the persons day
 
 Returns: 
  print statement regarding the quality of their day as a string
"""

    if points >= 60:
        print("It was a good day")
        
    if points < 60:
        print("It was a bad day")
      
    bad_choices_set = {"hello", "bye"}
    
    good_choices_set = {"hello", "cool", "bye"}
    
    total_set = bad_choices_set & good_choices_set
    
    Counter(points, point_change)
    
    # List comprehension for finding point amount needed to 
    threshold_adder = [x+1 for x in bad_choices_set if x < 60]
    
    
    
    


def With_Conditions(filepath, condition1):
# METHOD: Open text file (.txt) with prompts and then put conditions in based on user picks
# Akash
"""
Args:
  path(str): file path to text prompts
  condition1(str): condition user picks

Side effects:
  Prints to stdout

"""



def __repr__():
# METHOD: __Repr__ for formal strings
"""Using magic method to formally represent

Returns: 
  str: string representation
"""

def Counter(points, point_change):
# METHOD: Counter for Points (add/subtract)
# Abel
""" Counts the amount of points the user receives.
Args:
  points(int): Amount of points the user has.
  point_change(int): Amount of points the user gains/ loses.

Returns:
  The sum of points that is awarded to the user as an int.
"""
