# The goal of this project is to create a working sudoku solver
# This solution will implement recustion to solve the board

# Attempting a Gui
import sys
import pygame

# import pandas as pd

# This function takes in a 2D array and will print is as a sudoku board
def print_board(board):
    for row in range(0, len(board)):
        for col in range(0, len(board)):
            # prints the boarder for the right side of the board
            if col == 0:
                print("|", end=" ")
            # Prints the boarder for the right side of the board
            if col == 8:
                endline = " |\n"
            elif (col + 1) % 3 == 0:
                endline = "|"
            elif (row + 1) % 3 == 0:
                endline = "_"
            else:
                endline = " "
            if board[row][col] == 0:
                print(" ", end=endline)
            else:
                print(board[row][col], end=endline)


# This function takes in a postion and a number and returns weather the placement is valid
def valid(board, row, col, number):
    # Checks to see if that number shares a row
    for i in range(0, len(board)):
        if board[row][i] == number and col != i:
            print("in the same row")
            return False
    # checks to see if that number shars a col
    for j in range(0, len(board)):
        if board[j][col] == number and row != j:
            print("in the same col")
            return False
    # This is the logic used to check if the nuber shares a box
    x = (col // 3) * 3
    y = (row // 3) * 3
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if board[i][j] == number:
                print(board[i][j])
                print("in the same box")
                return False
    return True


def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return (row, col)
    return None


def solve(board):

    empty_position = find_empty(board)

    # If no more empty positions return true
    if not empty_position:
        return True
    else:
        row, col = empty_position

    for num in range(1, 10):
        if valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True
            board[row][col] = 0
    return False


def drawGrid(screen, board):
    x = 0
    y = 0
    for row in range(0, len(board)):
        for col in range(0, len(board)):
          if x % 15==0:
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 50), 5)
          if y % 15 ==0:
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x+50 , y), 5)
            # pygame.display.flip()
          if y+50 == 450:
            pygame.draw.line(screen, (0, 0, 0), (x, y+50), (x+50 , y+50), 5)
          if board[row][col] != 0:
            display_num((x,y),board[row][col])
          pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 50), 3)
          pygame.draw.line(screen, (0, 0, 0), (x, y), (x+50 , y), 3)
          x+=50
          if x == 450:
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + 50), 5)
        y = y + 50
        x = 0
    
        
        
def display_num(position, num):
        '''Displays a number on that tile'''
        font = pygame.font.SysFont('arial', 50)
        num = font.render(str(num), True, (0, 0, 0))
        screen.blit(num, position)

class cursor:

  def __init__(self):
    self.x = 25
    self.y = 45
    self.row = 0
    self.col = 0

  def shift_right(self):
    if self.x + 50 >450:
      self.x +=0
    else:
      self.x += 50
      self.col +=1
    
  def shift_left(self):
    if self.x - 50 <0:
      self.x +=0
    else:
      self.x -= 50
      self.col -=1

    
  def shift_up(self):
    if self.y - 50 <0:
      self.y +=0
    else:
      self.y -= 50
      self.row -=1


  def shift_down(self):
    if self.y + 50 >450:
      self.y +=0
    else:
      self.y += 50
      self.row +=1

  def get_coords(self):
    x = self.col
    y = self.row
    return(x,y)
      
  def show_cursor(self,screen):
    pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (self.x + 15, self.y), 3)
    pygame.display.update()

def fill_pos(cursor,event,board):
  if event.key == pygame.K_0 or event.key == pygame.K_KP0:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 0

  if event.key == pygame.K_1 or event.key == pygame.K_KP1:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 1

  if event.key == pygame.K_2 or event.key == pygame.K_KP2:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 2

  if event.key == pygame.K_3 or event.key == pygame.K_KP3:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 3

  if event.key == pygame.K_4 or event.key == pygame.K_KP4:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 4

  if event.key == pygame.K_5 or event.key == pygame.K_KP5:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 5

  if event.key == pygame.K_6 or event.key == pygame.K_KP6:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 6

  if event.key == pygame.K_7 or event.key == pygame.K_KP7:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 7

  if event.key == pygame.K_8 or event.key == pygame.K_KP8:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 8

  if event.key == pygame.K_9 or event.key == pygame.K_KP9:  
              x_pos, y_pos = cursor.get_coords()
              board[y_pos][x_pos] = 9
  
              
def valid_guess(pos,event,board,screen):
  if event.key == pygame.K_KP_ENTER:
    #TODO: Valid changes the board. change so that they return stuff
    x,y = pos.get_coords()  
    guess= board[y][x]
    board[y][x] = 0     
    if (valid(board,y,x,guess)):
      print("Valid")
      board[y][x] = guess
    else: 
      print("Not valid")
      board[y][x] = 0
      pygame.draw.line(screen, (0,0,0),(50,50),(0,100),8)     


board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7],
    ]
pygame.init()



if __name__ == "__main__":
    
    

    # Creating the screen

    # print("#" * 8 + " Original Board " + "#" * 8)
    # print_board(board)
    # print("#" * 8 + " Sovled Board " + "#" * 8)

    #solve(board)

    #this will constaly print the board to the terminal
    print_board(board)
    
    
    # Intalizing other things in pygame
    size = width, height = 500, 500

    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Sudoku")
    pygame.mouse.set_visible(1)

    pygame.display.set_caption("Test")
    # Intalizing the bakground
    background = pygame.Surface(size)
    background = background.convert()
    background.fill((250, 250, 250))

    #Trying to initalize a cursor
    pos = cursor()

    running = True
    while running:
        pygame.time.delay(100)
        screen.fill((255, 255, 255))
        events = pygame.event.get()
        for event in events:
          
            # If the escape key is hit exit the gui
          if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
            
            if event.key == pygame.K_LEFT:
              pos.shift_left()
              
            if event.key == pygame.K_RIGHT:
              pos.shift_right()

            if event.key == pygame.K_UP:
              pos.shift_up()
              
            if event.key == pygame.K_DOWN:
              pos.shift_down()
            (x,y)=pos.get_coords()
            print(x,y,board[y][x])
            fill_pos(pos,event,board)
            pygame.time.delay(100)
            valid_guess(pos,event,board,screen)

            # Creating the white background
          
          drawGrid(screen, board)
          pos.show_cursor(screen)
          pygame.display.update()
         

            # drawGrid(screen)
    pygame.quit()
