
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:56:49 2018

@author: karinadandia

TIC TACK TOE GAME
in a nutshell, the tic-tac-toe board can be thought of 3 lists inside another one

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

por ejemplo, si queremos ver cual es el estado de la casilla de arriba a la 
izquerda, podemos acceder haciendo tablero[[0,0]]

We have 2 players, and each player will alternate in choosing a different slot on the board,
and placing either an "X"  (player 1) or "O" (player 2)

The game will have to validate that the new coordinates chosen by the current player 
are valid, i.e., they need to be empty and be inside the board.


Hint: You can use a deque (in the module collections) to rotate between player 1 and 2

"""

#collections.deque 

def game():
    
    pboard = [] #empty player board list 
    
    for x in range (0, 9): #add to player board availible spot numbers
        pboard.append(str(x + 1))
        
    p1turn = True
    winner = False
    
    while winner == False:
        
        #print userboard aka tic tac toe board
        #example: pboard[0] will print 1 for selecting position 1 spot if available 
        print ( '\n -----')
        print ( '|' + pboard[0] + '|' + pboard[1] + '|' + pboard[2] + '|')
        print ( '\n -----')
        print ( '|' + pboard[3] + '|' + pboard[4] + '|' + pboard[5] + '|')
        print ( '\n -----')
        print ( '|' + pboard[6] + '|' + pboard[7] + '|' + pboard[8] + '|')
        print ( '\n -----')
        
        #prompt correct player number 
        if p1turn == True:
            print( "Player 1: ")
        else: 
            print( "Player 2: ")
        
        try: #pull user input and convert from string to int
            uinput = int(input(">> "))
            
        except: 
            print("Invalid input. Please enter a valid number")
            continue 
        
        #check to see if spot available 
        if pboard[uinput - 1] == 'X' or pboard[uinput - 1] == 'O':
            print("This is already taken. Please try another location")
            continue 
        
        #fill designated player's spot with their symbol
        if p1turn == True:
            pboard[uinput - 1] = 'X'
        else: #player 2 turn
            pboard[uinput - 1] = 'O'
            
        p1turn = not p1turn #change p1turn boolean 
        
        #check for winning
        #y takes care of horizontal combinations 
        #x takes care of vertical combinations
        for x in range (0, 3):
            y = x * 3 
            if ( (pboard[y] == pboard [(y+1)]) and (pboard[y] == pboard[(y+2)])):
                print ( '\n -----')
                print ( '|' + pboard[0] + '|' + pboard[1] + '|' + pboard[2] + '|')
                print ( '\n -----')
                print ( '|' + pboard[3] + '|' + pboard[4] + '|' + pboard[5] + '|')
                print ( '\n -----')
                print ( '|' + pboard[6] + '|' + pboard[7] + '|' + pboard[8] + '|')
                print ( '\n -----')
               
                winner = True
            
            if ( (pboard[x] == pboard[(x + 3)]) and (pboard[x] == pboard[(x + 6)])):
                print ( '\n -----')
                print ( '|' + pboard[0] + '|' + pboard[1] + '|' + pboard[2] + '|')
                print ( '\n -----')
                print ( '|' + pboard[3] + '|' + pboard[4] + '|' + pboard[5] + '|')
                print ( '\n -----')
                print ( '|' + pboard[6] + '|' + pboard[7] + '|' + pboard[8] + '|')
                print ( '\n -----')
               
                winner = True
                
        #check for winnning
        #takes care of diagonal combinations
        if ( ( (pboard[0] == pboard[4]) and (pboard[0] == pbaord[8]) ) or ( (
                pboard[2] == pboard[4]) and (pboard[4] == pboard[6]) ) ):
                print ( '\n -----')
                print ( '|' + pboard[0] + '|' + pboard[1] + '|' + pboard[2] + '|')
                print ( '\n -----')
                print ( '|' + pboard[3] + '|' + pboard[4] + '|' + pboard[5] + '|')
                print ( '\n -----')
                print ( '|' + pboard[6] + '|' + pboard[7] + '|' + pboard[8] + '|')
                print ( '\n -----')
               
                winner = True
                
    print( "Player " + str(int(p1turn + 1)) + " wins!\n")


if __name__ == "__main__": #do not touch 
    game()


