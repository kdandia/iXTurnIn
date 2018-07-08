#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:33:30 2018

@author: karinadandia
"""

When initally starting the poker game, I was a bit nervous because I have never played poker in real life. However, after reading the directions I proceeded to code. 

First the user is asked to input how many players are in the game. For each player, the user is prompted to imput the players' names. This information is stored in a list, and the player names can easily be accessed using an index of the list. 

In order to assign cards to the poker game players, I created a list within the list that stores all the cards. Each sublist is a group of the same card to model how a card can be from four different suits. So the first sublist is [2,2,2,2] and is a list consisting of strings. Each subsequent sublist is a card with a higher power so the next sublist has four entries of 3. Because each sublist in the list is sequentially ordered and with increasing power, I used the list indeces to determine who had the winning hand. The outer index of the card list determines the value of the card in the hand cards[x][]. Since the list with 2s is the first entry in the cards list, it has a value of 0. The list of 3s has index and value 1, and so on for each sublist. 

For producing a hand for each player, I used a for loop to go through the players list. I used a while loop to assign each card to a player's hand one at a time. The cards list was easily accessed using the indeces method mentioned above and the random funtion. After a player was assigned a hand, it was printed out. Based on the player's hands, I added up the indeces of each card in order to create points for each player to evaluate which player had the winning hand. I created a variable that would keep track of which player had the winning hand and it would get updated through the for loop based on the new hands created for each player. 

The game outputs a winner based on whichever player has the highest amount of points, meaning they have the hand that with the highest valued cards.     

For the future, in order to improve the game I could add in the complexity of assigning a suit to each card. I could do this by making each index in the sublist of cards equal to a suit. So for the list [2,2,2,2] the first index 0 could be for spades, the second index 1 could be for hearts and so on. When checking for the winning hands I could pull the index to check the suit the card belongs to. 