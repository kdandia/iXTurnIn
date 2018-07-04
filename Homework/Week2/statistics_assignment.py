# -*- coding: utf-8 -*-
"""
Statistics Assignment: Apartment Search tool

This assignment will help us solidify what we have learned so far about data 
manipulation and statistics

Using the Airbnb dataset (located in data/airbnb.csv), we are going to make a script
with the following functionalities:
*******************************************************************************
Functionality 1: Neighbourhood information
- Given a neighbourhood, the tool will provide the following information to the user
  - Total number of available listings in the neighbourhood
  - Number of rooms broken down per listing type
  - Average Room Price
  - Price quartiles

For example if we run the script like;

"python statistics_assignment.py information Belém"

The script will print out information about Belem.

*******************************************************************************
Functionality 2: Apartment Search.
This functionality will help the user to find an appropriate listing. It will ask
the user different listing requirements:
- desired price range
- desired number of rooms (a range)
- a list of desired neighbourhoods
If the user doesnt specifiy any of the requirements (pressing enter without typing anything)
We will consider that the user is indiferent

It will also ask the user if he/she prefers the results sorted by price, by average score
or by number of reviews.

Finally the script will print out the top 10 results matching the desired requirements and sorted
by the desired sorting criteria.

If there are no listings that match the criteria, the script will tell the user that no
listings match the criteria.

For example if we run

"python statistics_assignment.py search"

The script will start prompting us for the requirements and finally print out the results
*******************************************************************************

There should be a main() function that serves as an entrypoint.

When we load the script it will load the dataset and it will be used as the data source.
"""

import pandas as pd
import sys

data = pd.read_csv("data/airbnb.csv")
data = pd.DataFrame(data)


argument1 = sys.argv[1] 
hood = sys.argv[2]

def information(hood):
    """ functionality 1"""
    
    #make subset based on neighborhood 
    hood_data = data[data.neighborhood == hood]
    
    #total number of available listings in the neighbourhood
    available = hood_data.room_id.count()
    
    #number of rooms broken down per listing type
    listings = hood_data.groupby("room_type").count()
    
    #average Room Price
    price = hood_data.price.mean()

    #price quartiles
    quartile25 = hood_data.price.quantile(.25)
    quartile5 = hood_data.price.quantile(.50)
    quartile75 = hood_data.price.quantile(.75)
    
    
    print("The total number of available listings in " + hood + " are " + str(available) + ".")
    print("The number of rooms broken down per listing type are ")
    print(str(listings))
    print("The average room price is " + str(price) + ".")
    print("The price quartiles are " + str(quartile25) + ", " + str(quartile5) + ", " + 
          str(quartile75) + ".")
    
    pass

def search(hood):
    """ functionality 2"""
    
    #ask user for all information
    print("What is your desired price range?")
    priceinput_lower = int(input(">> "))
    priceinput_upper = int(input(">> "))
    
    print("What is your desired number of rooms range?")
    room_lower = int(input(">> "))
    room_upper = int(input(">> "))
        
    print("What are your desired neighborhoods?")
    hoodlist = list(input(">> "))
    
    
    pass

def parse_arguments():
    """ parses the arguments"""
    
    
    pass

def main(argument1):
    """main entrypoint"""
    
    pass

if __name__ == "__main__":
    if argument1 == 'information':
        information(hood)
    else:
        search()

main(argument1)
    
