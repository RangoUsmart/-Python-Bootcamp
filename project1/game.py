q1="\nВиберіть значок гравець 1: "
q2="\nВведіть значок гравець 2: "
q3="\nБажаєте продовжити?(Yes/No): "
q4="\nВиберіть іншу клітинку :-): "
q5="\nВи починаєте гру, для виграшу потрібно зібрати хрестики або нулики відповідно вашого вибору в ряд: "
q6="\nВиберіть число: "

checkers_list = ["X", "O"]
analog =["Yes", "No"]
game_field1="___"
game_field2=["1","2","3","4","5","6","7","8","9"]
game_field3=["   "]

win_list=[[1,2,3],[1,4,7],
          [4,5,6],[2,5,8],
          [7,8,9],[3,6,9],
          [1,5,9],[3,5,7]]
player2_list=[]
def check_position(position, massive):
    # Перевіряємо, чи елемент за вказаною позицією `position` не дорівнює " "
    if massive[position] != " ":
        return False
    return True
    

def check_position(position, massive):
    if massive[position - 1] != " ":
        return False
    return position
    
def check_win(board):
    for triplet in win_list:
        if all(board[index - 1] in ['X'] for index in triplet):
            return True
        elif all(board[index - 1] in ['O'] for index in triplet):
            return True
    return False
    
def question(que, options=None):
    print(que)
    
    if options:
        print("Доступні варіанти відповідей:", ", ".join(map(str, options)))
        while True:
            user_input = input("Введіть вашу відповідь: ")
            if user_input in options:
                return user_input
            else:
                print("Будь ласка, введіть один із доступних варіантів відповідей.")
    # else:
    #     user_input = input("Введіть вашу відповідь: ")
    #     return user_input


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
    player1_list = [' '] * 9
    gamestatus = "Yes"

    player1 = question(q1, checkers_list)
    player2 = question(q2, checkers_list)

    question(q5)
    question(q3, analog)

    while gamestatus == "Yes":
        game_field(*player1_list)
        
        a = int(question(f"{q6} для гравця {player1}", game_field2))
        while player1_list[a - 1] != ' ':  # Перевірка на зайнятість клітинки
            print("Ця клітинка вже зайнята. Оберіть іншу.")
            a = int(question(f"{q6} для гравця {player1}", game_field2))
        
        player1_list[a - 1] = player1
        game_field(*player1_list)
        if check_win(player1_list):
            game_field(*player1_list)
            print("Ви виграли!")
            break
        
        b = int(question(f"{q6} для гравця {player2}", game_field2))
        while player1_list[b - 1] != ' ':  # Перевірка на зайнятість клітинки
            print("Ця клітинка вже зайнята. Оберіть іншу.")
            b = int(question(f"{q6} для гравця {player2}", game_field2))
        
        player1_list[b - 1] = player2
        game_field(*player1_list)
        if check_win(player1_list):
            game_field(*player1_list)
            print("Ви виграли!")
            break
        
        
        if all(cell != ' ' for cell in player1_list):
            game_field(*player1_list)
            print("Нічия!")
            break

        gamestatus = question(q3, analog)

        if gamestatus == "No":
            break

quest = logick()
