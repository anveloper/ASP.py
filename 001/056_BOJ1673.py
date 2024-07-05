while True:
    try:
        y = 0
        n, k = map(int, input().split())
        y += n
        while n // k:
            y += n // k
            n = n // k + n % k
        print(y)
    except:
        break
