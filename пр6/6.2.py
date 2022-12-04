def santa_users(a):
    for i in a:
        if len(i)%2==1:
            i.append('None') 
    return print(dict(a))
    
if __name__ == '__main__':
    santa_users([["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]])