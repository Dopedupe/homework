import sys
import pygame as pg 
from tkinter import *

MAX_N = 20
FREE = 0
BUSY = 1
ATTACKED = 2
IS_FINDED = 0 #флаг, что хоть одна расстановка найдена (= кол-во расстановок)

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
                    if IS_FINDED == 0:
                        IS_FINDED += 1          #флаг, что хоть одна расстановка найдена
                        window(n, board, 1)
                    output(board, n, output_file) #вывод расстановки в файл
                else:
                    search_solutions(board, n, l, k+1, x, y, output_file) #вызов ф-ции для следующей установки фигуры

def window(n: int, board: list, mode: int):
    pg.init()
    RES =  600, 650
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0,255,0)
    BLACK = (0,0,0)
    FPS = 60
    objects = []

    class Button():
        def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.onclickFunction = onclickFunction
            self.onePress = onePress
            self.alreadyPressed = False

            self.fillColors = {
                'normal': '#cccccc',
                'hover': '#666666',
                'pressed': '#333333',
            }
            self.buttonSurface = pg.Surface((self.width, self.height))
            self.buttonRect = pg.Rect(self.x, self.y, self.width, self.height)
            self.buttonSurf = pg.font.Font(None, 40).render(buttonText, True, (20, 20, 20))
            
            
            objects.append(self)

        def process(self):
            mousePos = pg.mouse.get_pos()
            self.buttonSurface.fill(self.fillColors['normal'])
            if self.buttonRect.collidepoint(mousePos):
                self.buttonSurface.fill(self.fillColors['hover'])

                if pg.mouse.get_pressed(num_buttons=3)[0]:
                    self.buttonSurface.fill(self.fillColors['pressed'])

                    if self.onePress:
                        self.onclickFunction()

                    elif not self.alreadyPressed:
                        self.onclickFunction()
                        self.alreadyPressed = True

                else:
                    self.alreadyPressed = False

            self.buttonSurface.blit(self.buttonSurf, [
                self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
                self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
            sc.blit(self.buttonSurface, self.buttonRect)

    def func():
        if mode == 1:
            solve()
        else:
            with open("output.txt", "w") as output_file:
                output_file.write("no solutions")
        exit()

    sc = pg.display.set_mode(RES)
    size = 600//n
    clock = pg.time.Clock()
    sc.fill(WHITE)
    customButton = Button(0, 600, 600, 50, 'Вывод', func)
    temp = []

    for x in range(0, n):
        for y in range(0, n):
            if board[x][y] == BUSY:
                temp.append("{0},{1}".format(x, y))
    while True:
        for event in pg.event.get():
            if mode == 1:
                for i in range(len(temp)):
                    x1, y1 = temp[i].split(',')
                    x1, y1 = int(y1), int(x1)
                    for x in range(0, n):
                        for y in range(0, n):
                            if x1 == x and y1 == y:
                                pg.draw.rect(sc, GREEN, (size * x, size * y, size, size))
                                pg.draw.rect(sc, BLACK, (size * x, size * y, size, size),1)    
                            else:
                                pg.draw.rect(sc, BLACK, (size * x, size * y, size, size),1)
                    for i in range(-2, 3, 1):           #устанавливаем атаку на диагоналях
                        if i == 0:
                            continue
                        if x1 + i >= 0 and y1 + i >= 0 and x1 + i < n and y1 + i < n:
                            pg.draw.rect(sc, BLUE, (size * (x1 + i), size * (y1 + i), size, size))    
                        if x1 + i >= 0 and y1 - i >= 0 and x1 + i < n and y1 - i < n:
                            pg.draw.rect(sc, BLUE, (size * (x1 + i), size *(y1 - i), size, size))     
                    for i in range(-3, 4, 6):           #устанавливаем атаку на прямых
                        if x1 + i >= 0 and x1 + i < n:
                            pg.draw.rect(sc, BLUE, (size * (x1 + i), size * y1, size, size))
                        if y1 + i >= 0 and y1 + i < n:
                            pg.draw.rect(sc, BLUE, (size * x1, size * (y1 + i), size, size))
            elif mode == 0:
                f1 = pg.font.Font(None, 44)
                text1 = f1.render('No solutions', 10, (255, 50, 50))
                place = text1.get_rect(center=(300,275))
                sc.blit(text1, place)
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        for object in objects:
            object.process()

        sc.blit(sc, (0, 0))
        pg.display.flip()
        clock.tick(FPS)

def solve():
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
            if x >= N or y >= N:    # no solutions
                window(N, chessboard, 0)
            if L == 0:  #если L == 0, то выводим в файл начальную расстановку
                IS_FINDED = 1
                break
            chessboard[x][y] = BUSY #занимаем поле
            set_attacked(chessboard, x, y, N)   #отмечаем поля, находящиеся под ударом

    with open("output.txt", mode="a") as output_file:   #открываем файл для вывода перед вызовом рекурсивной функции
        search_solutions(chessboard, N, L, 0, 0, 0, output_file) #поиск всех возможных расстановок
    
    if IS_FINDED == 0:  #если расстановки не найдены, вывод no solutions
        window(N, chessboard, 0)

def viewer():
    root = Tk()

    root.title("Шахматы")
    root.geometry("200x180")

    def clicker():
        N = int(a.entries[0].get())
        L = int(a.entries[1].get())
        K = int(a.entries[2].get())

        input_file = open("input.txt", mode="w"); #для очищения файла вывода
        input_file.close()
        with open("input.txt", "w") as input_file:
            input_file.write("{0} {1} {2}".format(N, L, K))

        root.destroy()

        second_window = Tk()
        second_window.title("Tesy")
        second_window.geometry("200x{0}".format(50*K+75)) # добавить второй столюик, если больше 10

        b = tkinter_input(second_window)

        def add_k():
            for i in b.entries:
                x, y = i.get().split(' ')
                with open("input.txt", mode="a") as input_file:
                    input_file.write("\n{0} {1} ".format(y, x)) 
            second_window.destroy()

        for i in range(1, K+1):
            b.add_label('Введите координаты:\n№{0}'.format(i), '2')
        b.add_button("Создать", add_k)

    def valid(new_value, val):
        if val == '1':
            try:
                return new_value[-1].isnumeric()
            except:
                return new_value == ''
        if val == '2':
            try:
                if new_value[-1].isnumeric():
                    return True
                elif new_value[-1].isascii() and new_value[-1] == ' ' and new_value.count(' ') <= 1:
                    return True
                else:
                    return False
            except:
                return new_value == ''

    class tkinter_input:
        def __init__(self, master):
            self.entries = []
            self.root = master
            myFrame = Frame(self.root)
            myFrame.pack()
            self.root.resizable(False, False)

        def add_label(self, text_labbel, val):
            self.lbl = Label(self.root, text=text_labbel)
            self.lbl_text = Entry(self.root, width=30, validate='key', validatecommand=(self.root.register(valid), '%P', val))
            self.lbl.pack()
            self.lbl_text.pack()
            self.entries.append(self.lbl_text)

        def add_button(self, text_button, func):
            self.myButton = Button(self.root, text = text_button, command=func)
            self.myButton.pack(pady=10)

    a = tkinter_input(root)
    a.add_label('Размер доски (N)', '1')
    a.add_label('Кол-во требуемых фигур (L)', '1')
    a.add_label('Кол-во размещенных фигур (K)', '1')
    a.add_button('Запустить', clicker)

    root.mainloop()
    
if __name__ == "__main__":
    viewer()
    solve()