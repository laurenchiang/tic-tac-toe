
#creating initial board
board = {'1': ' ','2': ' ','3': ' ','4': ' ','5': ' ','6': ' ','7': ' ','8': ' ','9': ' ' }
#keys
ttckeys = []

for key in board:
  ttckeys.append(key)
#print board definition
def showBoard(b):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
#main play definition
def play():
  print('\nWho wants to go first? (X or O)')
  first = input()
  player = first
  turncount = 0


  for x in range(10):
    
    
    print("\n" + player + "\'s turn")
    showBoard(board)
    move = input()
    if board[move] == ' ':
      board[move] = player
      turncount += 1
    else:
      print("\ninvalid, try again!")
      continue
    if(turncount > 4): ##if 5 turns or more, check if anyone won
      if (board['1'] == board['2'] == board['3'] != ' ' or board['4'] == board['5'] == board['6'] != ' ' or board['7'] == board['8'] == board['9'] != ' ' or board['1'] == board['4'] == board['7'] != ' ' or board['2'] == board['5'] == board['8'] != ' ' or board['3'] == board['6'] == board['9'] != ' ' or board['1'] == board['5'] == board['9'] != ' ' or board['3'] == board['5'] == board['7']!= ' ' ):
        showBoard(board)
        print("\n" + player + " won!")
        break
    if (turncount == 9): ##at turn 9 there is a tie if no one wins
      showBoard(board)
      print("Tie game!")
      break
    if player == 'X':
      player = 'O'
    else:
      player = 'X'
  #asks if player wants to play again
  print("\nPlay again? (y or n)")
  decision = input()
  if(decision == 'y' or decision == 'Y'):
    for key in ttckeys:
        board[key] = ' '
    play()
  else:
    print("\nbye!")

print("board's keys")
print('1 ' + '|' + ' 2 ' + '|' + ' 3')
print('-  ---  -')
print('4 ' + '|' + ' 5 ' + '|' + ' 6')
print('-  ---  -')
print('7 ' + '|' + ' 8 ' + '|' + ' 9')


play()

