list_my = [int(i) for i in input('insert number: ').split()]
i = 0
while i != len(list_my):
    num = list_my[i]
    if num % 2 == 0:
        i += 1
    else:
        print('NO')
        break
else:
    print("all numbers are even")


