n = int(input())

digits = 1
while n > 9 * digits * 10 ** (digits - 1):
    n -= 9 * digits * 10 ** (digits - 1)
    digits += 1
start = 10 ** (digits - 1)
target = start + (n - 1) // digits
index = (n - 1) % digits

print(int(str(target)[index]))
