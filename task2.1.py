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
    count = 1
    max_count = 0
    for i in range(1,len(a)):
        if (a[i-1] != a[i]):
            b = b + a[i-1] + a[i]
            if (check(b)):
                b = b[:-1:]
                count += 1
            else:
                b = b[1:-1:]
                c = b
                b = ""
                max_count = count
                count = 1
        
    
    if max_count == 0 or max_count < count:
        print(b + a[i])
    else:
        print(c) 
    
if __name__ == "__main__":
    main()
    