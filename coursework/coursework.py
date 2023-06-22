from typing import Callable, TextIO
import pygame as pg
from tkinter import *


class Tkinter_input:
    """Абстрактный класс для создания полей и кнопок"""

    def __init__(self, master: Tk) -> None:
        """
        Инициализация
        :param master:
            Окно
        """
        self.entries = []
        self.root = master
        self.root.resizable(False, False)

    def mainloop(self) -> None:
        """Цикл окна"""
        self.root.mainloop()

    def add_label(self, text_label: str, val: str) -> None:
        """
        Добавление надписи и поля для ввода
        :param text_label:
            Надпись над полем для ввода
        :param val:
            Параметр для функции валидации
        """
        lbl = Label(self.root, text=text_label)
        lbl_text = Entry(self.root, width=30, validate='key',
                         validatecommand=(self.root.register(self.valid), '%P', val))
        lbl.pack()
        lbl_text.pack()
        self.entries.append(lbl_text)

    def add_button(self, text_button: str, func: Callable) -> None:
        """
        Добавлении кнопки
        :param text_button:
            Надпись кнопки
        :param func:
            Функция для исполнения при нажатии на кнопку
        """
        myButton = Button(self.root, text=text_button, command=func)
        myButton.pack(pady=10)

    def valid(self, new_value: str, val: str) -> bool:
        """
        Функция валидации
        :param new_value:
            Значение из поля
        :param val:
            Параметр опредиляюций способ валидации
        :return:
        """
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


class Viewer(Tkinter_input):
    """Окно для ввода параметров шахматной доски"""

    def __init__(self) -> None:
        """Создание полей окна"""
        super().__init__(Tk())

        self.root.title("Шахматы")
        self.root.geometry("200x180")

        self.add_label('Размер доски (N)', '1')
        self.add_label('Кол-во требуемых фигур (L)', '1')
        self.add_label('Кол-во размещенных фигур (K)', '1')
        self.add_button('Запустить', self.clicker)

    def clicker(self) -> None:
        """Взятие значений из полей, удаление, создание окна для ввода K расставленных фигур"""
        N = int(self.entries[0].get())
        L = int(self.entries[1].get())
        K = int(self.entries[2].get())

        self.root.destroy()

        second_window = ViewerK(N, L, K)


class ViewerK(Tkinter_input):
    """Окно для ввода координат K расставленных фигур"""

    def __init__(self, N: int, L: int, K: int) -> None:
        """Создание полей окна"""
        super().__init__(Tk())

        self.N = N
        self.L = L

        self.root.title("Tesy")
        self.root.geometry("200x{0}".format(50 * K + 75))  # добавить второй столюик, если больше 10

        for i in range(1, K + 1):
            self.add_label('Введите координаты:\n№{0}'.format(i), '2')
        self.add_button("Создать", self.add_k)

    def add_k(self) -> None:
        """Запись координат расставленных фигур, удаление окна, поиск решений"""
        coords = []
        for i in self.entries:
            coords.append(tuple(map(int, i.get().split(' '))))

        self.root.destroy()

        sol = Solutions(self.N, self.L, coords)
        sol.solve()


