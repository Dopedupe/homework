def main():
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]

    l1 = set(list1)
    l2 = set(list2)
    
    l3 = l1.intersection(l2) 
    a = l1.union(l2)
    b = l1.difference(l2)
    c = l2.difference(l1)

    print(l3,len(a)-len(l3),len(b),len(c), sep='\n')
if __name__ == '__main__':
    main()

