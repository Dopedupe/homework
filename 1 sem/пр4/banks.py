def banks(n, bank):
    bank_list = bank.replace('(', '').replace('[', '').replace(']', '').replace(')', '').replace('"', '').split(",")
    bank_list_clear = {}
    for i in range(0,int(len(bank_list))-1):
        if i%2 == 0:
            bank_list_clear[bank_list[i]] = bank_list[i+1]
    return bank_list_clear

def max_robery(bank_list):
    keys = list(bank_list.keys())
    max_sum = []
    max_banks = []
    for i in range(0, len(bank_list)):
        if i == 0:
            max_sum.append(int(bank_list[keys[0]]))
            max_banks.append(keys[0])
        if i == 1:
            if int(bank_list[keys[0]]) > int(bank_list[keys[1]]):
                max_sum.append(int(bank_list[keys[0]]))
                max_banks.append(keys[0])
            else:
                max_sum.append(int(bank_list[keys[1]]))
                max_banks.append(keys[1])
        if i > 1:
            if max_sum[i-2] + int(bank_list[keys[i]]) > max_sum[i-1]:
                max_sum.append(max_sum[i-2] + int(bank_list[keys[i]]))
                max_banks.append(max_banks[i-2] +" "+ keys[i])

            else:
                max_sum.append(max_sum[i-1])
                max_banks.append(max_banks[i-1] + " " + keys[i])
    
    temp = max_banks[max_sum.index(max(max_sum))].split()
    max_banks = {}

    for i in temp:
        max_banks[i] = keys.index(i) + 1
    print(max(max_sum),max_banks)

if __name__ == '__main__':
    n = int(input("Numbers: "))
    bank = input("Write banks: ")
    max_robery(banks(n, bank))