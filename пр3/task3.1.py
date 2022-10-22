import sys
from itertools import *

def main():
    def nearest(lst, target):
        return min(lst, key=lambda x: abs(x-target))

    num = int(input("Задайте количество элементов в списке\n"))

    if num < 4:
        print("end")
        sys.exit()

    a = eval(input("Задайте список из целых чисел в [] через запятую\n "))
    b = []

    if len(a) != num:
        print("end")
        sys.exit()

    c = int(input())

    summ = []

    for i in combinations(a, 4):
        summ.append(sum(i))
        b.append(i)
        

    res = nearest(summ, c)

    for i in range(len(summ)):
        if res == summ[i]:
            index = i
            break
    print(b[index])
    print(res)


if __name__ == '__main__':
    main()