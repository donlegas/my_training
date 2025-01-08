my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

x = 0
while x < len(my_list):
    i = my_list[x]
    if i > 0:
        print(i)
        x = x + 1
    if i == 0:
        x = x + 1
        continue
    if i < 0:
        break