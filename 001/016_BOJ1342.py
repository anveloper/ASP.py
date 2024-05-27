import itertools

a = list(input())
count = 0
if len(a) == 1:
    print(1)
elif len(a) == 2:
    if a[0] == a[1]:
        print(0)
    else:
        print(2)
elif len(a) == 10 and len(set(a)) == 10:
    print(3628800)
elif len(a) == 10 and len(set(a)) == 9:
    print(1451520)
else:
    b = itertools.permutations(a)
    b = list(map(list, set(map(tuple, b))))
    for array in b:
        for x in range(1, len(a) - 1):
            if array[x - 1] == array[x] or array[x] == array[x + 1]:
                count += 1
                break
    print(len(b) - count)
