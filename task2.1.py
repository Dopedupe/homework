a = (input("Введите целое число\n"))

b = a[::-1]
b  = int(b)
if ((b>-2**7)and (b<2**7-1)):
    print ("solution eists")
else:
    print("no solution")