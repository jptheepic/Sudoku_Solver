
#The goal of this project is to create a working sudoku solver 
#This solution will implement recustion to solve the board

#This function takes in a 2D array and will print is as a sudoku board
def print_board(board):
  for row in range(0,len(board)):
    for col in range(0,len(board)):
      #prints the boarder for the right side of the board
      if col ==0:
        print("|",end=' ')
      #Prints the boarder for the right side of the board
      if col ==8:
        endline = ' |\n'
      elif (col+1)%3 == 0:
        endline = "|"
      elif (row+1)%3 == 0:
        endline = "_"
      else:
        endline = " "
      if board[row][col] ==0:
        print(" ", end=endline)
      else:
        print(board[row][col], end=endline)

#This function takes in a postion and a number and returns weather the placement is valid 
def valid(board, row, col,number):
  #Checks to see if that number shares a row
  for i in range(0,len(board)):
    if (board[row][i] == number  and col != i):
      return False
  #checks to see if that number shars a col
  for j in range(0,len(board)) :
    if (board[j][col] == number and row != j):
      return False
  #This is the logic used to check if the nuber shares a box
  x = (col//3)*3
  y = (row//3)*3
  for i in range(y, y + 3):
    for j in range(x , x + 3):
      if (board[i][j] == number ):
        return False
  return True

def find_empty(board):
  for row in range(len(board)):
    for col in range(len(board)):
      if board[row][col] == 0:
        return (row,col)
  return None

def solve(board):

  empty_position = find_empty(board)
  
  #If no more empty positions return true
  if not empty_position:
    return True
  else:
    row, col = empty_position
  

  for num in range(1,10):
    if valid(board,row,col,num):
      board[row][col] = num
      

      if solve(board):
        return True
      board[row][col] = 0
  return False


        


if __name__ == '__main__':
  board =[
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]]
  print('#'*8 + " Original Board " +'#'*8)
  print_board(board)
  print('#'*8 + " Sovled Board " +'#'*8)

  solve(board)
  print_board(board)