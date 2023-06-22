import math

from decimal import Decimal
def solve(candy, pack):
    res = 0
    if pack > candy:
        return "No solution"
    else:
        for i in range(pack + 1):
            res += pow(-1, pack-i) * pow(i, candy) * (math.comb(pack, i))
    return Decimal(res) / math.factorial(pack)

if __name__ == '__main__':
    n, k = input("Write candies and packs: ").split(" ")
    print(solve(int(n), int(k)))