def check(text):
    for i in range(len(text) - 1):
        for j in range(i + 1, len(text)):
            if text[i] != text[j]:
                pass
            else:
                return False

    return True

def main():
    a = input("Введите строку\n")
    b = ""
    c = ""
    for i in range(0,len(a)):
        b = a[i::]
        if (check(b)):
            if len(c) < len(b):
                c = b
                b = ""
    for i in range(0,len(a)):
        b = a[:i:]
        if (check(b)):
            if len(c) < len(b):
                c = b
                b = ""
    print(c)

if __name__ == "__main__":
    main()
