print ("TIC TAC TOE board. Rows and Columns starting from 1,1")
print ("Game board is printed each time to show progress!")
import sys
# Declare the blank game           
game=[[0,0,0], 
      [0,0,0],
      [0,0,0]]
      
count = 0

# create the print gameboard function
def print_game(game):
    print ("\n")
    for i in range(3):
        print (str(game[i]) + "\n")

# Insert the checkWin function here.
def checkwin():
  if game[0][0] == game[0][1] == game[0][2]:
    player=game[0][0]
  elif game[1][0] == game[1][1] == game[1][2]:
    player=game[1][0]
  elif game[2][0] == game[2][1] == game[2][2]:
    player=game[2][0]
  elif game[0][0] == game[1][0] == game[2][0]:
    player=game[0][0]
  elif game[0][1] == game[1][1] == game[2][1]:
    player=game[0][1]
  elif game[0][2] == game[1][2] == game[2][2]:
    player=game[0][2]
  elif game[0][0] == game[1][1] == game[2][2]:
    player=game[0][0]
  elif game[0][2] == game[1][1] == game[2][0]:
    player=game[0][2]
  else:
    print ("YOU BOTH SUCK")
  if player == 'X':
    print ("player 1 wins!")
    print ("game over!")
    sys.exit()
  if player == 'O':
    print ("player 2 wins!")
    print ("game over!")
    sys.exit()
  
# Now lets start the game
while True:
  #Insert the code from Step 4
  spot = input("Enter the row,column in same format as given: ")
  spot = spot.split(",") # This will remove the comma
  row = int(spot[0]) -1    
  column = int(spot[1]) -1
  if count%2==0:
    print ("\nPlayer 1's Turn!")
    if game[row][column] == 0:  # Make sure the spot is blank
      game[row][column] = 'X'   # if it's blank, mark an X
    else:
      print ("Try Again!")      # if it's not blank, try again
      count-=1   # this will reset the counter, so you can try again
    print_game(game)  # print your new game board
  else:
    print ("\nPlayer 2's Turn!")
    if game[row][column] == 0:  # Make sure the spot is blank
      game[row][column] = 'O'   # if it's blank, mark an X
    else:
      print ("Try Again!")      # if it's not blank, try again
      count-=1   # this will reset the counter, so you can try again
    print_game(game)
  count +=1
  checkwin()
