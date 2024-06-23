N, S, R = map(int, input().split())

team_a = set(map(int, input().split()))
team_b = set(map(int, input().split()))

ans = 0

diff = team_a & team_b
team_a = list(team_a - diff)
team_b = list(team_b - diff)

if not team_a:
    ans = 0
else:
    team_a.sort()

    for t in team_a:
        if t - 1 in team_b:
            team_b.remove(t - 1)
        elif t + 1 in team_b:
            team_b.remove(t + 1)
        else:
            ans += 1

print(ans)
