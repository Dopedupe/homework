def main():
    a=input("Введите целое число\n")
    if a == a[::-1]:
        print("true")
    else:
        print("false")
if __name__ == '__main__':
    main()