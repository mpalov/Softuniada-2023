def lvp(ch):
    stack = []
    res = 0

    for i in range(len(ch)):
        curr_ch = ch[i]
        if curr_ch == ')':
            if stack and stack[-1][0] == 0:
                stack.pop()
                res = max(res, i - (-1 if not stack else stack[-1][1]))
            else:
                stack.append((1, i))
        else:
            stack.append((0, i))

    return res


chars = input()
print(lvp(chars))
