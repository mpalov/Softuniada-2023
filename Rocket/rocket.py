def redo_char(s, count):
    return s * count

n = int(input())

first_row = redo_char("_", n // 2 + 2) + "^" + redo_char("_", n // 2 + 2)
print(first_row)

second_row = redo_char("_", n // 2 + 1) + "/|\\" + redo_char("_", n // 2 + 1)
print(second_row)

for i in range(n // 2 + 1):
    print(redo_char("_", n // 2 - i) + "/" + redo_char(".", i) + "|||" +
          redo_char(".", i) + "\\" + redo_char("_", n // 2 - i))

mid_row = "_/" + redo_char(".", n // 2 - 1) + "|||" + redo_char(".", n // 2 - 1) + "\\_"
print(mid_row)

for i in range(n):
    print(redo_char("_", n // 2 + 1) + "|||" + redo_char("_", n // 2 + 1))

down_mid_row = redo_char("_", n // 2 + 1) + "~~~" + redo_char("_", n // 2 + 1)
print(down_mid_row)

for i in range(n // 2):
    print(redo_char("_", n // 2 - i) + "//" + redo_char(".", i) +
          "!" + redo_char(".", i) + "\\\\" + redo_char("_", n // 2 - i))
