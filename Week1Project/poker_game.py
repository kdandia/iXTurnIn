# -*- coding: utf-8 -*-
"""
Created on Friday 6/29/18
This is my pokergame.py file.

I have created a game in which each player's hand is compared. The player with 
highest cards wins the game (without regard to the hand's suit).

3
"""

import random

def NUMBER_OF_PLAYERS():
    
    #find out number of players
    print('Please indicate the number of players: ')
    number_of_players = int(input('>> ')) 
    
    #accept name of each player in list
    #associate x-1 index in list with x being player number
    player_names = []    
    for x in range(0, number_of_players):
        print('Please enter the name of the player: ')
        player_names.append(str(input('>> ')))
    
    #create card list: 
    #{x][]outer index determines value of card in hand (2 value = 0, 3 value = 1)
    #[][x]inner list has four of each card and is a STRING
    cards = [ ['2','2','2','2'] , ['3','3','3','3'] , ['4','4','4','4'] , 
             ['5','5','5','5'] , ['6','6','6','6'] , ['7','7','7','7'] , 
             ['8','8','8','8'], ['9','9','9','9'] , ['10','10','10','10'] ,
             ['J','J','J','J'] , ['Q','Q','Q','Q'] , ['K','K','K','K'] , 
             ['A','A','A','A'] ]
    
    lengthc = len(cards) - 1
    
    winnername = ''
    winnerpoints = 0
    playernumber = 0
    
    #assign cards to each player 
    for x in player_names: 
            #create 5 entries in player hand using random.choice and append
            playerpoints = 0
            hand = ''
            numinhand = 0 #number of cards in player hand 
           
            while numinhand < 5: 
                cardnumselect = random.randint(0, lengthc) #select a random element number in cards
                cardselect = cards[cardnumselect][0] #choose that list element and one item from list
            
                hand = hand + (str(cardselect) + ', ') #add to hand list card
                  
                playerpoints = playerpoints + cardnumselect #give points to player based on index
                numinhand = numinhand + 1 #counts number in the hand, increments
        
            print(player_names[playernumber] + " has the hand: " + hand) #print out player hand
            
            if playerpoints > winnerpoints: #check for winner using points 
                winnerpoints = playerpoints 
                winnername = str(player_names[playernumber])
            
            playernumber = playernumber + 1
                
    print("The winner of the game is " + winnername )
        
    
NUMBER_OF_PLAYERS()
