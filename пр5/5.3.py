import itertools

near_digit = {"1": {"1", "2", "4"},
              "2": {"1", "2", "5"},
              "3": {"2", "3", "6"},
              "4": {"1", "4", "5", "7"},
              "5": {"2", "4", "5", "6", "8"},
              "6": {"3", "5", "6", "9"},
              "7": {"4", "7", "8"},
              "8": {"5", "7", "8", "9", "0"},
              "9": {"6", "8", "9"},
              "0": {"8", "0"}}

def add_number(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
         c.append(a[i]+b[j])
    return c

def get_pins(pin):
    codes = []
    codes += sorted(list(near_digit[str(pin[0])]))
    for i in range(1, len(pin)):
        temp = sorted(list(near_digit[str(pin[i])]))
        codes = add_number(codes, temp)
    codes = sorted(set(codes))
    return codes
    
if __name__ == '__main__':
    pin = str(input("PIN: "))
    print(get_pins(pin))