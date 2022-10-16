def main():
    a = input("Введите текст\n")
    b = (" ".join(a.split()))
    
    s = ''
    i = len(b)-1
    while i >= 0:
        if b[i] == ' ':
            s = s + b[i+1:] + ' '
            b = b[:i]
            i = len(b) - 1
        else:
            i -= 1
    s = s + b
    
    print(s.capitalize())    
            
   
if __name__ == '__main__':
    main()