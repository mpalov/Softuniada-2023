def pascal_triangle(num):
    row = [1]
    for n in range(1, num + 1):
        row.append(row[n - 1] * (num - n + 1) // n)
    return row


number = int(input())
row = pascal_triangle(number)
print(*row)
