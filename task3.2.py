import itertools

a = eval(input())
b = []

a = sorted(a)

b = list(map(list, itertools.permutations(a)))

print(b)
