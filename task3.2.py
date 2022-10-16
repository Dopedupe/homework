import itertools

def main():
    a = eval(input("Задайте список целых чисел\n"))
    b = []

    a = sorted(a)

    b = list(map(list, itertools.permutations(a)))

    print(b)

if __name__ == '__main__':
    main()
