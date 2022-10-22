



def longest_valid(s):
    match = [0] * (len(s) + 1)
    for i in range(1, len(s)):
        if s[i] in '({[':
            continue
        open = '({['[')}]'.index(s[i])]
        start = i - 1 - match[i - 1]
        if start < 0:
            continue
        if s[start] != open:
            continue
        match[i] = i - start + 1 + match[start - 1]
    best = max(match)
    end = match.index(best)
    return s[end + 1 - best:end + 1]

print(longest_valid("()(({}[](][{[()]}]{})))("))

# if __name__ =="__main__":
#     main()
