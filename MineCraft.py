
import numpy as np
import random
import os

# number of row in game board
rowGameBoardNum = 7

# number of column in game board
columnGameBoardNum = 7

# number of bomb number
bombNumber = 7


# clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# check neighbors
def neighbor_checker(nh):
    
    bombAroundCounter = 0

    x = nh[0]
    y = nh[1]

    # get around neighbors
    aroundNeighborList = [[x-1,y-1 if x>0 and y>0 else None], 
                          [x-1,y if x>0 else None], 
                          [x-1,y+1 if x>0 and y<8 else None], 
                          [x,y-1 if y>0 else None],
                          [x,y+1 if y<8 else None], 
                          [x+1,y-1 if x<8 and y>0 else None], 
                          [x+1,y if x<8 else None], 
                          [x+1,y+1 if x<8 and y<8 else None]]


    for neighbor in aroundNeighborList:
        if neighbor in bombList:
            bombAroundCounter += 1
    
    return(bombAroundCounter)


# draw MineCraft GameBoard
def draw_gameBoard():
    # draw game map
    gameBoard = np.zeros((rowGameBoardNum, columnGameBoardNum)).astype(str)
    for i in range(rowGameBoardNum):
        for j in range(columnGameBoardNum):
            gameBoard[i,j] = 'O'

    return gameBoard


def get_bombList():
    bombList = []
    while len(bombList) < bombNumber:
        home = [random.randint(0,bombNumber),random.randint(0,bombNumber)]
        if home not in bombList:
            # print(home)
            bombList.append(home)
    
    return bombList



####################### Main Code ##################################

gameBoard = draw_gameBoard()
print(gameBoard)

bombList = get_bombList()

gameLeft = True
while gameLeft:

    try:

        print('*' * 50)
        print('Dear User. Please Enter Youe Selection. Ex-> 2,3')
        userSelection = input('Enter Your Home Selection: ')
        
        # Definition For Check User Input is true or False:
        userSelectionSpliter = userSelection.split(',')
        userSelectionSpliter = [int(userSelectionSpliter[0]) , int(userSelectionSpliter[1])]
        if int(userSelectionSpliter[0]) in range(0,7) and int(userSelectionSpliter[1]) in range(0,7):
            
            if userSelectionSpliter in bombList:
                print('Oh, The bomb Exploded!!!')
                gameBoard[userSelectionSpliter[0], userSelectionSpliter[1]] = 'B'
                print(gameBoard)
                quit()
            else:
                # Get main User Selection
                x = userSelectionSpliter[0]
                y = userSelectionSpliter[1]
                
                neigh_Counter = neighbor_checker(userSelectionSpliter)


                gameBoard[x,y] = neigh_Counter

                if neigh_Counter == 0:
                        for i in range(x-1, x+2):
                            for j in range(y-1, y+2):
                                neigh_Counter = neighbor_checker(userSelectionSpliter)
                                gameBoard[i,j] = neigh_Counter

                print(gameBoard)

        else:
            print('*' * 50)
            print('--> Please Insert Number in range 0 to 6 ...')                     
        
    except ValueError as e:
        print('*' * 50)
        print('Invalid input. Please try Again...')