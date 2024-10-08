from colorama import Fore
import random

def display_board(board):
    for row in board:
        for cell in row:
            print(f"{cell} |",end=" ") 
        print()

def is_vaild_move(board,row,col):
    return board[row][col] == ' '

def place_move(board,row,col,player):
    board[row][col] = player

def is_board_full(board):
    for row in board :
        for cell in row:
            if cell == ' ':
                return False
    return True
    
def is_winer(board,player):
    winer_serial = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]

    for i in winer_serial:
        if all(board[x][y] == player for x,y in i):
            return True
    return False
    
def main():  
    board = [[' ' for _ in range(3) ] for _ in range(3)]
    print("Game Start now :-")
    print("--------------------------------------------")
    
    print("Player 1 -> O")
    print("Player 2 -> X")

    player  = 'O'

    while True: 
        player_no = 1 if player == 'O' else 2
        print(Fore.YELLOW + f"\nTurn for player {player_no}\n" + Fore.RESET)
    
        while True :
            if player_no == 2:
                row = random.randint(0,2)
                col = random.randint(0,2)
            
            else :
                row = int(input("Enter the row:- "))
                col = int(input('Enter the column:- '))

                row = row - 1
                col = col - 1

            if is_vaild_move(board,row,col):
                place_move(board,row,col,player)
                break

            else :
                print(Fore.RED + "This place is already use! Enter the other place !\n" + Fore.RESET)
            
        display_board(board)

        if is_winer(board,player):
            print(Fore.GREEN + f"Player {player_no} wins!" + Fore.RESET)
            break

        elif is_board_full(board):
            print(Fore.GREEN + "It is a tie game" + Fore.RESET)
            break

        player = 'O' if player == 'X' else 'X'

main()
