board = [" " for x in range(9)]                      #BOARD TEMPLATE
def print_board():       
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print("-------------")
    print(row2)
    print("-------------")
    print(row3)
    print()

acceptable_input_token=['x','o','X','O']
acceptable_play_states=['yes','no','Yes','No','y','n','N','Y']
valid_positions=['1','2','3','4','5','6','7','8','9']

def check_win_or_fail(board,p1):         #CHECK STATUS IF WON/LOSS/DRAW
  turn2=''
  if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
     print("X WINS")
     while turn2 not in acceptable_play_states or turn2.isdigit()==True:
      turn2=input("Replay? Yes/No:")            #to replay
      if(turn2=='Yes' or turn2=='y' or turn2=='yes' or turn2=='Y'):
        board[:] = [" " for x in range(9)] 
        user_input_token()
      else:
        print("GAME ENDED")
        return True
  elif (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[4] == 'X' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
     print("O WINS")
     while turn2 not in acceptable_play_states or turn2.isdigit()==True:
      turn2=input("Replay? Yes/No:")            #to replay
      if(turn2=='Yes' or turn2=='y' or turn2=='yes' or turn2=='Y'):
        board[:] = [" " for x in range(9)] 
        user_input_token()
      else:
        print("GAME ENDED")
        return True
  elif(" " not in board):
    print("Its a DRAW")
    while turn2 not in acceptable_play_states or turn2.isdigit()==True:
      turn2=input("Replay? Yes/No:")            #to replay
      if(turn2=='Yes' or turn2=='y' or turn2=='yes' or turn2=='Y'):
        board[:] = [" " for x in range(9)] 
        user_input_token()
      else:
        print("GAME ENDED")
        return True
  else:
    if(p1=='X' or p1=='x'):
        p1='O'
        enter_position('yes',p1)       
    else:
        p1='X'
        enter_position('yes',p1)  

def replace_token(board,position,p1):           #ADD THE X/O TOKEN IN THE BOARD
  if(board[position-1]=='X' or board[position-1]=='O'):
    print("Position aldready filled!")
    enter_position('yes',p1)
  board[position-1]=p1.upper()
  # return board
  print_board()
  check_win_or_fail(board,p1)

def enter_position(status,p1):                   #ENTER POSITON FOR THE TOKEN X/O
  updated_list=False
  position=''
  while(position.isdigit()== False or position not in valid_positions and updated_list==False):
    print("PLAYER ",p1)
    position=input("Enter a valid position (1-9): ")
  updated_list=replace_token(board,int(position),p1)  #result to be stored or printed
  turn=''
  while turn not in acceptable_play_states and updated_list==False:
    turn=input("Play Again? Yes/No:")
    if(turn=='Yes' or turn=='y' or turn=='yes' or status=='Y'):                       #to start the game
      if(p1=='X' or p1=='x'):
        p1='O'
        enter_position(turn,p1)       
      else:
        p1='X'
        enter_position(turn,p1)              
    else:
      print("Game Ended")        

def user_input_token():                       #CHOOSING THE TOKEN                    
  print("Welcome to TIC-TACK-TOE")
  p1='8'
  while p1.isalpha() == False or p1 not in acceptable_input_token:
    p1=input("Player 1: Do you want to be X or O: ")
    if p1.isalpha()== False or p1 not in acceptable_input_token:
      print("Sorry wrong input, either X or O")
    else:
      if(p1=='X' or p1=='x'):
        print("Player 1 you may proceed")
      else:
        print("Since you are O, Player 2 goes First")
      status=''
      while status not in acceptable_play_states:
        status=input("Are you ready to play? Yes/No: ")
        if(status=='Yes' or status=='y' or status=='yes' or status=='Y'):
          print("Lets begin the game")
          enter_position(status,'X')                    #TO ENTER POSITION
        else:
          print("Game Ended")
        

user_input_token()