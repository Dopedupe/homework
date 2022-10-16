def main():
    a = eval(input())
    b = []
    res = []

    def all_char(x, y):
        x = sorted(x)
        y = sorted(y)
        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True

    b = [a[i] for i in range(len(a))]
    all_elem = []

    for i in range(len(a)-1):
        c = []
        a = [b[i] for i in range(len(b))]
        for j in range(i+1,len(a)):
            if len(a[i]) == len(a[j]) and all_char(a[i],a[j]) == True:
                if a[i] not in c or a[j] not in c:
                    if a[i] not in c and a[j] not in c and (a[i] and a[j]) not in all_elem:
                        c.append(a[i])
                        c.append(a[j])
                        all_elem.append(a[i])
                        all_elem.append(a[j])
                    if a[i] not in all_elem:
                        if a[i] not in c:
                            c.append(a[i])
                        all_elem.append(a[i])
                    if a[j] not in all_elem:
                        if a[j] not in c:
                            c.append(a[j])
                        all_elem.append(a[j])
        if len(c) != 0:
            res.append(c)
        if a[i] not in all_elem:
            res.append([a[i]])
    if a[len(a)-1] not in all_elem:
            res.append([a[len(a)-1]])
    for i in range(len(a)):
        if i not in all_elem:
            pass
    print(res)
if __name__ == "__main__":
    main()