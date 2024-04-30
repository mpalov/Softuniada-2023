def biggest_number(n):
    arr = [str(num) for num in n]

    arr.sort(key=lambda x: (x * 4)[:4], reverse=True)

    res = ''.join(arr)

    while res[0] == '0' and len(res) > 1:
        res = res[1:]

    return res


numbers = [int(x) for x in input().split()]
print(biggest_number(numbers))
