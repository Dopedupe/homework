from itertools import combinations
def main():
    a = [1,2,3,4,4]
    res = set ()
    a = set (a)
    for x in range(1,len (a) +1):
        temp = combinations (a, x)
        for i in (set (temp)) :
            res.add (i)
    res = sorted (sorted (res) , key=len)
    ress ="{"
    for i in res:
        i = set(i)
        ress += str(i).replace(' ','') +','
    ress = ress [:-1:] +"}"
    print(ress)
    print(len(res))
if __name__ =='__main__':
    main()