class Solutions:
    """Класс для поиска решений (расстановок шахматных фигур)"""
    MAX_N = 20
    FREE = 0
    BUSY = 1
    ATTACKED = 2

    def __init__(self, N: int, L: int, coords: list[tuple[int]]) -> None:
        """
        Инициализация основных параметров шахматной доски
        :param N:
            Размер доски
        :param L:
            Сколько фигур нужно еще расставить
        :param coords:
            Координаты расставленных фигур
        """
        self.IS_FINDED = 0  # флаг, что хоть одна расстановка найдена (= кол-во расстановок)

        self.N = N
        self.L = L
        self.coords = coords

    def set_attacked(self, chessboard: list[list[int]], x: int, y: int, n: int) -> None:
        """
        Просчет атаки фигуры

        :param chessboard:
            Шахматная доска двухмерный массив
        :param x:
            Координата
        :param y:
            Координата
        :param n:
            Размер шахматной доски
        """
        for i in range(-2, 3, 1):  # устанавливаем атаку на диагоналях
            if i == 0:
                continue
            if x + i >= 0 and y + i >= 0 and x + i < n and y + i < n:
                chessboard[x + i][y + i] = self.ATTACKED
            if x + i >= 0 and y - i >= 0 and x + i < n and y - i < n:
                chessboard[x + i][y - i] = self.ATTACKED

        for i in range(-3, 4, 6):  # устанавливаем атаку на прямых
            if x + i >= 0 and x + i < n:
                chessboard[x + i][y] = self.ATTACKED
            if y + i >= 0 and y + i < n:
                chessboard[x][y + i] = self.ATTACKED

    def output(self, chessboard: list[list[int]], n: int, output_file: TextIO) -> None:
        """
        Вывод расстановки в файл

        :param chessboard:
            Шахматная доска двухмерный массив
        :param n:
            Размер шахматной доски
        :param output_file:
            Файл для вывода решения
        """
        for x in range(0, n):
            for y in range(0, n):
                if chessboard[x][y] == self.BUSY:
                    output_file.write("({0},{1}) ".format(x, y))
        output_file.write("\n")

    def search_solutions(self, chessboard: list[list[int]], n: int, l: int, k: int, x_prev: int, y_prev: int,
                         output_file: TextIO) -> None:
        """
        Поиск Решений

        :param chessboard:
            Шахматная доска двухмерный массив
        :param n:
            Размер шахматной доски
        :param l:
            Сколько фигур нужно еще расставить
        :param k:
            Сколько фигур уже расставлено
        :param x_prev:
            Предыдущая координата
        :param y_prev:
            Предыдущая координата
        :param output_file:
            Файл для вывода решения
        """
        board = [[0] * self.MAX_N for i in range(self.MAX_N)]  # доп. доска
        for x in range(x_prev,
                       n):  # начинаем проходить по полям с прошлой итерации (или с начальной 0 0), ищем свободное поле
            y1 = y_prev if x == x_prev else 0
            for y in range(y1, n):
                if chessboard[x][y] == self.FREE:  # если поле свободно, то
                    for x1 in range(0, n):  # копируем доску в доп. доску
                        for y1 in range(0, n):
                            board[x1][y1] = chessboard[x1][y1]
                    board[x][y] = self.BUSY  # занимаем поле
                    self.set_attacked(board, x, y, n)  # отмечаем поля, находящиеся под ударом
                    if k + 1 == l:  # если кол-во расставленных фигур равно L, то
                        if self.IS_FINDED == 0:
                            self.IS_FINDED += 1  # флаг, что хоть одна расстановка найдена
                            win = Window(self, n, board, 1)
                            win.mainloop()
                        self.output(board, n, output_file)  # вывод расстановки в файл
                    else:
                        self.search_solutions(board, n, l, k + 1, x, y,
                                              output_file)  # вызов ф-ции для следующей установки фигуры

    def solve(self) -> None:
        """Поиск и вывод решений"""
        output_file = open("output.txt", mode="w")  # для очищения файла вывода
        output_file.close()

        chessboard = [[0] * self.MAX_N for i in range(self.MAX_N)]

        for x, y in self.coords:  # ввод начальной расстановки из файла
            if x >= self.N or y >= self.N:  # no solutions
                win = Window(self, self.N, chessboard, 0)
                win.mainloop()
            if self.L == 0:  # если L == 0, то выводим в файл начальную расстановку
                self.IS_FINDED = 1
                break
            chessboard[x][y] = self.BUSY  # занимаем поле
            self.set_attacked(chessboard, x, y, self.N)  # отмечаем поля, находящиеся под ударом

        with open("output.txt", mode="a") as output_file:  # открываем файл для вывода перед вызовом рекурсивной функции
            self.search_solutions(chessboard, self.N, self.L, 0, 0, 0, output_file)  # поиск всех возможных расстановок

        if self.IS_FINDED == 0:  # если расстановки не найдены, вывод no solutions
            win = Window(self, self.N, chessboard, 0)
            win.mainloop()


