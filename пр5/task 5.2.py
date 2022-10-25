from itertools import combinations
A = [1,2,3,4,4]
res = set ()
A = set (A)
for x in range(1,len (A) +1):
    temp = combinations (A, x)
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