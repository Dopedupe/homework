MAX_N = 20
FREE = 0
BUSY = 1
ATTACKED = 2
IS_FINDED = 0 #флаг, что хоть одна расстановка найдена (= кол-во расстановок)

def print_board(chessboard: list, n: int) -> None: #вывод доски в консоль
    for x in range(0, n):
        for y in range(0, n):
            if chessboard[x][y] == FREE:
                print("0 ", end="")
            if chessboard[x][y] == BUSY:
                print("# ", end="")
            if chessboard[x][y] == ATTACKED:
                print("* ", end="")
        print()
    print()   

def set_attacked(chessboard: list, x: int, y: int, n: int) -> None:  
    for i in range(-2, 3, 1):           #устанавливаем атаку на диагоналях
        if i == 0:
            continue
        if x + i >= 0 and y + i >= 0 and x + i < n and y + i < n:
            chessboard[x + i][y + i] = ATTACKED
        if x + i >= 0 and y - i >= 0 and x + i < n and y - i < n:
            chessboard[x + i][y - i] = ATTACKED

    for i in range(-3, 4, 6):           #устанавливаем атаку на прямых
        if x + i >= 0 and x + i < n:
            chessboard[x + i][y] = ATTACKED
        if y + i >= 0 and y + i < n:
            chessboard[x][y + i] = ATTACKED


def output(chessboard: list, n: int, output_file ) -> None:     #вывод расстановки в файл
    for x in range(0, n):
        for y in range(0, n):
            if chessboard[x][y] == BUSY:
                output_file.write("({0},{1}) ".format(x, y))
    output_file.write("\n")
    


def search_solutions(chessboard: list, n: int, l: int, k: int, x_prev: int, y_prev: int, output_file ) -> None:
    global IS_FINDED
    board = [[0] * MAX_N for i in range(MAX_N)] #доп. доска
    for x in range(x_prev, n):  #начинаем проходить по полям с прошлой итерации (или с начальной 0 0), ищем свободное поле
        y1 = y_prev if x == x_prev else 0   
        for y in range(y1, n):              
            if chessboard[x][y] == FREE:    #если поле свободно, то
                for x1 in range(0, n):      #копируем доску в доп. доску
                    for y1 in range(0, n):
                        board[x1][y1] = chessboard[x1][y1]
                board[x][y] = BUSY  #занимаем поле
                set_attacked(board, x, y, n)    #отмечаем поля, находящиеся под ударом
                if k + 1 == l:  #если кол-во расставленных фигур равно L, то
                    output(board, n, output_file) #вывод расстановки в файл
                    IS_FINDED += 1   #флаг, что хоть одна расстановка найдена
                    if IS_FINDED == 1:
                        print_board(board, n)   #вывод доски в консоль
                else:
                    search_solutions(board, n, l, k+1, x, y, output_file) #вызов ф-ции для следующей установки фигуры

def main():
    output_file = open("output.txt", mode="w"); #для очищения файла вывода
    output_file.close()
    
    global IS_FINDED
    N: int  #размер доски
    L: int  #сколько фигур нужно еще расставить
    K: int  #сколько фигур уже расставлено
    chessboard = [[0] * MAX_N for i in range(MAX_N)]

    with open("input.txt", "r") as input_file:
        strings = input_file.readlines(1)
        N = int(strings[0].split(" ")[0])
        L = int(strings[0].split(" ")[1])
        K = int(strings[0].split(" ")[2])
        strings = input_file.readlines()
        for i in range(0, K):   #ввод начальной расстановки из файла
            x = int(strings[i].replace("\n","").split(" ")[0])
            y = int(strings[i].replace("\n","").split(" ")[1])
            if L == 0:  #если L == 0, то выводим в файл начальную расстановку
                IS_FINDED = 1
                with open("output.txt", mode="a") as output_file:
                    output_file.write("({0},{1}) ".format(x, y))
            chessboard[x][y] = BUSY #занимаем поле
            set_attacked(chessboard, x, y, N)   #отмечаем поля, находящиеся под ударом

    with open("output.txt", mode="a") as output_file:   #открываем файл для вывода перед вызовом рекурсивной функции
        
        if L == 0:
            print_board(chessboard, N) 
        else:
            search_solutions(chessboard, N, L, 0, 0, 0, output_file) #поиск всех возможных расстановок
    
    if IS_FINDED == 0:  #если расстановки не найдены, вывод no solutions
        with open("output.txt", "w") as output_file:
            output_file.write("no solutions")
    
if __name__ == "__main__":
    main()