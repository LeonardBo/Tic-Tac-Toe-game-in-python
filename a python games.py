import random

def displayBanner():
  print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
  print("O                              X")
  print("X         Tic Tac Toe          O")
  print("O                              X")
  print("XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO")
  print("")

grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

def displayGrid(grid):
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])


def player1():
    print("Player X: Your Turn!")
    row = int(input("Enter the row index: 0 , 1 or 2: "))
    col = int(input("Enter the col index: 0 , 1 or 2: "))
    while row > 2 or row < 0 or col > 2 or col < 0:
        print("Sorry you are out of index range... Try again!")
        row = int(input("Enter the row index: 0 , 1 or 2: "))
        col = int(input("Enter the col index: 0 , 1 or 2: "))
    else:
        while grid[row][col] != " "  :
            print("Sorry this cell is already taken... Try again!")
            row = int(input("Enter the row index: 0 , 1 or 2: "))
            col = int(input("Enter the col index: 0 , 1 or 2: "))
        else:
            grid[row][col] = "X"
    


def player2():
    print("Player O: Your Turn!")
    row = int(input("Enter the row index: 0 , 1 or 2: "))
    col = int(input("Enter the col index: 0 , 1 or 2: "))
    while row > 2 or row < 0 or col > 2 or col < 0 :
        print("Sorry you are out of index range... Try again!")
        row = int(input("Enter the row index: 0 , 1 or 2: "))
        col = int(input("Enter the col index: 0 , 1 or 2: "))
    else:
        while grid[row][col] != " ":
            print("Sorry this cell is already taken... Try again!")
            row = int(input("Enter the row index: 0 , 1 or 2: "))
            col = int(input("Enter the col index: 0 , 1 or 2: "))
        else:
            grid[row][col] ="O"

def calculator():
    print("Player O: Your Turn!")
    row = random.randint(0,2)
    col = random.randint(0,2)
    while grid[row][col]!=" ":
        print("Sorry this cell is already taken... Try again!")
        row = random.randint(0,2)
        col = random.randint(0,2)
    else:
        grid[row][col] ="O"

def checkGrid(grid):
    if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
        displayGrid(grid)
        print("Three Xs in a row.")
        exit()
    elif grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
        displayGrid(grid)
        print("Three Os in a row.")
        exit()
    if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
        displayGrid(grid)
        print("Three Xs in a row.")
        exit()
    elif grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
        displayGrid(grid)
        print("Three Os in a row.")
        exit()
    if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
        displayGrid(grid)
        print("Three Xs in a row.") 
        exit()
    elif grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
        displayGrid(grid)
        print("Three Os in a row.")
        exit()
    if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
        displayGrid(grid)
        print("Three Xs in a column.")
        exit()
    elif grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
        displayGrid(grid)
        print("Three Os in a column.")
        exit()
    if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
        displayGrid(grid)
        print("Three Xs in a column.")
        exit()
    elif grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
        displayGrid(grid)
        print("Three Os in a column.")
        exit()
    if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
        displayGrid(grid)
        print("Three Xs in a column.")
        exit() 
    elif grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
        displayGrid(grid)
        print("Three Os in a column.")
        exit()
    if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
        displayGrid(grid)
        print("Three Xs in diagonal")
        
    elif grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
        displayGrid(grid)
        print("Three Os in diagonal")
        exit()
    if grid[0][2]=="X" and grid[1][1]=="X" and grid[2][0]=="X":
        displayGrid(grid)
        print("Three Xs in diagonal")
        exit()
    elif grid[0][2]=="O" and grid[1][1]=="O" and grid[2][0]=="O":     
        displayGrid(grid)
        print("Three Os in diagonal")
        

def start():
    print("If you want to play with player press 'y' otherwise press 'n' and you are playing with calculator")
    print("[y/n]")
    choise = input()
    displayGrid(grid)
    if choise == "y":
        for i in range(0, 5, 1):
            if i <= 5:
                player1()
                checkGrid(grid)
                displayGrid(grid)
            else:
                print("Equal")
            if i < 4:
                player2()
                checkGrid(grid)
                displayGrid(grid)
            else:
                print("Equal")

    elif choise == "n":
        for i in range(0, 5, 1):
            if i <= 5:
                player1()
                checkGrid(grid)
                displayGrid(grid)
            else:
                print("Equal")
            if i < 4:
                calculator()
                checkGrid(grid)
                displayGrid(grid)
            else:
                print("Equal")

displayBanner()
start()
restart = input("Do you want to restart? (y/n): ")
if restart == "y":
    displayBanner()
    start()
elif restart == "n":
    quit()