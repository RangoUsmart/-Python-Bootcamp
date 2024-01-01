q1="Введіть клітинку гравець 1: "
q2="Введіть клітинку гравець 2: "
q3="\nБажаєте продовжити?(Yes/No): "
game_field1="___"
game_field2=[1,2,3,4,5,6,7,8,9]
game_field3=["   "]

win_list=[[1,2,3],[1,4,7],
          [4,5,6],[2,5,8],
          [7,8,9],[3,6,9],
          [1,5,9],[3,5,7]]
player2_list=[]
def check_win(board):
    for triplet in win_list:
        if all(board[index - 1] in ['X', 'O'] for index in triplet):
            return True
    return False
    
def question(que):
    if (que==q1):
        user_input = input(q1)
        try:
            number = int(user_input)
            if(number>0 and number<10):
                return number
        except ValueError: 
            return 0 
    else:
        user_input = input(q2)
        if (user_input=="yes"):
            return 0
        else:
            return 1

def game_field(*cells):
    game_list = []
    k=0
    for i in range(9):      
            
        if ((i+1)%3==0 and i!=0 and i!=8):
            row=("_____")
            for j in range(5):
                if (j%2!=0 and j!=5):
                    game_list.append("|")
                else:                   
                    game_list.append(row) 
            game_list.append('\n') 
        elif (i==1 or i==4 or i==7):
            
            for j in range(5):
                if (j%2!=0 and j!=5):
                    game_list.append("|")
                else:
                    try:
                        if cells[k] != "":
                            # print(*cells[k])
                            row = f"  {cells[k]}  "
                        else:
                            row = "  X  "
                    except IndexError:
                        row = "     "
                    # print(k)
                    k=k+1
                    game_list.append(row)
            game_list.append('\n')
        else:
            row=("     ")
            for j in range(5):
                if (j%2!=0 and j!=5):
                    game_list.append("|")
                else:                   
                    game_list.append(row)
            game_list.append('\n') 
    for symbol in game_list:
        print(symbol, end='')
    
def answer(value):
    print("Ви ввели:", value)

def logick():
    # Оголошуємо набір для користувача
    player1_list = [' '] * 9
    # Тут можна вставити елемент для початку гри вивід поля з цифрами для розуміння, інструкції
    while True:
        game_field(*player1_list)
        a = question(q1)
        player1_list[a - 1] = 'X'
        if check_win(player1_list):
            game_field(*player1_list) 
            print("Ви виграли!")
            break
        game_field(*player1_list)
        gamestatus = question(q3)
        if gamestatus:
            break

quest = logick()
