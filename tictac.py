
board = ['']*9
turn = True
moves = 0


def validMove(position):
    if(position >= 0 and position <= 9 and board[position] == ''):
        return True
    
    return False

def consumeMove(turn, position):
    if(turn):
        board[position] = 'X'
    else:
        board[position] = 'O'

def tieSituation():
    if(moves >= 9):
        print('Match is a Tie')
        return True
    return False

def checkColumns():
    if((board[0] == board[3] == board[6] and board[0] != '') or (board[1] == board[4] == board[7] and board[1] != '') or (board[2] == board[5] == board[8] and board[2] != '')):
        return True
    return False

def checkRows():
    if((board[0] == board[1] == board[2] and board[0] != '') or (board[3] == board[4] == board[5] and board[3] != '') or (board[6] == board[7] == board[8] and board[6] != '')):
        return True
    return False

def checkDiagonals():
    if((board[0] == board[4] == board[8] and board[0] != '') or (board[2] == board[4] == board[6] and board[2] != '')):
        return True
    return False

def isGameOver():
    if(checkColumns() or checkRows() or checkDiagonals()):
        return True
    return False

def winningSituation(turn):
    if(isGameOver()):
        if(turn):
            print('Player 2 has won')
        else:
            print('Player 1 has won')
            
        return True
    return False


def resetGame():
    global board,turn,moves
    board = ['']*9
    turn = True
    moves = 0
    initGame()

def displayBoard():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n')
    print('------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n')
    print('------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')
    


def initGame():
    global turn,moves
    print('Would you like to have first turn')
    response = input('Yes/No');
    
    turn = True if response.lower() == 'yes' else False
    
    while(not winningSituation(turn) and not tieSituation()): #check board status
        displayBoard()
        if(turn):
            print('Player 1 please enter your move')
        else:
            print('Player 2 please enter your move')
        try:
            position = int(input())
        except ValueError:
            print('Please enter a number')
            continue
        
        if(not validMove(position)): #check validity of move
            print('Not a valid move!!')
            continue
        else:
            consumeMove(turn,position) #define a method for displaying board
            turn = not turn
            moves = moves + 1
    
    print('Do you want to replay? Yes/No')
    response = input()
    
    if(response.lower() == 'yes'):
        resetGame()
    else:
        return

initGame()
