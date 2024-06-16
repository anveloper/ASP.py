def min_a(word):
    tot = word.count("a")
    ac = word + word
    cur = ac[:tot].count("a")
    max_a = cur
    for i in range(1, len(word)):
        if ac[i - 1] == "a":
            cur -= 1
        if ac[tot + i - 1] == "a":
            cur += 1
        max_a = max(max_a, cur)
    return tot - max_a


print(min_a(input()))
