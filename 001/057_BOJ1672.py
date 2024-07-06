DNA = {
    "AA": "A",
    "AG": "C",
    "AC": "A",
    "AT": "G",
    "GA": "C",
    "GG": "G",
    "GC": "T",
    "GT": "A",
    "CA": "A",
    "CG": "T",
    "CC": "C",
    "CT": "G",
    "TA": "G",
    "TG": "A",
    "TC": "G",
    "TT": "T",
}
N = int(input())
S = input().rstrip()
S = "".join(reversed(list(S)))
tmp = S[0]
for i in range(1, N):
    tmp = DNA[tmp + S[i]]
print(tmp)
