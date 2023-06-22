def main():
    a = [[1,2,3,23],[43,12,34,71],[3,51,3,44],[17,18,20,19]]
    b = 4
    kk = ""
    count = 0
    for i in range(b):
        count += 1
        kk+=str(a[0][i]) + " "
    j = 0
    i = b-1
    b -= 1 

    while len(a)**2 != count:
        for k in range(b):
            j += 1
            count += 1
            kk+=str(a[j][i]) + " "
        for k in range(b):
            i -= 1
            count += 1
            kk+=str(a[j][i]) + " "
        for k in range(b-1):
            j -= 1
            count += 1
            kk+=str(a[j][i]) + " "
        for k in range(b-1): 
            i += 1
            count += 1
            kk+=str(a[j][i]) + " "
        b-= 2
    print(a)
    print(kk)
if __name__ =='__main__':
    main()