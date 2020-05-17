matrix=[['-','-','-'],
          ['-','-','-'],
          ['-','-','-']]

count=0
def display_board():
  global matrix
  print (matrix[0],"   ","1 | 2 | 3")
  print (matrix[1],"   ","4 | 5 | 6")
  print (matrix[2],"   ","7 | 8 | 9")
#hand,hand1


'''def play_game():
    hand1=False
    while hand1==False:
      change_hand()
      check()'''


def player1():
  #matrix
  global matrix
  global count
  print("")
  print("choose from 1-9")
  position=int(input("enter position to put X"))
  print(position)
  if position==1:
    if matrix[0][0]!='-':
      print("position taken,choose other")
      player1()
    else:
      matrix[0][0]="X"
      #print(matrix[0][0])
  if position==2:
    if matrix[0][1]!='-':
      print("position taken,choose other")
      ##rint("")
      player1()  
    else:
      matrix[0][1]="X"             
  if position==3:
    if matrix[0][2]!='-':
      print("position taken,choose other")
      player1()
    else:
      matrix[0][2]='X'
  if position==4:
    if matrix[1][0]!='-':
      print("position taken,choose other")
      player1()
    else:
      matrix[1][0]='X'
  if position==5:
    if matrix[1][1]!='-':
      print("position taken,choose other")
      player1()
    else:
      matrix[1][1]='X'
  if position==6:
    if matrix[1][2]!='-':
      print("position taken,choose other")
      player1()
    else:
      matrix[1][2]='X'
  if position==7:
    if matrix[2][0]!='-':
      print("position taken,choose other")
      player1()   
    else:
      matrix[2][0]='X'
  if position==8:
    if matrix[2][1]!='-':
      print("position taken,choose other")
      player1()
    else:
      matrix[2][1]='X'
  if position==9:
    if matrix[2][2]!='-':
      print("position taken,choose other")
      player1()
    else:
      matrix[2][2]='X' 
  '''print(matrix[0])
  print(matrix[1])
  print(matrix[2])'''
  count+=1
  check()
  return


def player2():
  global matrix
  global count
  #if '-' in matrix:
  print("choose from 1-9")
  position=int(input("enter position to put O"))
  if position==1:
    if matrix[0][0]!='-':
      print("position taken,choose other")
      player2()
    else:
      #matrix[0][0]='x'
      matrix[0][0]="O"
  if position==2:
    if matrix[0][1]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[0][1]="O"             
  if position==3:
    if matrix[0][2]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[0][2]='O'
  if position==4:
    if matrix[1][0]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[1][0]='O'
  if position==5:
    if matrix[1][1]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[1][1]='O'
  if position==6:
    if matrix[1][2]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[1][2]='O'
  if position==7:
    if matrix[2][0]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[2][0]='O'
  if position==8:
    if matrix[2][1]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[2][1]='O'
  if position==9:
    if matrix[2][2]!='-':
      print("position taken,choose other")
      player2()
    else:
      matrix[2][2]='O' 
  '''print(matrix[0])
  print(matrix[1])
  print(matrix[2])'''
  count+=1
  check()
  return
  

'''def change_hand():
  hand=False
  while hand==False:      
    player1()
    player2()
  return'''


def check():
  #hand
  global count
  global matrix
  global hand
  if (matrix[0][0]==matrix[0][1]==matrix[0][2]=='X' or
      matrix[1][0]==matrix[1][1]==matrix[1][2]=='X' or
      matrix[2][0]==matrix[2][1]==matrix[2][2]=='X' or
      matrix[0][0]==matrix[1][0]==matrix[2][0]=='X' or
      matrix[0][1]==matrix[1][1]==matrix[2][1]=='X' or
      matrix[0][2]==matrix[1][2]==matrix[2][2]=='X' or
      matrix[0][0]==matrix[1][1]==matrix[2][2]=='X' or
      matrix[0][2]==matrix[1][1]==matrix[2][0]=='X'): 
        print("")
        print("player1 wins=X")
        print("")
        display_board()
        #hand=True
        exit()
  if (matrix[0][0]==matrix[0][1]==matrix[0][2]=='O' or
      matrix[1][0]==matrix[1][1]==matrix[1][2]=='O' or
      matrix[2][0]==matrix[2][1]==matrix[2][2]=='O' or
      matrix[0][0]==matrix[1][0]==matrix[2][0]=='O' or
      matrix[0][1]==matrix[1][1]==matrix[2][1]=='O' or
      matrix[0][2]==matrix[1][2]==matrix[2][2]=='O' or
      matrix[0][0]==matrix[1][1]==matrix[2][2]=='O' or
      matrix[0][2]==matrix[1][1]==matrix[2][0]=='O'):
        print("")
        print("player1 wins=O")
        print("")
        display_board()
        exit()
  elif count==9:
    print("NO ONE WINS")
    display_board()
    exit()

  else:
    print("game continues")
    print("")
    print("")
    return

'''def main():
  hand=False
  while hand==False:
    display_board()
    player1()
    check()'''

print("________GAME STARTS ________")
print("")
print("")
def main():
  hand=False
  while hand==False:
    display_board()
    player1()
    display_board()
    player2()
  return

if __name__=="__main__":
  main()
