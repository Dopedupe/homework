import sys

a, n = input("Введите слово и число через запятую\n").split(',')
n = int(n)
k = n - 2
if n == 1:
    print(a)
    sys.exit()
if n == 2:
    print(a[0::2] + a[1::2])
    sys.exit()
temp = ""
res = "" + a[0::n+k]

for i in range(n + k):
    temp += a[i::n+k] +","

temp = temp[:-1:]
def del_coma(te,num1):
    count = 1
    for i in range(len(te)):
        if te[i] == ",":
            count+=1
    for j in range(num1-1):
        t = te
        for i in range(0,len(t)):
            if t[i] == ",":
                te = te[1::]
                break
            else:
                te = te[1::]
    t = te
    count_small = 0
    for i in reversed(range(0, len(t))):
        if t[i] == "," and count_small != count - num1:
            te = te[:-1:]
            count_small += 1
        elif count_small == count - num1:
            break
        else:
            te = te[:-1:]
    return te

def ctrl_v(word, diag):
    llen = min(len(word),len(diag))
    text = ""
    for i in range(llen):
        text += word[i] + diag[i]
    if len(text) < len(word) + len(diag):
        text += word[len(word)-1]
    return text
i = 0

while True:
    res = res + ctrl_v(del_coma(temp,2 + i), del_coma(temp, n+k - i))
    i += 1
    if i == k:
        break
res += a[n-1::n+k]
print(res)
