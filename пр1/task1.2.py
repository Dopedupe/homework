def main():
    a = (input("Введите целое число\n"))
    if a[0] == '-':
        c = a[:0] + a[1:]
        b = c[::-1]
        b = a[0] + b
        b  = int(b)
        print(b)
        if ((b>-2**7)and (b<2**7-1)):
            print ("solution eists")
        else:
            print("no solution")
    else:
        b = a[::-1]
        b  = int(b)
        print(b)
        if ((b>-2**7)and (b<2**7-1)):
            print ("solution exists")
        else:
            print("no solution")
if __name__=='__main__':
    main()