replay_phrases=['OK','OKAY',"HUSS","HUSH",'OKEY','HUNCHA']    #created some lists of nepali phrases similar in meaning to yes

def printboard(board):#function to print full board
    print()
    print('-'*26)
    print(' ',"|",board[1],"|",'  ',"|",board[2],"|",'  ',"|",board[3],"|")
    print('-'*26)
    print(' ',"|",board[4],"|",'  ',"|",board[5],"|",'  ',"|",board[6],"|")
    print('-'*26)
    print(' ',"|",board[7],"|",'  ',"|",board[8],"|",'  ',"|",board[9],"|")
    print('-'*26)
    print()
    
    
#function to check whether board is full or not and return value in boolean
def board_is_full_check(board):
    if ' ' not in board:
        return True
    if ' ' in board:
        return False

def is_win(board, mark):   #function to check if anyone has won the game and return boolean
    if board[1]==board[2]==board[3]==mark: #row1
        return True
    elif board[4]==board[5]==board[6]==mark: #row2
        return True
    elif board[7]==board[8]==board[9]==mark:  #row3
        return True
    elif board[1]==board[4]==board[7]==mark: #col1
        return True
    elif board[2]==board[5]==board[8]==mark: #col2
        return True
    elif board[3]==board[6]==board[9]==mark: #col3
        return True
    elif board[1]==board[5]==board[9]==mark: #diagonal1
        return True
    elif board[3]==board[5]==board[7]==mark: #diagonal2
        return True
   

def choosemarker():  #function to allow first player to choose marker
    '''used to just assign certain marker to player'''
    global marker1,marker2    #calling the global variables for marker
    marker1=input('\nhey '+player1+", Say which marker you want to use?(x/o):   ").upper()
    while marker1!="X" and marker1!="O":    #correcting user to input correct marker
        print("'{}' marker is unavailable".format(marker1))
        marker1=input('\nhey '+player1+", Say which marker you want to use?(x/o):   ").upper()
    if marker1=="X":
        marker2="O"  #no need to re-enter marker for another player
    elif marker1=="O":
        marker2="X"
    print()
    print(player1+' will use: '+marker1)
    print(player2+' will use: '+marker2)
    print()
    
def isavailable(board,place):        #function to check space availability
    '''input: boardlist name  and place to place the marker
    output: boolean(true if place is available, false if place is not available)'''
    try :
        place=int(place)   #if converting into integer is possible then carry so
        if place not in range(1,10):
            return False
        elif "X" in board[place] or "O" in board[place]:    #checking whether the place is empty or not
            return False
        elif "X" and "O" not in board[place]:
            return True
    except:    #correcting user from inputting a non integer
        return False
    

def markerplacer(board,insert_to_place,marker):     #function to place marker to desired place
    board[int(insert_to_place)]=marker
    
#program starts here

program_active=True                  #declaring a program active variable

print('\t\t\t\tWelcome to TIC-TAC-TOE')
print('\t\t\t\t'+'='*22)
print()
print()
player1=input('who will be player 1?').capitalize()
player2=input('So, player 2 is: ').capitalize()
marker1='none'
marker2='none'


while program_active:
    choosemarker()
    board_list=['zeroth value']+[' ']*9     #creating list for creating board
    printboard(board_list)
    while ' ' in board_list:     #while space is still available
        print("It's {}'s turn".format(player1))
        print(player1,", Choose where you want to place marker: '{}'".format(marker1))
        place=input()
        while not isavailable(board_list,place):
            print("'{}' Place is not available\n".format(place))
            print(player1,", Choose where you want to place marker: '{}'".format(marker1))
            place=input()
        
        markerplacer(board_list,int(place),marker1)
        printboard(board_list)
        if is_win(board_list,marker1):
            print("{} wins".format(player1))
            break
        else:
            pass
        if board_is_full_check(board_list):         #full board checkup
            if not is_win(board_list,marker1) and not is_win(board_list,marker2):
                print('game is draw')
                break
            if is_win(board_list,marker1):
                print("{} wins".format(player1))
                break
            elif is_win(board_list,marker2):
                print("{} wins".format(player1))
                break
        print("It's {}'s turn".format(player2))
        print(player2,", Choose where you want to place marker: '{}'".format(marker2))
        place=input()
        while not isavailable(board_list,place):
            print("'{}' Place is not available\n".format(place))
            print(player2,", Choose where you want to place marker: '{}'".format(marker2))
            place=input()
        markerplacer(board_list,int(place),marker2)
        printboard(board_list)
        if is_win(board_list,marker2):
            print("{} wins".format(player2))
            break
        else:
            pass
        if board_is_full_check(board_list):   #checking whether space is full or not
            if not is_win(board_list,marker1) and not is_win(board_list,marker2):
                print('game is draw')
                break
            if is_win(board_list,marker1):
                print("{} wins".format(player1))
                break
            elif is_win(board_list,marker2):
                print("{} wins".format(player1))
                break
                
                
    #replay session            
    ask=input('\nReplay the game? \n')
    while not ask.upper().startswith("Y") and not ask.upper().startswith("N") and ask.upper() not in replay_phrases :
        print("'{}' was an invalid choice".format(ask))
        ask=input('play again?(y/n)\n')
    if ask.upper().startswith("Y") or ask.upper() in replay_phrases:
        pass
    else:
        print("\nThanks for playing   :)   ")
        program_active=False
                