class Window:
    """Окно для вывода решения"""
    RES = 600, 650
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    FPS = 60

    def __init__(self, sol, n: int, board: list[list[int]], mode: int) -> None:
        """
        Инициализация окна pygame

        :param sol:
            Ссылка на Solutions
        :param n:
            Размер шахматной доски
        :param board:
            Шахматная доска двухмерный массив
        :param mode:
            Параметр для вывода 0 - no solutions 1 - вывод окна с решением
        """
        self.sol = sol
        self.n = n
        self.board = board
        self.mode = mode

        self.objects = []
        self.temp = []

        pg.init()
        self.sc = pg.display.set_mode(self.RES)
        self.size = 600 // n
        self.clock = pg.time.Clock()
        self.sc.fill(self.WHITE)
        customButton = Pbutton(self, 0, 600, 600, 50, 'Вывод', self.func)

        for x in range(0, n):
            for y in range(0, n):
                if board[x][y] == self.sol.BUSY:
                    self.temp.append("{0},{1}".format(x, y))

    def func(self) -> None:
        """Вывод решений в файл"""
        if self.mode == 1:
            self.sol.solve()
        else:
            with open("output.txt", "w") as output_file:
                output_file.write("no solutions")
        exit()

    def mainloop(self) -> None:
        """Цикл окна pygame"""
        while True:
            for event in pg.event.get():
                if self.mode == 1:
                    for i in range(len(self.temp)):
                        x1, y1 = self.temp[i].split(',')
                        x1, y1 = int(y1), int(x1)
                        for x in range(0, self.n):
                            for y in range(0, self.n):
                                if x1 == x and y1 == y:
                                    pg.draw.rect(self.sc, self.GREEN,
                                                 (self.size * x, self.size * y, self.size, self.size))
                                    pg.draw.rect(self.sc, self.BLACK,
                                                 (self.size * x, self.size * y, self.size, self.size), 1)
                                else:
                                    pg.draw.rect(self.sc, self.BLACK,
                                                 (self.size * x, self.size * y, self.size, self.size), 1)
                        for i in range(-2, 3, 1):  # устанавливаем атаку на диагоналях
                            if i == 0:
                                continue
                            if x1 + i >= 0 and y1 + i >= 0 and x1 + i < self.n and y1 + i < self.n:
                                pg.draw.rect(self.sc, self.BLUE,
                                             (self.size * (x1 + i), self.size * (y1 + i), self.size, self.size))
                            if x1 + i >= 0 and y1 - i >= 0 and x1 + i < self.n and y1 - i < self.n:
                                pg.draw.rect(self.sc, self.BLUE,
                                             (self.size * (x1 + i), self.size * (y1 - i), self.size, self.size))
                        for i in range(-3, 4, 6):  # устанавливаем атаку на прямых
                            if x1 + i >= 0 and x1 + i < self.n:
                                pg.draw.rect(self.sc, self.BLUE,
                                             (self.size * (x1 + i), self.size * y1, self.size, self.size))
                            if y1 + i >= 0 and y1 + i < self.n:
                                pg.draw.rect(self.sc, self.BLUE,
                                             (self.size * x1, self.size * (y1 + i), self.size, self.size))
                elif self.mode == 0:
                    f1 = pg.font.Font(None, 44)
                    text1 = f1.render('No solutions', True, (255, 50, 50))
                    place = text1.get_rect(center=(300, 275))
                    self.sc.blit(text1, place)
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            for object in self.objects:
                object.process()

            self.sc.blit(self.sc, (0, 0))
            pg.display.flip()
            self.clock.tick(self.FPS)


class Pbutton:
    """Кнопка для окна Pygame"""

    def __init__(self, root: Window, x: int, y: int, width: int, height: int, buttonText: str = 'Button',
                 onclickFunction: Callable = None, onePress: bool = False) -> None:
        """
        Инициализация кнопки pygame

        :param root:
            Окно где будет отображаться кнопка
        :param x:
            Координата
        :param y:
            Координата
        :param width:
            Ширина
        :param height:
            Высота
        :param buttonText:
            Текст кнопки
        :param onclickFunction:
            Функция для исполнения при нажатии на кнопку
        :param onePress:
            Параметр определяющий возможность повторного нажатия на кнопку
        """
        self.root = root
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

        root.objects.append(self)

    def process(self) -> None:
        """Отслеживание нажатия на кнопку"""
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
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.root.sc.blit(self.buttonSurface, self.buttonRect)


def main():
    app = Viewer()
    app.mainloop()


if __name__ == "__main__":
    main()
