mok, dog = map(int, input().split())
rest = dog - mok
if rest == 0:
    print(0)
elif rest == 1:
    print(1)
elif rest == 2:
    print(2)
else:
    for i in range(1, 100000000):
        if i * (i + 1) < rest <= i * (i + 1) + (i + 1):
            print(i * 2 + 1)
            break
        if i * (i + 1) + (i + 1) < rest <= (i + 1) * (i + 2):
            print(i * 2 + 2)
            break
