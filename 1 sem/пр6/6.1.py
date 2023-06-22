r_n = dict(I= 1,V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)

def r_to_a(n):   
    res = 0
    for i,j in enumerate(n):
        if i+1<len(n) and r_n[n[i]] < r_n[n[i+1]]:
            res -= r_n[n[i]]
        else:
            res += r_n[n[i]]
    return(res)

if __name__ == '__main__':
    print(r_to_a('XIV'))