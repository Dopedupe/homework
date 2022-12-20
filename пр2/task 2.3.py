def main(s):
    long_list = [0] * (len(s) + 1)
    for i in range(1, len(s)):
        if s[i] in '({[':
            continue
        open = '{[('['}])'.index(s[i])]
        opener_index = i - 1 - long_list[i - 1]
        if opener_index < 0:
            continue
        if s[opener_index] != open:
            continue
        long_list[i] = i - opener_index + 1 + long_list[opener_index - 1]
        
    longest = max(long_list)
    end_index = long_list.index(longest)
    if longest:
        return s[end_index+1-longest:end_index+1]
    if st == s:
        return True
    else:
        return False
st = input("Введите последовательность скобок\n")
print(main(st))


 


